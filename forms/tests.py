import datetime
from django.test import TestCase
from django.urls import reverse
from forms.models import AbsentDaysAllowed, AbsenceRequest
from login.models import Employee
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import TimeoutException


class AbsenceRequestTestCase(TestCase):
    """Testing class for absence request model"""

    def setUp(self):
        """Set up initial test data for all tests in this class"""
        self.manager = Employee.objects.create(clock_number="123456", email="manager@email.com", name="Manager Name", role="Manager")
        self.floor = Employee.objects.create(clock_number="654321", email="floor@email.com", name="Floor Employee", role="Floor Role")

        self.valid_form_data = {
            'clock_number': '123456',
            'start_date': '2024-01-01',
            'end_date': '2024-01-05',
            'shift_number': '1st',
            'hours_gone': 8,
            'absence_type': 'vacation',
        }

        self.invalid_form_data = {
            'start_date': '2024-01-01',
            'shift_number': '1st',
            'hours_gone': 8,
            'absence_type': 'vacation',
        }

    def test_valid_absence_request_creation(self):
        """Test valid creation of an AbsenceRequest object"""
        ar = AbsenceRequest.objects.create(
            clock_number=12345,
            start_date="2024-02-08",
            end_date="2024-02-10",
            approval_status="pending",
            shift_number="1st",
            hours_gone=16,
            absence_type="vacation",
            approval=self.manager,
            filled_by=self.floor,
        )
        self.assertEqual(ar.start_date.strftime("%Y-%m-%d"), "2024-02-08")
        self.assertEqual(ar.end_date.strftime('%Y-%m-%d'), "2024-02-10")
        self.assertEqual(ar.approval_status, "pending")
        self.assertEqual(ar.shift_number, "1st")
        self.assertEqual(ar.hours_gone, 16)
        self.assertEqual(ar.absence_type, "vacation")
        self.assertEqual(ar.approval, self.manager)
        self.assertEqual(ar.filled_by, self.floor)

    def test_invalid_form_submission(self):
        """Test the behavior of invalid form submission for AbsenceRequest"""
        response = self.client.post(reverse('submit_absence_request'), self.invalid_form_data)
        self.assertEqual(AbsenceRequest.objects.count(), 0)

    def test_requests_page_content(self):
        """Test if the requests page correctly displays AbsenceRequest objects"""
        AbsenceRequest.objects.create(**self.valid_form_data)
        response = self.client.get(reverse('requests'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('requests' in response.context)
        self.assertEqual(len(response.context['requests']), 1)

class CalendarViewTestCase(TestCase):
    """Testing class for calendar view"""

    def test_calendar_view(self):
        """Test if the calendar view loads successfully"""
        response = self.client.get(reverse('calendar'))
        self.assertEqual(response.status_code, 200)

class JavaScriptTests(StaticLiveServerTestCase):
    """Testing class for JavaScript functionalities"""

    @classmethod
    def setUpClass(cls):
        """Set up the test environment for JavaScript tests"""
        super().setUpClass()
        cls.selenium = webdriver.Chrome()  # Choose the appropriate driver
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        """Tear down the test environment for JavaScript tests"""
        cls.selenium.quit()
        super().tearDownClass()

    def test_update_date_time(self):
        """Test if the date and time are updated correctly on the webpage"""
        self.selenium.get(self.live_server_url + '/calendar')
        date_element = WebDriverWait(self.selenium, 10).until(EC.presence_of_element_located((By.ID, "date")))
        time_element = WebDriverWait(self.selenium, 10).until(EC.presence_of_element_located((By.ID, "time")))
        self.assertNotEqual(date_element.text, "")
        self.assertNotEqual(time_element.text, "")


    def get_displayed_month_year(self):
        calendar_title = self.selenium.find_element(By.ID, 'calendar-title').text
        return datetime.datetime.strptime(calendar_title, '%B %Y')

    def test_navigate_calendar(self):
        self.selenium.get('http://localhost:8000/calendar')  # Adjust URL as needed
        wait = WebDriverWait(self.selenium, 10)

        current_month_year = self.get_displayed_month_year()

        # Test for previous month navigation
        prev_button = wait.until(EC.element_to_be_clickable((By.ID, 'prevMonth')))
        prev_button.click()

        prev_month_year = self.get_displayed_month_year()
        expected_prev_month_year = current_month_year.replace(day=1) - datetime.timedelta(days=1)
        self.assertEqual(prev_month_year.year, expected_prev_month_year.year)
        self.assertEqual(prev_month_year.month, expected_prev_month_year.month)

        # Test for next month navigation
        next_button = wait.until(EC.element_to_be_clickable((By.ID, 'nextMonth')))
        next_button.click()
        next_button.click()  # Click twice to go to the next month from the original

        next_month_year = self.get_displayed_month_year()
        expected_next_month_year = current_month_year + datetime.timedelta(
            days=31)  # Assuming 31 days in the month for simplicity
        self.assertEqual(next_month_year.year, expected_next_month_year.year)
        self.assertEqual(next_month_year.month, expected_next_month_year.month)

    def test_fetch_absent_and_requested_days(self):
        # Create some AbsentDaysAllowed data
        AbsentDaysAllowed.objects.create(shiftDay=datetime.date.today(), allowedAbsent=2)

        # Create an AbsenceRequest that is not rejected
        AbsenceRequest.objects.create(
            start_date=datetime.date.today(),
            end_date=datetime.date.today() + datetime.timedelta(days=1),
            approval_status="approved",  # or "pending"
            shift_number="1st",
            hours_gone=8,
            absence_type="pto",
            clock_number=123456
        )

        # Load the calendar page
        self.selenium.get(self.live_server_url + reverse('calendar'))

        # Wait until the calendar is loaded
        WebDriverWait(self.selenium, 10).until(
            EC.presence_of_element_located((By.ID, 'calendar-title'))
        )

        # Fetch the absent and requested days data displayed on the calendar
        calendar_dates = self.selenium.find_elements(By.CLASS_NAME, 'calendar-date')
        calendar_data = []

        for date in calendar_dates:
            if date.text != '':
                # Check for the presence of 'Allowed Absent' and 'Requested Off' data
                innerHTML = date.get_attribute('innerHTML')
                absent_info = "Allowed Absent:" in innerHTML
                requested_info = "Requested Off:" in innerHTML
                calendar_data.append((date.text, absent_info, requested_info))

        # Check if the calendar has the correct data for today
        today = datetime.date.today()
        today_str = today.strftime('%d')  # Assuming the calendar displays the day as 'DD'

        self.assertIn((today_str, True, True), calendar_data, "Absent or requested days data not displayed correctly")

    def test_count_requested_days(self):
        # Load the calendar page
        self.selenium.get(self.live_server_url + '/calendar')

        # Wait until the calendar is loaded
        WebDriverWait(self.selenium, 10).until(
            EC.presence_of_element_located((By.ID, 'calendar-title'))
        )

        # Fetch the requested days data displayed on the calendar
        calendar_dates = self.selenium.find_elements(By.CLASS_NAME, 'calendar-date')
        requested_dates_count = {}

        for date in calendar_dates:
            if date.text != '':
                # Check for the presence of 'Requested Off' data
                requested_off_info = date.get_attribute('innerHTML')
                if 'Requested Off:' in requested_off_info:
                    date_text = date.text
                    # Extract only the numerical part from the string
                    count_str = requested_off_info.split('Requested Off: ')[1].split('<')[0]
                    count = int(count_str)  # Convert the string to an integer
                    requested_dates_count[date_text] = count

        # Assertions
        # Check if the counts are correct
        for date, count in requested_dates_count.items():
            self.assertTrue(count >= 0, f"Count for date {date} should be non-negative")

        # Check if dates with high requests are highlighted
        high_request_dates = self.selenium.find_elements(By.CLASS_NAME, 'high-request')
        for date in high_request_dates:
            date_text = date.text
            self.assertIn(date_text, requested_dates_count, "High request dates should be in the count list")
            self.assertTrue(requested_dates_count[date_text] > 0, f"High request date {date_text} should have requests")

    def test_update_allowed_absent(self):
        # Go to the calendar page
        self.selenium.get(f'{self.live_server_url}/calendar')

        # Click on a specific date in the calendar
        date_element = self.selenium.find_element(By.CSS_SELECTOR, '.calendar-date:not(.empty-date)')
        date_element.click()

        # Simulate entering a new value in the prompt
        new_allowed_absent = 3
        Alert(self.selenium).send_keys(str(new_allowed_absent))
        Alert(self.selenium).accept()

        # Handle the alert and assert its text
        try:
            alert = WebDriverWait(self.selenium, 10).until(EC.alert_is_present())
            alert_text = alert.text
            alert.accept()
            self.assertEqual(alert_text, "Update failed!", "The alert text did not match the expected message.")
        except TimeoutException:
            self.fail("Expected alert did not appear.")

    def test_generate_calendar(self):
        # Navigate to the calendar page
        self.selenium.get(f'{self.live_server_url}/calendar')

        # Set specific month and year
        specific_year = 2024
        specific_month = 1  # February (0-indexed in JavaScript)
        self.selenium.execute_script(f'currentYear = {specific_year}; currentMonth = {specific_month};')

        # Call generateCalendar
        self.selenium.execute_script('generateCalendar(currentYear, currentMonth);')

        # Check if the calendar is correctly generated
        try:
            calendar_title = WebDriverWait(self.selenium, 10).until(
                EC.presence_of_element_located((By.ID, "calendar-title"))
            )
            self.assertIn("February 2024", calendar_title.text,
                          "Calendar title does not match the expected month and year.")

        except TimeoutException:
            self.fail("Calendar generation failed or took too long.")
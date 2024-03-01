# steps.py
from behave import given, then, when
from selenium import webdriver
from selenium.webdriver.common.by import By
from django.core import mail

# tests for different browsers
@given("The user is using chrome")
def step_impl(context):
    context.browser = webdriver.Chrome

@given("The user is using edge")
def step_impl(context):
    context.browser = webdriver.Edge

@given("The user is using firefox")
def step_impl(context):
    context.browser = webdriver.Firefox


@given("the user has navigated to the login page")
def step_impl(context):
    """The step for putting the test env on the login page"""
    # context.browser.visit(context.get_url("login"))
    context.browser = webdriver.Chrome()
    context.browser.get("http://localhost:8000/")


@given("the user has navigated to the home page")
def step_impl(context):
    """Putting the test environment on the home page"""
    context.browser = webdriver.Chrome()
    context.browser.get("http://localhost:8000/home")


@given("the user has logged in")
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get("http://localhost:8000/home")
    username_input = context.browser.find_element(By.ID, "id_username")
    password_input = context.browser.find_element(By.ID, "id_password")
    username_input.send_keys("Kiosk1")
    password_input.send_keys("freestand1")
    login_button = context.browser.find_element(By.ID, "log-in")
    login_button.click()


@given("a user is logged in and on the absence request form")
def step_impl(context):
    """Logs the user in, then navigates to the absence request Form
    This is a temporary fix until I can get a before run function set up.
    It didn't want to work earlier
    """
    context.browser.get("http://localhost:8000/")
    username_input = context.browser.find_element(By.ID, "username")
    username_input.send_keys("user")
    password_input = context.browser.find_element(By.ID, "password")
    password_input.send_keys("pass")
    login_button = context.browser.find_element(By.ID, "log-in")
    login_button.click()
    # then once we're on the home page
    absence_request_button = context.browser.find_element(By.ID, "absence-request-link")
    absence_request_button.click()


@given("the user is not logged in")
def step_impl(context):
    context.browser.get("http://localhost:8000/")


@given("the user tries to navigate to the home page")
def step_impl(context):
    context.browser.get("http://localhost:8000/home")



@when("the user correctly fills out clock number")
def step_impl(context):
    """The test env correctly fills out the clock number"""
    clock_input = context.browser.find_element(By.ID, "clock")
    clock_input.send_keys("12345")


@when("the user incorrectly fills out clock number")
def step_impl(context):
    """The test env incorrectly fills out the clock number"""
    clock_input = context.browser.find_element(By.ID, "clock")
    clock_input.send_keys("1")


@when("the user correctly selects a shift")
def step_impl(context):
    """The user correctly selects a shift"""
    shift_input = context.browser.find_element(By.ID, "shift")
    shift_input.select_by_index(1)


@when("the user correctly fills out their name")
def step_impl(context):
    """The user correctly fills out their name"""
    name_input = context.browser.find_element(By.ID, "full-name")
    name_input.send_keys("Testy McGee")


@when("the user incorrectly fills out their name")
def step_impl(context):
    """The user incorrectly fills out their name.
    In this case, it's an integer"""
    name_input = context.browser.find_element(By.ID, "full-name")
    name_input.send_keys(14)


@when("the user correctly selects a start date")
def step_impl(context):
    """The user correctly selects a start date"""
    date_input = context.browser.find_element(By.ID, "first-day-absent")
    date_input.send_keys("12-20-2024")


@when("the user incorrectly selects a start date")
def step_impl(context):
    """The user incorrectly selects a start date.
    In this case, it's in the past."""
    date_input = context.browser.find_element(By.ID, "first-day-absent")
    date_input.send_keys("12-20-2001")


@when("the user correctly selects a return date")
def step_impl(context):
    """The user correctly selects a return date."""
    date_input = context.browser.find_element(By.ID, "last-day-absent")
    date_input.send_keys("1-5-2025")


@when("the user incorrectly selects a return date")
def step_impl(context):
    """The user incorrectly selects a return date.
    In this case, it's in the past."""
    date_input = context.browser.find_element(By.ID, "last-day-absent")
    date_input.send_keys("1-5-2001")


@when("the user correctly selects the amount of hours")
def step_impl(context):
    """The user correctly selects the amount of hours"""
    hours_input = context.browser.find_element(By.ID, "hours")
    hours_input.send_keys(136)


@when("the user incorrectly selects the amount of hours")
def step_impl(context):
    """The user incorrectly selects the amount of hours,
    in this case it's negative"""
    hours_input = context.browser.find_element(By.ID, "hours")
    hours_input.send_keys(-1)


@when("the user correctly selects the reason for time off")
def step_impl(context):
    """The user correctly selects the reasoning for time off"""
    reason_input = context.browser.find_element(By.ID, "absence-type")
    reason_input.select_by_index(0)


@when("the user correctly selects their approving supervisor")
def step_impl(context):
    """The user correctly selects the approving supervisor"""
    super_input = context.browser.find_element(By.ID, "approving-supervisor")
    super_input.send_keys("Supervisor McGee")


@when("the user incorrectly selects their approving supervisor")
def step_impl(context):
    """The user incorrectly selects their approving supervisor"""
    super_input = context.browser.find_element(By.ID, "approving-supervisor")
    super_input.send_keys("Myself")


@when("The user correctly enters their email")
def step_impl(context):
    """The user correctly enters their email"""
    email_input = context.browser.find_element(By.ID, "email")
    email_input.send_keys("testy_mcgee@test.com")


@when("The user incorrectly enters their email")
def step_impl(context):
    """The user enters an incorrect email"""
    email_input = context.browser.find_element(By.ID, "email")
    email_input.send_keys("testy_mcgee@")


@when("the user submits the login form with valid credentials")
def step_impl(context):
    """Fills in the login form with valid credentials and submits it"""
    # context.browser.fill("username", "user")
    username_input = context.browser.find_element(By.ID, "id_username")
    password_input = context.browser.find_element(By.ID, "id_password")
    username_input.send_keys("kiosk1")
    # context.browser.fill("password", "pass")
    password_input.send_keys("freestand1")
    login_button = context.browser.find_element(By.ID, "log-in")
    login_button.click()


@when("the user submits the login form with incorrect credentials")
def step_impl(context):
    """Fills in the login form with incorrect credentials and submits it"""
    username_input = context.browser.find_element(By.ID, "id_username")
    username_input.send_keys("user_wrong")
    password_input = context.browser.find_element(By.ID, "id_password")
    password_input.send_keys("pass_wrong")
    login_button = context.browser.find_element(By.ID, "log-in")
    login_button.click()


@when("the user clicks on the absence request button")
def step_impl(context):
    """Clicks on the absence request link"""
    absence_request_button = context.browser.find_element(By.ID, "absence-request-link")
    absence_request_button.click()


@when("the user submits the absence request form")
def step_impl(context):
    """Submits the absence request form"""
    absence_request_submit = context.browser.find_element(By.ID, "submit")
    absence_request_submit.click()


@then("the user should not be redirected to the home page")
def step_impl(context):
    """Checks if the test env is not on the home page"""
    assert context.browser.current_url != "http://localhost:8000/home", (
        f"Expected url to be on login page, "
        f"instead is on {context.browser.current_url}"
    )
    context.browser.quit()


@then("the user is redirected to the login page")
def step_impl(context):
    assert context.browser.current_url != "http://localhost:8000/home", (
        f"expected to be on login page, " f"instead is on {context.browser.current_url}"
    )
    context.browser.quit()


@then("the user should be redirected to the home page")
def step_impl(context):
    """Checks if the test env is on the home page"""
    assert context.browser.current_url == "http://localhost:8000/home", (
        f"Expected url to be on home page, "
        f"instead is on {context.browser.current_url}"
    )
    context.browser.quit()


@then("the user is redirected to the absence request form")
def step_impl(context):
    """Checks if the test env is on the absence request form"""
    assert context.browser.current_url == "http://localhost:8000/absence-request", (
        f"Expected url to be on absence request form page, "
        f"instead is on {context.browser.current_url}"
    )
    context.browser.quit()


@then("the form should be submitted")
def step_impl(context):
    """Checks if the test env is on the confirmation page"""
    assert context.browser.current_url == "http://localhost:8000/confirm", (
        f"Expected url to be on absence request form page, "
        f"instead is on {context.browser.current_url}"
    )
    context.browser.quit()


@then("the form should not be submitted")
def step_impl(context):
    """Checks if the test env is still on the absence request page"""
    assert context.browser.current_url == "http://localhost:8000/absence_request", (
        f"Expected url to be on absence request form page, "
        f"instead is on {context.browser.current_url}"
    )
    context.browser.quit()


@given("a user has filled out the absence request form")
def step_user_filled_out_form(context):
    context.form_data = {
        "first_day_absent": "2024-02-14",
        "last_day_absent": "2024-02-15",
        "shift": "1",
        "hours": "8",
        "absence_type": "sick",
        "email": "test@example.com",
    }


@when("they submit the form")
def step_user_submits_form(context):
    context.response = context.test.client.post(
        "/submit_absence_request/", context.form_data
    )


@then("an email should be sent to the user with the pending status")
def step_email_is_sent(context):
    assert len(mail.outbox) == 1
    assert mail.outbox[0].subject == "Absence Request Submission"
    assert "pending" in mail.outbox[0].body
    assert mail.outbox[0].to == [context.form_data["email"]]

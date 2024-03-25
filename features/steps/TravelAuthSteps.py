from behave import given, then, when
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

@given("the user clicks on the travel authorization button")
def step_impl(context):
    travel_authorization_button = context.browser.find_element(By.ID, "travel_auth")
    travel_authorization_button.click()


@given("the user enters {clock_number} as their clock number")
def step_impl(context, clock_number):
    clock_number_input = context.browser.find_element(By.ID, "id_clock_number")
    clock_number_input.send_keys(clock_number)


@given("the user enters {name} as their name")
def step_impl(context, name):
    name_input = context.browser.find_element(By.ID, "id_name")
    name_input.send_keys(name)


@given("the user selects {department} from the dropdown menu")
def step_impl(context, department):
    dropdown = Select(context.browser.find_element(By.ID, "id_department"))
    dropdown.select_by_visible_text(department)


@given("the user enters {destination} as their destination")
def step_impl(context, destination):
    destination_input = context.browser.find_element(By.ID, "id_destination")
    destination_input.send_keys(destination)


@given("the users enters {departure_date} as their departure date")
def step_impl(context, departure_date):
    date_input = context.browser.find_element(By.ID, "id_departure_date")
    date_input.send_keys(departure_date)


@given("the user enters {return_date} as their return date")
def step_impl(context, return_date):
    date_input = context.browser.find_element(By.ID, "id_return_date")
    date_input.send_keys(return_date)


@given("the user selects {travel_type} as their mode of transportation")
def step_impl(context, travel_type):
    check = context.browser.find_element(By.ID, f'id_{travel_type}')
    check.click()


@given("the user enters {nights} as their amount of nights of lodging")
def step_impl(context, nights):
    nights_input = context.browser.find_element(By.ID, "id_nights_lodging")
    nights_input.send_keys(nights)


@given("the user enters {manager} as their manager")
def step_impl(context, manager):
    dropdown = Select(context.browser.find_element(By.ID, "id_department_manager"))
    dropdown.select_by_visible_text(manager)


@given("the user enters {email} as their email")
def step_impl(context, email):
    email_input = context.browser.find_element(By.ID, "id_email")
    email_input.send_keys(email)


@given("the user enters {signature} as their signature")
def step_impl(context, signature):
    signature_input = context.browser.find_element(By.ID, "id_signature")
    signature_input.send_keys(signature)

@given("the users enters {departure_date} as their departure date on firefox")
def step_impl(context, departure_date):
    date_input = context.browser.find_element(By.ID, "id_departure_date")
    date_input.send_keys(departure_date)

@step("the user enters {return_date} as their return date on firefox")
def step_impl(context, return_date):
    date_input = context.browser.find_element(By.ID, "id_return_date")
    date_input.send_keys(return_date)

@then("the user should be on the travel authorization form")
def step_impl(context):
    assert  context.browser.current_url == 'http://localhost:8000/travel-auth', (
        f"Expected url to be on travel auth page, "
        f"instead is on {context.browser.current_url}"
    )
    context.browser.quit()



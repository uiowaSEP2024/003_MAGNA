from behave import given, then, when
from selenium import webdriver
from selenium.webdriver.common.by import By
from django.core import mail

@given("a kiosk user is logged in")
def step_impl(context):
    context.browser.get("http://localhost:8000/")
    username_input = context.browser.find_element(By.ID, "id_username")
    password_input = context.browser.find_element(By.ID, "id_password")
    username_input.send_keys("kiosk1")
    password_input.send_keys("kioskpass1")
    login_button = context.browser.find_element(By.ID, "log-in")
    login_button.click()

@given("the user is on the login page")
def step_impl(context):
    context.browser.get("http://localhost:8000/")

@when("the user clicks on the absence request button")
def step_impl(context):
    """Clicks on the absence request link"""
    absence_request_button = context.browser.find_element(By.ID, "absence_request")
    absence_request_button.click()

@when("the user clicks on the travel authorization button")
def step_impl(context):
    travel_authorization_button = context.browser.find_element(By.ID, "travel_auth")
    travel_authorization_button.click()

# then steps

@then("the user is redirected to the absence request form")
def step_impl(context):
    """Checks if the test env is on the absence request form"""
    assert context.browser.current_url == "http://localhost:8000/absence-request", (
        f"Expected url to be on absence request form page, "
        f"instead is on {context.browser.current_url}"
    )
    context.browser.quit()


@then("the user is redirected to the travel authorization form")
def step_impl(context):
    assert  context.browser.current_url == 'http://localhost:8000/travel-auth', (
        f"Expected url to be on travel auth page, "
        f"instead is on {context.browser.current_url}"
    )
    context.browser.quit()
# steps.py
from behave import given, then, when
from selenium import webdriver
from selenium.webdriver.common.by import By


@given("the user has navigated to the login page")
def step_impl(context):
    """FILL IN"""
    # context.browser.visit(context.get_url("login"))
    context.browser = webdriver.Chrome()
    context.browser.get("http://localhost:8000/")


@given("the user has navigated to the home page")
def step_impl(context):
    context.browser = webdriver.Chrome()
    context.browser.get("http://localhost:8000/home")


@when("the user submits the login form with valid credentials")
def step_impl(context):
    """FILL IN"""
    # context.browser.fill("username", "user")
    username_input = context.browser.find_element(By.ID, "username")
    username_input.send_keys("user")
    # context.browser.fill("password", "pass")
    password_input = context.browser.find_element(By.ID, "password")
    password_input.send_keys("pass")
    login_button = context.browser.find_element(By.ID, "log-in")
    login_button.click()


@when("the user submits the login form with incorrect credentials")
def step_impl(context):
    username_input = context.browser.find_element(By.ID, "username")
    username_input.send_keys("user_wrong")
    password_input = context.browser.find_element(By.ID, "password")
    password_input.send_keys("pass_wrong")
    login_button = context.browser.find_element(By.ID, "log-in")
    login_button.click()


@when("the user clicks on the PTO button")
def step_impl(context):
    pto_button = context.browser.find_element(By.ID, "pto-link")
    pto_button.click()


@then("the user should not be redirected to the home page")
def step_impl(context):
    assert context.browser.current_url != "http://localhost:8000/home", (
        f"Expected url to be on login page, "
        f"instead is on {context.browser.current_url}"
    )


@then("the user should be redirected to the home page")
def step_impl(context):
    """FILL IN"""
    assert context.browser.current_url == "http://localhost:8000/home", (
        f"Expected url to be on home page, "
        f"instead is on {context.browser.current_url}"
    )


@then("the user is redirected to the PTO form")
def step_impl(context):
    assert context.browser.current_url == "http://localhost:8000/pto", (
        f"Expected url to be on pto form page, "
        f"instead is on {context.browser.current_url}"
    )

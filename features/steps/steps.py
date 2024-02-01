# steps.py
from behave import given, when, then

@given('the user has navigated to the login page')
def step_impl(context):
    context.browser.visit(context.get_url('login'))

@when('the user submits the login form with valid credentials')
def step_impl(context):
    context.browser.fill('username', 'user')
    context.browser.fill('password', 'pass')
    context.browser.find_by_value('Log In').first.click()

@then('the user should be redirected to the home page')
def step_impl(context):
    assert context.browser.url == context.get_url('home')

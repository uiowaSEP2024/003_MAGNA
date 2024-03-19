from behave import given, then, when
from selenium import webdriver
from selenium.webdriver.common.by import By
from django.core import mail


# Steps for logging in the different types of users, specifically on the login page.
# Note: All of these steps assume a browser has been set up. These steps also assume the user
# is on the login page. These were made for testing the login page originally.

# test for if the user is not logged in
@given("the user is not logged in")
def step_impl(context):
    context.browser.get("http://localhost:8000/")


@given("the user tries to navigate to the home page")
def step_impl(context):
    context.browser.get("http://localhost:8000/home")


# new given variants for scenario outline
@given("the user enters {username} as the username")
def step_impl(context, username):
    username_input = context.browser.find_element(By.ID, "id_username")
    username_input.send_keys(username)


@given("the user enters {password} as the password")
def step_impl(context, password):
    password_input = context.browser.find_element(By.ID, "id_password")
    password_input.send_keys(password)


@when("the user presses the login button")
def step_impl(context):
    login_button = context.browser.find_element(By.ID, "log-in")
    login_button.click()

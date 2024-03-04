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


# login feature when steps are here

# Kiosk user
@when("the kiosk user correctly enters the username")
def step_impl(context):
    username_input = context.browser.find_element(By.ID, "id_username")
    username_input.send_keys("kiosk1")


@when("the kiosk user correctly enters the password")
def step_impl(context):
    password_input = context.browser.find_element(By.ID, "id_password")
    password_input.send_keys("kioskpass1")


# Incorrect variants
@when("the kiosk user incorrectly enters the username")
def step_impl(context):
    username_input = context.browser.find_element(By.ID, "id_username")
    username_input.send_keys("kiosk")


@when("the kiosk user incorrectly enters the password")
def step_impl(context):
    password_input = context.browser.find_element(By.ID, "id_password")
    password_input.send_keys("kioskpass")


# Floor employee user

# correct variants
@when("the floor employee user correctly enters the username")
def step_impl(context):
    username_input = context.browser.find_element(By.ID, "id_username")
    username_input.send_keys("floor1")


@when("the floor employee user correctly enters the password")
def step_impl(context):
    password_input = context.browser.find_element(By.ID, "id_password")
    password_input.send_keys("floorpass1")

    # incorrect variants


@when("the floor employee user incorrectly enters the username")
def step_impl(context):
    username_input = context.browser.find_element(By.ID, "id_username")
    username_input.send_keys("floor")


@when("the floor employee user incorrectly enters the password")
def step_impl(context):
    password_input = context.browser.find_element(By.ID, "id_password")
    password_input.send_keys("floorpass")


# Manager user

# correct variants
@when("the manager user correctly enters the username")
def step_impl(context):
    username_input = context.browser.find_element(By.ID, "id_username")
    username_input.send_keys("manager1")


@when("the manager user correctly enters the password")
def step_impl(context):
    password_input = context.browser.find_element(By.ID, "id_password")
    password_input.send_keys("managerpass1")

    # incorrect variants


@when("the manager user incorrectly enters the username")
def step_impl(context):
    username_input = context.browser.find_element(By.ID, "id_username")
    username_input.send_keys("manager")


@when("the manager user incorrectly enters the password")
def step_impl(context):
    password_input = context.browser.find_element(By.ID, "id_password")
    password_input.send_keys("managerpass")


# HR Variants

# correct variants
@when("the HR user correctly enters the username")
def step_impl(context):
    username_input = context.browser.find_element(By.ID, "id_username")
    username_input.send_keys("hr1")


@when("the HR user correctly enters the password")
def step_impl(context):
    password_input = context.browser.find_element(By.ID, "id_password")
    password_input.send_keys("hrpass1")

    # incorrect variants


@when("the HR user incorrectly enters the username")
def step_impl(context):
    username_input = context.browser.find_element(By.ID, "id_username")
    username_input.send_keys("hr")


@when("the HR user incorrectly enters the password")
def step_impl(context):
    password_input = context.browser.find_element(By.ID, "id_password")
    password_input.send_keys("hrpass")


# admin variants

# correct variants

@when("the admin user correctly enters the username")
def step_impl(context):
    username_input = context.browser.find_element(By.ID, "id_username")
    username_input.send_keys("admin")


@when("the admin user correctly enters the password")
def step_impl(context):
    password_input = context.browser.find_element(By.ID, "id_password")
    password_input.send_keys("adminpass123")

    # incorrect variants


@when("the admin user incorrectly enters the username")
def step_impl(context):
    username_input = context.browser.find_element(By.ID, "id_username")
    username_input.send_keys("admin1")


@when("the admin user incorrectly enters the password")
def step_impl(context):
    password_input = context.browser.find_element(By.ID, "id_password")
    password_input.send_keys("adminpass1")


@when("the user presses the login button")
def step_impl(context):
    login_button = context.browser.find_element(By.ID, "log-in")
    login_button.click()

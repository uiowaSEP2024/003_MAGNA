from behave import given, then, when
from selenium import webdriver
from selenium.webdriver.common.by import By
from django.core import mail
# Do we need the mail statements

#Tests for different browsers

@given("The user is using chrome")
def step_impl(context):
    context.browser = webdriver.Chrome()


@given("The user is using edge")
def step_impl(context):
    context.browser = webdriver.Edge()


@given("The user is using firefox")
def step_impl(context):
    context.browser = webdriver.Firefox()


@given("The user is using internet explorer")
def step_impl(context):
    context.browser = webdriver.Ie()
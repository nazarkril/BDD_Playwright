import os

from behave import given, when, then
from playwright.sync_api import sync_playwright

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

from pages.main_page import MainPage
from tool import take_screenshot


@given("the user is on the SauceDemo login page")
def step_go_to_side(context):
    context.login_page = LoginPage(context.page)
    context.login_page.go_to(os.getenv("SITE"))
    
@when("user1 enter valid credentials")
def step_pass_credential_user1(context):
    context.login_page.login(os.getenv("USER"), os.getenv("PASSWORD"))
    take_screenshot("after_login")

@when("user2 enter valid credentials")
def step_pass_credential_user2(context):
    context.login_page.login(os.getenv("USER2"), os.getenv("PASSWORD"))
    take_screenshot("after_login")

@when("user3 enter valid credentials")
def step_pass_credential_user3(context):
    """ locked_out_user"""
    context.login_page.login(os.getenv("USER3"), os.getenv("PASSWORD"))
    take_screenshot("after_login")

@when("User open menu")
def step_open_menu(context):
    context.page.get_by_role("button", name="Open Menu").click()

@when("user log out")
def step_logout(context):
    step_open_menu(context)
    context.page.locator('[data-test="logout-sidebar-link"]').click()
    take_screenshot("after_logout")
    
@then("they should be redirected to the inventory page")
def step_check_inventory_page(context):
    context.inventory_page = InventoryPage(context.page)
    assert "inventory" in context.page.url
    take_screenshot("inventory_page")

@then('the error message is "{error_message}"')
def step_check_error_message(context, error_message):
    error_message_locator = context.page.locator('[data-test="error"]')
    assert error_message_locator.text_content() == error_message
    take_screenshot("error_message.png")



    
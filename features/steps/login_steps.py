from behave import given, when, then
from playwright.sync_api import sync_playwright

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@given("the user is on the SauceDemo login page")
def step_impl(context):
    playwright = sync_playwright().start()
    context.browser = playwright.chromium.launch(headless=False)
    context.page = context.browser.new_page()
    context.login_page = LoginPage(context.page)
    context.login_page.go_to("https://saucedemo.com/")
    context.login_page.take_screenshot("login_page")

@when("they enter valid credentials")
def step_impl(context):
    context.login_page.login("standard_user", "secret_sauce")
    context.login_page.take_screenshot("after_login")

@then("they should be redirected to the inventory page")
def step_impl(context):
    context.inventory_page = InventoryPage(context.page)
    assert "inventory" in context.page.url
    context.inventory_page.take_screenshot("inventory_page")
    context.browser.close()

import os
import time
from behave import given, when, then
import playwright
from playwright.sync_api import expect
from pages.main_page import MainPage, SortingOptions, add_good, remove_good, select_sorting_option
from tool import normalized_name, take_screenshot
from playwright.sync_api import sync_playwright


@given("the user is logged in")
def step_login(context):
    context.login_page = MainPage(context.page)
    context.login_page.go_to(os.getenv("SITE"))
    context.login_page.login(os.getenv("USER"), os.getenv("PASSWORD"))
    take_screenshot("login_page")

@when('the user click "Add to cart" on "{goods}"')
def step_add_goods_to_cart(context, goods):
    goods_list = goods.split(',') 
    for good in goods_list:
        added_good_obj = add_good(context=context, good=good)
        if added_good_obj.text_content() == "Add to cart":
            raise ValueError(f"Button text did not change to 'Remove' for {good}")
        take_screenshot(f"add_{normalized_name(good)}.png") 

@when('the user click "Remove" on "{goods}" from main page')
def step_remove_goods_from_cart(context, goods):
    """this step removes goods from main page, not from cart page"""
    for good in goods.split(','):
        removed_good_obj = remove_good(context=context, good=good)
        if  removed_good_obj.text_content() == "Remove":
            raise ValueError(f"Button text did not change to 'Add to cart' for {good}")
        take_screenshot(f"remove_{normalized_name(good)}.png")

@when('the user sorts goods by "{option_text}"')
def step_sorting_by(context, option_text):
    """this step sorts goods by option_text""" 
    nomalized_name = SortingOptions.get_constant_name(option_text)
    take_screenshot(f"before_sort_by_{nomalized_name}.png")
    select_sorting_option(context, option_text)
    take_screenshot(f"after_sort_by_{nomalized_name}.png")    

@then('the goods is sorted by "{option_text}"')
def step_check_product_sort_container(context, option_text):
    nomalized_name = SortingOptions.get_constant_name(option_text)
    product_sort_container = context.page.locator('[data-test="product-sort-container"] option:checked')
    expect(product_sort_container).to_have_text(f"{option_text}")
    take_screenshot(f"product_sort_container_by_{nomalized_name}.png")    

@then('the name of the first item is "{first_item}"')
def step_check_first_item_name(context, first_item):
    first_item_locator = context.page.locator('[data-test="inventory-item-name"]').first
    expect(first_item_locator).to_have_text(f"{first_item}")
    take_screenshot(f"check_first_item_name_{normalized_name(first_item)}.png")    

@then('the price of the first item is "{price_first_item}"')
def step_check_first_item_price(context, price_first_item):
    first_item_price = context.page.locator('[data-test="inventory-item-price"]').first
    expect(first_item_price).to_have_text(f"{price_first_item}")
    take_screenshot(f"check_first_item_price_{price_first_item.replace('.', '_')}.png")    

# the basket contains "<number>" item
@then('the basket contains "{number}" item')
def step_check_basket_count(context, number):
    context.page.evaluate("window.scrollTo(0, 0)")
    shopping_badge = context.page.locator(".shopping_cart_badge")
    if number == "0":

        expect(shopping_badge).not_to_be_visible()
    else:
        numbere_of_chosen_goods = shopping_badge.text_content()
        expect(shopping_badge).to_have_text(f"{number}")
    take_screenshot(f"basket_contains_{number}_item.png")

@then('the "{goods}" changed status to "{new_status}"')
def step_check_good_status(context, goods, new_status):
    for good in goods.split(','):
        product_locator = context.page.locator(f"text={good}")
        good_status = product_locator.locator("xpath=../../..//button")
        expect(good_status).to_have_text(new_status)



from behave import given, when, then
from playwright.sync_api import expect
from pages.main_page import remove_good
from tool import normalized_name, take_screenshot


@when('the user click on Shopping cart icon')
def step_go_to_shopping_cart(context):
    context.page.locator("#shopping_cart_container").click()
    take_screenshot("go_to_shopping_cart.png")
   
@when('the user click "Remove" on "{goods}" from shopping cart page')
def step_remove_goods_from_cart(context, goods):
    """this step removes goods from shopping cart page, not from main page"""
    for good in goods.split(','):
        remove_good_from_cart(context=context, good=good)
        
        locator = context.page.locator('[data-test="inventory-item-name"]', has_text=good)
        if locator.count() > 0:
            raise ValueError(f"The {good} is present after removing from cart")
        take_screenshot(f"remove_{normalized_name(good)}.png")
   
@when('the user click "Continue Shopping" from shopping cart page')
def step_remove_goods_from_cart(context):
    context.page.locator('[data-test="continue-shopping"]').click()
    take_screenshot("continue_shopping.png")

@then('the basket contains "{number}" item on shopping cart page')
def step_check_basket_number(context, number):
    cart_badge = context.page.locator(".shopping_cart_badge")
    expect(cart_badge).to_have_text(f"{number}")
    take_screenshot(f"basket_contains_{number}_item.png")
    
@then('the "{goods}" are present in the shopping cart')
def step_check_goods_in_cart(context, goods):
    for good in goods.split(','):
        good_card_locator = context.page.locator('.cart_item [data-test="inventory-item-name"]', has_text="Sauce Labs Bolt T-Shirt")
        expect(good_card_locator).to_be_visible()
        take_screenshot(f"check_{normalized_name(good)}_in_cart.png")

@then('the "{removed_goods}" is removed from the shopping cart')
def step_check_goods_not_in_cart(context, removed_goods):
    for good in removed_goods.split(','):
        product_locator = context.page.locator(f"text={good}")
        expect(product_locator).not_to_be_visible()
        take_screenshot(f"check_{normalized_name(good)}_not_in_cart.png")

@then('the "{viewed_goods}" is added in the shopping cart')
def step_check_goods_in_cart(context, viewed_goods):
    for good in viewed_goods.split(','):
        product_locator = context.page.locator(f"text={good}")
        expect(product_locator).to_be_visible()
        take_screenshot(f"check_{normalized_name(good)}_in_cart.png")

def remove_good_from_cart(context, good):
    cart_item = context.page.locator('.cart_item', has_text=good)
    remove_button = cart_item.locator('button', has_text="Remove")
    remove_button.click()
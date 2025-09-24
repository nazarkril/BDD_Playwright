import time
from pages.login_page import LoginPage


class MainPage(LoginPage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.product_sort_container = page.locator(".product_sort_container")
        self.inventory_items = page.locator(".inventory_item")
        self.cart_icon = page.locator("#shopping_cart_container")

# def click_sorting_dropdown(context):
#     product_sort_container = context.page.locator(".product_sort_container")
#     product_sort_container.click()

# def get_sorting_dropdown(context):
#     product_sort_container = context.page.locator(".product_sort_container")
#     context.product_sort_container.text_content()
#     context.page.locator(".product_sort_container").text_content()

def select_sorting_option(context, option_text):
    context.page.locator('[data-test="product-sort-container"]').select_option(SortingOptions.get_constant_name(option_text))
    
def add_good(context, good):
    product_locator = context.page.locator(f"text={good}")
    add_button = product_locator.locator("xpath=../../..//button")
    add_button.click()
    time.sleep(1)  # wait for the button text to update
    return add_button

def remove_good(context, good):
    product_locator = context.page.locator(f"text={good}")
    remove_button = product_locator.locator("xpath=../../..//button")
    remove_button.click()
    time.sleep(1)  # wait for the button text to update
    return remove_button

class SortingOptions:
    az = "Name (A to Z)"
    za = "Name (Z to A)"
    lohi = "Price (low to high)"
    hilo = "Price (high to low)"


# class SortingOptions:
#     A_TO_Z = "Name (A to Z)"
#     Z_TO_A = "Name (Z to A)"
#     PRICE_LOW_TO_HIGH = "Price (low to high)"
#     PRICE_HIGH_TO_LOW = "Price (high to low)"


    # Reverse mapping: value to constant name
    VALUE_TO_NAME = {
        az: "az",
        za: "za",
        lohi: "lohi",
        hilo: "hilo",
    }

    @classmethod
    def get_constant_name(cls, value):
        return cls.VALUE_TO_NAME.get(value)
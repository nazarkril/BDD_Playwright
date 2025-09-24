from pages.base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.add_to_cart_button = page.locator("button[id^='add-to-cart']")
        self.cart_icon = page.locator("#shopping_cart_container")

    def add_first_item_to_cart(self):
        self.add_to_cart_button.click()

    def go_to_cart(self):
        self.cart_icon.click()

    def remove_first_item_from_cart(self):
        """ToDO: implement removing specific item"""
        remove_button = self.page.locator("button[id^='remove-']")
        remove_button.click()


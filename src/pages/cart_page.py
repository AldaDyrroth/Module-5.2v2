from src.pages.base_page import BasePage
from constant import Selectors, Endpoints, ExpectedData

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = Endpoints.CART.value

    def remove_item_from_cart(self):
        self.wait_for_selector_click(Selectors.CART_REMOVE_SELECTOR.value)

    def continue_shopping(self):
        self.wait_for_selector_click(Selectors.CART_RETURN_SELECTOR.value)
        self.assert_text_present_on_page(ExpectedData.INVENTORY_PAGE.value)

    def go_to_checkout_cart(self):
        self.wait_for_selector_click(Selectors.CART_CHECKOUT_SELECTOR.value)
        self.assert_text_present_on_page(ExpectedData.CHECKOUT_FIRST_PAGE.value)

    def check_count(self, count):
        self.assert_count_of_elements(Selectors.CART_ITEM_SELECTOR.value, count)
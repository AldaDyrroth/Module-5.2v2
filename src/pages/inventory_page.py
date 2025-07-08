from src.pages.base_page import BasePage
from constant import Selectors, Endpoints, ExpectedData, Par

class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = Endpoints.INVENTORY.value


    def add_item_to_cart(self):
        self.wait_for_selector_click(Selectors.INVENTORY_GOOD_SELECTOR.value)
        self.assert_element_is_visible(Selectors.INVENTORY_RED_MARK_SELECTOR.value)


    def remove_item_from_cart(self):
        self.wait_for_selector_click(Selectors.INVENTORY_REMOVE_SELECTOR.value)
        self.assert_element_is_not_visible(Selectors.INVENTORY_RED_MARK_SELECTOR.value)


    def sort_items_by_price_growing(self):
        self.wait_for_selector_click(Selectors.INVENTORY_SORTING_SELECTOR.value)
        self.wait_for_selector_click(Selectors.INVENTORY_SORT_PARAM_PRICE_SELECTOR.value)
        self.assert_text_in_first_element(Selectors.INVENTORY_GOOD_SELECTOR, Par.MIN_PRICE.value)
        self.assert_text_in_last_element(Selectors.INVENTORY_GOOD_SELECTOR, Par.MAX_PRICE.value)

        self.wait_for_selector_click(Selectors.INVENTORY_RED_MARK_SELECTOR.value)
        self.assert_text_present_on_page(ExpectedData.CART_PAGE.value)

    def sort_items_by_title_z_to_a(self):
        self.wait_for_selector_click(Selectors.INVENTORY_SORTING_SELECTOR.value)
        self.wait_for_selector_click(Selectors.INVENTORY_SORT_PARAM_NAME_SELECTOR.value)
        self.assert_text_in_first_element(Selectors.INVENTORY_GOOD_SELECTOR.value, Par.FIRST_TITLE.value)
        self.assert_text_in_last_element(Selectors.INVENTORY_GOOD_SELECTOR.value, Par.LAST_TITLE.value)

    def go_to_cart_page(self):
        self.wait_for_selector_click(Selectors.INVENTORY_RED_MARK_SELECTOR.value)
        self.assert_text_present_on_page(ExpectedData.CART_PAGE.value)
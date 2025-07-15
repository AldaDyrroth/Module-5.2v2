from src.pages.base_page import BasePage
from src.enums.web_metadata import Selectors, Endpoints, ExpectedData

class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = Endpoints.CHECKOUT.value


    def first_checkout_step(self, data):


        self.wait_for_selector_fill(Selectors.CHECKOUT_FIRSTNAME_SELECTOR.value, data[0])
        self.wait_for_selector_fill(Selectors.CHECKOUT_LASTNAME_SELECTOR.value, data[1])
        self.wait_for_selector_fill(Selectors.CHECKOUT_POSTAL_CODE_SELECTOR.value, data[2])
        self.assert_input_value(Selectors.CHECKOUT_POSTAL_CODE_SELECTOR.value, data[2])

        self.wait_for_selector_click(Selectors.CHECKOUT_CONTINUE_SELECTOR.value)
        self.assert_text_present_on_page(ExpectedData.CHECKOUT_SECOND_PAGE.value)
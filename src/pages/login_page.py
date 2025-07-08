from src.pages.base_page import BasePage
from constant import Selectors, Endpoints, ExpectedData

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = Endpoints.LOGIN.value



    def authorization(self, username, password):
        self.navigate_to()
        data = {
            Selectors.LOGIN_USERNAME_SELECTOR.value: username,
            Selectors.LOGIN_PASSWORD_SELECTOR.value: password
        }
        self.wait_for_selector_fill_anymore(data)
        self.wait_for_selector_click_anymore([Selectors.LOGIN_LOGIN_BUTTTON_SELECTOR.value])
        self.assert_text_present_on_page(ExpectedData.INVENTORY_PAGE.value)
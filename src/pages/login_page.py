from src.pages.base_page import BasePage, AsyncBasePage
from src.enums.web_metadata import WebData
from src.enums.page_selectors import Selectors
from src.enums.page_flag import ExpectedData
from src.enums.endpoints import Endpoints

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



class AsyncLoginPage(AsyncBasePage):
    def __init__(self, page):
        super().__init__(page)
        self._endpoint = Endpoints.LOGIN.value


    async def async_authorization(self, username, password):
        await self.navigate_to()
        data = {
            Selectors.LOGIN_USERNAME_SELECTOR.value: username,
            Selectors.LOGIN_PASSWORD_SELECTOR.value: password
        }
        await self.wait_for_selector_fill_anymore(data)
        await self.wait_for_selector_click_anymore([Selectors.LOGIN_LOGIN_BUTTTON_SELECTOR.value])
        await self.assert_text_present_on_page(ExpectedData.INVENTORY_PAGE.value)
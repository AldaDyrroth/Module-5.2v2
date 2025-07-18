from playwright.sync_api import expect
from src.enums.endpoints import Endpoints

class BasePage:
    __BASE_URL = Endpoints.BASE_URL.value


    def __init__(self, page):
        self.page = page
        self._endpoint = ''

    def _get_full_url(self):
        return f'{self.__BASE_URL}/{self._endpoint}'

    def navigate_to(self):
        full_url = self._get_full_url()
        self.page.goto(full_url)
        self.page.wait_for_load_state('load')
        expect(self.page).to_have_url(full_url)

    def wait_for_selector_click(self, selector):
        self.page.wait_for_selector(selector)
        self.page.click(selector)

    def wait_for_selector_click_anymore(self, forms):
        for selector in range(len(forms)):
            self.page.wait_for_selector(forms[selector])
            self.page.click(forms[selector])

    def wait_for_selector_fill(self, selector, text):
        self.page.wait_for_selector(selector)
        self.page.fill(selector, text)

    def wait_for_selector_fill_anymore(self, forms):
        for selector, text in forms.items():
            self.page.wait_for_selector(selector)
            self.page.fill(selector, text)

    def wait_for_selector_type(self, selector, text, delay):
        self.page.wait_for_selector(selector)
        self.page.type(selector, text, delay=delay)

    def assert_element_is_visible(self, selector):
        expect(self.page.locator(selector)).to_be_visible()

    def assert_element_is_not_visible(self, selector):
        expect(self.page.locator(selector)).not_to_be_visible()

    def assert_text_present_on_page(self, title):
        expect(self.page.locator("body")).to_contain_text(title)

    def assert_text_in_element(self, selector, text):
        expect(self.page.locator(selector)).to_have_text(text)

    def assert_text_in_first_element(self, selector, text):
        expect(self.page.locator(selector).first).to_have_text(text)

    def assert_text_in_last_element(self, selector, text):
        expect(self.page.locator(selector).last).to_have_text(text)

    def assert_input_value(self, selector, expected_value):
        expect(self.page.locator(selector)).to_have_value(expected_value)

    def assert_count_of_elements(self, selector, count):
        expect(self.page.locator(selector)).to_have_count(count)

class AsyncBasePage:
    __BASE_URL = Endpoints.BASE_URL.value


    def __init__(self, page):
        self.page = page
        self._endpoint = ''

    async def _get_full_url(self):
        return f'{self.__BASE_URL}/{self._endpoint}'

    async def navigate_to(self):
        full_url = self._get_full_url()
        await self.page.goto(full_url)
        await self.page.wait_for_load_state('load')
        expect(self.page).to_have_url(full_url)

    async def wait_for_selector_click(self, selector):
        self.page.wait_for_selector(selector)
        self.page.click(selector)

    async def wait_for_selector_click_anymore(self, forms):
        for selector in range(len(forms)):
            self.page.wait_for_selector(forms[selector])
            self.page.click(forms[selector])

    async def wait_for_selector_fill(self, selector, text):
        self.page.wait_for_selector(selector)
        self.page.fill(selector, text)

    async def wait_for_selector_fill_anymore(self, forms):
        for selector, text in forms.items():
            self.page.wait_for_selector(selector)
            self.page.fill(selector, text)

    async def wait_for_selector_type(self, selector, text, delay):
        self.page.wait_for_selector(selector)
        self.page.type(selector, text, delay=delay)

    async def assert_element_is_visible(self, selector):
        await expect(self.page.locator(selector)).to_be_visible()

    async def assert_element_is_not_visible(self, selector):
        await expect(self.page.locator(selector)).not_to_be_visible()

    async def assert_text_present_on_page(self, title):
        await expect(self.page.locator("body")).to_contain_text(title)

    async def assert_text_in_element(self, selector, text):
        await expect(self.page.locator(selector)).to_have_text(text)

    async def assert_text_in_first_element(self, selector, text):
        await expect(self.page.locator(selector).first).to_have_text(text)

    async def assert_text_in_last_element(self, selector, text):
        await expect(self.page.locator(selector).last).to_have_text(text)

    async def assert_input_value(self, selector, expected_value):
        await expect(self.page.locator(selector)).to_have_value(expected_value)

    async def assert_count_of_elements(self, selector, count):
        await expect(self.page.locator(selector)).to_have_count(count)


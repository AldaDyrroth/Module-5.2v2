from playwright.async_api import async_playwright
import asyncio
from playwright.sync_api import sync_playwright
import time
from faker import Faker
faker = Faker()
import pytest

@pytest.fixture(scope="session")
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    yield browser
    time.sleep(3)

    browser.close()

    playwright.stop()

@pytest.fixture(scope="session")
async def async_browser():
    async with async_playwright() as a:
        browser = await a.chromium.launch(headless=False, slow_mo=1000)
        yield browser
        time.sleep(3)
        await browser.close()



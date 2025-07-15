from dotenv import load_dotenv
import os
import sys
import pytest

from src.pages.inventory_page import InventoryPage
from src.pages.cart_page import CartPage
from src.pages.checkout_page import CheckoutPage
from src.pages.login_page import LoginPage, AsyncLoginPage
from src.scenarios.souce_scenarios import PositiveScenarios, AsyncPositiveScenarios

load_dotenv()
sys.path.insert(1, os.path.join(sys.path[0], '..'))

@pytest.fixture(scope="session")
def scenarios_souce(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    return PositiveScenarios(inventory_page, cart_page, checkout_page, login_page)

@pytest.fixture(scope="session")
def async_scenarios_souce(browser):
    page = browser.new_page()
    login_page = AsyncLoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    return AsyncPositiveScenarios(inventory_page, cart_page, checkout_page, login_page)

class TestSouce():

    def test_auth_2_0(self, scenarios_souce):
        scenarios_souce.login_on_site(os.getenv("USER_NAME"), os.getenv("USER_PASS"))

    def test_adding(self, scenarios_souce):
        scenarios_souce.add_goods_to_cart(6)

    async def test_async_auth_2_0(self, async_scenarios_souce):
        await async_scenarios_souce.login_on_site(os.getenv("USER_NAME"), os.getenv("USER_PASS"))



        pass


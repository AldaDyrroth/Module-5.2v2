from src.pages.inventory_page import InventoryPage
from src.pages.cart_page import CartPage
from src.pages.checkout_page import CheckoutPage
from src.pages.login_page import LoginPage
from constant import Par
import pytest

@pytest.fixture
def page(browser):
    return browser.new_page()

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def inventory_page(page):
    return InventoryPage(page)

@pytest.fixture
def cart_page(page):
    return CartPage(page)

@pytest.fixture
def checkout_page(page):
    return CheckoutPage(page)

class TestSouce:

    def test_add_items(self, login_page):

        login_page.authorization(Par.USER_NAME.value, Par.USER_PASS.value)
        #
        # inventory_page.add_item_to_cart()
        # inventory_page.remove_item_from_cart()
        # #inventory_page.sort_items_by_price_growing()
        # #inventory_page.sort_items_by_title_z_to_a()
        # inventory_page.add_item_to_cart()
        # inventory_page.add_item_to_cart()
        # inventory_page.go_to_cart_page()
        #
        # cart_page.remove_item_from_cart()
        # cart_page.go_to_checkout_cart()
        # # cart_page.continue_shopping()
        #
        # checkout_page.first_checkout_step(userdata)
        pass


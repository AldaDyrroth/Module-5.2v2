from enum import Enum

class Par(Enum):
    BASE_URL = "https://www.saucedemo.com"
    USER_NAME = "standard_user"
    USER_PASS = "secret_sauce"
    MIN_PRICE = '7.99'
    MAX_PRICE = '49.99'
    FIRST_TITLE = 'Test.allTheThings() T-Shirt (Red)'
    LAST_TITLE = 'Sauce Labs Backpack'


class Selectors(Enum):

    # CartPage
    CART_REMOVE_SELECTOR = ".cart_item >> text='Remove'"
    CART_RETURN_SELECTOR = ".cart_footer >> text='Continue Shopping'"
    CART_CHECKOUT_SELECTOR = "#checkout"

    # CheckoutPage
    CHECKOUT_FIRSTNAME_SELECTOR = '#first-name'
    CHECKOUT_LASTNAME_SELECTOR = '#last-name'
    CHECKOUT_POSTAL_CODE_SELECTOR = '#postal-code'
    CHECKOUT_CONTINUE_SELECTOR = '#continue'
    CHECKOUT_CANCEL_SELECTOR = '#cancel'

    # InventoryPage
    INVENTORY_GOOD_SELECTOR = ".inventory_item >> text='Add to cart'"
    INVENTORY_GOOD_2_SELECTOR = ".inventory_item >> text='Sauce Labs Bolt T-Shirt'"
    INVENTORY_RED_MARK_SELECTOR = '.shopping_cart_badge'
    INVENTORY_REMOVE_SELECTOR = ".inventory_item >> text='Remove'"
    INVENTORY_SORTING_SELECTOR = ".product_sort_container"
    INVENTORY_SORT_PARAM_PRICE_SELECTOR = ".product_sort_container >> text='Price (low to high)'"
    INVENTORY_SORT_PARAM_NAME_SELECTOR = ".product_sort_container >> text='Price (low to high)'"

    # LoginPage
    LOGIN_USERNAME_SELECTOR = '#user-name'
    LOGIN_PASSWORD_SELECTOR = '#password'
    LOGIN_LOGIN_BUTTTON_SELECTOR = '#login-button'


class Endpoints(Enum):
    CART = 'cart.html'
    CHECKOUT = 'checkout-step-one.html'
    INVENTORY = 'inventory.html'
    LOGIN = ''

class ExpectedData(Enum):
    LOGIN_PAGE = 'Login'
    INVENTORY_PAGE = 'Products'
    CART_PAGE = 'Your Cart'
    CHECKOUT_SECOND_PAGE = 'Checkout: Overview'
    CHECKOUT_FIRST_PAGE = 'Checkout: Your Information'
    COMPLETE_PAGE = 'Checkout: Complete!'

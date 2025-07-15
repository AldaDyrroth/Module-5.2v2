from enum import Enum


class Selectors(Enum):

    # CartPage
    CART_REMOVE_SELECTOR = ".cart_item >> text='Remove'"
    CART_RETURN_SELECTOR = ".cart_footer >> text='Continue Shopping'"
    CART_CHECKOUT_SELECTOR = "#checkout"
    CART_ITEM_SELECTOR = ".cart_item"

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
    INVENTORY_BURGER_MENU_SELECTOR = "#react-burger-menu-btn"

    # LoginPage
    LOGIN_USERNAME_SELECTOR = '#user-name'
    LOGIN_PASSWORD_SELECTOR = '#password'
    LOGIN_LOGIN_BUTTTON_SELECTOR = '#login-button'
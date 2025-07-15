from enum import Enum


class ExpectedData(Enum):
    LOGIN_PAGE = 'Login'
    INVENTORY_PAGE = 'Products'
    CART_PAGE = 'Your Cart'
    CHECKOUT_STEP_ONE = 'Checkout: Your Information'
    CHECKOUT_STEP_TWO = 'Checkout: Overview'
    COMPLETE_PAGE = 'Checkout: Complete!'

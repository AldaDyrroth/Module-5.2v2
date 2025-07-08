from src.pages.inventory_page import InventoryPage
from src.pages.cart_page import CartPage
from src.pages.checkout_page import CheckoutPage
from src.pages.login_page import LoginPage
from constant import Par


class PositiveScenarios:
    def __init__(self,
                 inventory: InventoryPage,
                 cart: CartPage,
                 checkout: CheckoutPage,
                 login: LoginPage,
            ):
        self.inventory = inventory
        self.cart = cart
        self.checkout = checkout
        self.login = login

    def login_in_site(self, username, password):
        self.login.authorization(username, password)



class NegativeScenarios:
    pass
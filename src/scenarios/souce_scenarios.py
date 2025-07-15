from src.pages.inventory_page import InventoryPage
from src.pages.cart_page import CartPage
from src.pages.checkout_page import CheckoutPage
from src.pages.login_page import LoginPage


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

    def login_on_site(self, username, password, num: int = 1):
        """
        Сценарий: авторизация пользоаветеля
        """

        self.login.authorization(username, password)

    def add_goods_to_cart(self, num: int = 1):
        """
        Сценарий: сваливаем всю дешевку в свой контейнер для мусора
        """

        for i in range(num):
            self.inventory.add_item_to_cart()

class AsyncPositiveScenarios:
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



class NegativeScenarios:
    pass
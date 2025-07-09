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

    def login_on_site(self, username, password, num: int = 1):
        """
        Сценарий: просто авторизация
        """

        self.login.authorization(username, password)

        # for i in range(num):
        #     self.inventory.add_item_to_cart()
        #
        #
        # self.login.authorization(username, password)

    def add_goods_to_cart(self, num: int = 1):
        """
        Сценарий: сваливаем всю дешевку в свой контейнер для мусора
        """

        for i in range(num):
            self.inventory.add_item_to_cart()






class NegativeScenarios:
    pass
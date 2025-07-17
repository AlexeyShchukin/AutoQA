import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from page_object_model.pages.cart_page import CartPage
from page_object_model.pages.inventory_page import InventoryPage
from page_object_model.pages.login_page import LoginPage
from page_object_model.tests.base_test import BaseTest


class TestCart(BaseTest):
    # def test_backpack_cost(self):
    # 1. Login with valid data
    # self.login_page.success_login("standard_user", "secret_sauce")

    # 2. Remember the cost of the item "Backpack"
    # backpack_price = self.inventory_page.get_item_price("Sauce Labs Backpack")

    # 3. Add item "Backpack" to the cart
    # self.inventory_page.add_item_to_cart("Sauce Labs Backpack")

    # 4. Click on the cart button
    # self.inventory_page.go_to_cart()

    # 5. Check that the cost of the item in the cart equals to the cost of the item on the Inventory page
    # cart_price = self.cart_page.get_cart_item_price("Sauce Labs Backpack")
    # assert backpack_price == cart_price, "Цена товара в корзине не совпадает с ценой на странице инвентаря."

    def test_total_price(self):
        self.login_page.success_login("standard_user", "secret_sauce")

        for i in range(1, 6, 2):
            self.inventory_page.click_add_to_cart_button_per_item(i)

        self.inventory_page.click_cart_button()

        self.cart_page.proceed_to_checkout()

        self.checkout_first_page.enter_all_data("Oleksii", "Shchukin", "39288")
        self.checkout_first_page.press_continue()

        assert self.checkout_second_page.get_total_price() == "Total: $58.29"

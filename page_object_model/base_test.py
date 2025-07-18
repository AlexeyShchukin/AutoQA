import pytest
from selenium import webdriver

from page_object_model.pages.cart_page import CartPage
from page_object_model.pages.checkout_first_page import CheckoutFirstPage
from page_object_model.pages.checkout_second_page import CheckoutSecondPage
from page_object_model.pages.inventory_page import InventoryPage
from page_object_model.pages.login_page import LoginPage


class BaseTest:
    @pytest.fixture(autouse=True)
    def driver(self):
        driver = webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")

        self.driver = driver
        self.inventory_page = InventoryPage(driver)
        self.login_page = LoginPage(driver)
        self.cart_page = CartPage(driver)
        self.checkout_first_page = CheckoutFirstPage(driver)
        self.checkout_second_page = CheckoutSecondPage(driver)

        yield
        driver.quit()
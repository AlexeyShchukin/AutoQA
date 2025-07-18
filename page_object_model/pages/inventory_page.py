from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_items(self):
        return self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))

    def get_items_amount(self):
        return len(self.get_items())

    def all_items_are_displayed(self):
        return all(item.is_displayed() for item in self.get_items())

    def get_item_names(self):
        return [
            item.text for item in
            self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_name")))]

    def all_items_names_are_displayed(self):
        return all(name.strip() != "" for name in self.get_item_names())

    def all_item_names_are_not_empty(self):
        return all(bool(name.strip()) for name in self.get_item_names())

    def all_item_names_contains_sauce_labs(self):
        return all(name.startswith("Sauce Labs") for name in self.get_item_names())

    def get_item_by_number(self, number):
        return self.wait.until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, f".inventory_item:nth-child({number})"
            ))
        )

    def _get_button_per_item(self, number):
        return self.wait.until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, f".inventory_item:nth-child({number}) button"
            ))
        )

    def click_add_to_cart_button_per_item(self, number):
        button = self._get_button_per_item(number)
        button.click()

    def add_items_to_cart(self, nums: list[int]):
        for num in nums:
            self.click_add_to_cart_button_per_item(num)

    def _get_cart_button(self):
        return self.wait.until(
            EC.visibility_of_element_located((
                By.CLASS_NAME, "shopping_cart_link"
            ))
        )

    def click_cart_button(self):
        button = self._get_cart_button()
        button.click()

    def get_price_per_item(self, number):
        return self.wait.until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, f".inventory_item:nth-child({number}) .inventory_item_price"
            ))
        ).text


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutFirstPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def _get_first_name_field(self):
        return self.wait.until(EC.visibility_of_element_located((By.ID, "first-name")))

    def _get_last_name_field(self):
        return self.wait.until(EC.visibility_of_element_located((By.ID, "last-name")))

    def _get_postcode_field(self):
        return self.wait.until(EC.visibility_of_element_located((By.ID, "postal-code")))

    def enter_first_name(self, first_name):
        first_name_field = self._get_first_name_field()
        first_name_field.clear()
        first_name_field.send_keys(first_name)

    def enter_last_name(self, last_name):
        last_name_field = self._get_last_name_field()
        last_name_field.clear()
        last_name_field.send_keys(last_name)

    def enter_postcode_field(self, postcode):
        postcode_field = self._get_postcode_field()
        postcode_field.clear()
        postcode_field.send_keys(postcode)

    def fill_checkout_form(self, first_name, last_name, postcode):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postcode_field(postcode)

    def click_continue(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()

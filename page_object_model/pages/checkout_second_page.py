from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutSecondPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_total_price(self):
        return self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label"))).text

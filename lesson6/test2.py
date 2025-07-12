import pytest, time, math
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture()
def driver():
    service = Service("C://Program Files/ChromDriver/chromedriver.exe")
    options = Options()
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_window_size(1024, 768)
    yield driver
    driver.quit()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def test_alert(driver):
    driver.get("https://suninjuly.github.io/math.html")
    x_value = driver.find_element(By.ID, "input_value").text
    result = calc(x_value)
    answer_input = driver.find_element(By.ID, "answer")
    answer_input.send_keys(result)
    robot_checkbox = driver.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()
    robots_rule_radio = driver.find_element(By.ID, "robotsRule")
    robots_rule_radio.click()
    submit_button = driver.find_element(By.CLASS_NAME, "btn-default")
    submit_button.click()

    wait = WebDriverWait(driver, 10)

    wait.until(EC.alert_is_present())

    alert = driver.switch_to.alert
    text = alert.text
    assert "Congrats, you've passed the task!" in text

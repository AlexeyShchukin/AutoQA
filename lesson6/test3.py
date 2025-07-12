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


def test_with_tabs(driver):
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.execute_script("window.open('https://google.com', '_blank');")
    # Получаем список всех вкладок
    tabs = driver.window_handles
    print("Идентификаторы вкладок:", tabs)
    # Переключаемся на вторую вкладку (Google)
    driver.switch_to.window(tabs[1])
    print("Текущая вкладка:", driver.current_window_handle)
    sleep(2)
    driver.close()
    sleep(2)
    driver.switch_to.window(tabs[0])
    print("Текущая вкладка:", driver.current_window_handle)
    sleep(2)
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


def test_with_hover(driver):
    #url = "https://the-internet.herokuapp.com/hovers"
    url = "https://crossbrowsertesting.github.io/hover-menu.html"
    driver.get(url)
    #element_to_hover = driver.find_element(By.CSS_SELECTOR, "#content > div > div:nth-child(5)")
    actions = ActionChains(driver)
    dropdown = driver.find_element(By.LINK_TEXT, "Dropdown")
    actions.move_to_element(dropdown).perform()
    sleep(1)
    secondary_menu = driver.find_element(By.LINK_TEXT, "Secondary Menu")
    actions.move_to_element(secondary_menu).perform()
    sleep(1)
    secondary_action = driver.find_element(By.LINK_TEXT, "Secondary Action")
    secondary_action.click()
    sleep(1)
    wait = WebDriverWait(driver, 10)
    header = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div > div.jumbotron.secondary-clicked > h1")))
    assert header.text == "Secondary Page"

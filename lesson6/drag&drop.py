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


def test_dragging(driver):
    driver.get("https://jqueryui.com/droppable/")
    # Переключаемся в iframe, если drag-and-drop внутри фрейма
    driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))

    # Находим элементы
    source = driver.find_element(By.ID, "draggable")  # Что перетаскиваем
    target = driver.find_element(By.ID, "droppable")  # Куда перетаскиваем

    # Выполняем перетаскивание
    actions = ActionChains(driver)
    actions.drag_and_drop(source, target).perform()
    sleep(3)

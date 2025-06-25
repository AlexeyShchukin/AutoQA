from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

service = Service("C://Program Files/ChromDriver/chromedriver.exe")
options = Options()
driver = webdriver.Chrome(service=service, options=options)
driver.set_window_size(1024, 768)

driver.get("https://suninjuly.github.io/cats.html")

obj = driver.find_element(By.CSS_SELECTOR, "body > main > section > div > h1")
assert obj.text == "Cat memes"

from selenium import webdriver
from chromedriver_py import binary_path
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

"""Открытие браузера"""
svc = webdriver.ChromeService(executable_path=binary_path)
driver = webdriver.Chrome(service=svc)
driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
driver.maximize_window()

# Основной код
start = driver.find_element(By.CSS_SELECTOR, '#start > button')
start.click()


wait = WebDriverWait(driver, 10)
value = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#finish")))

assert value.text == "Hello World!"
# Не закрываем браузер после выполнения команды
input("Нажмите Enter для завершения программы...")

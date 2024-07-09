from selenium import webdriver
from chromedriver_py import binary_path
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

"""Открытие браузера"""
svc = webdriver.ChromeService(executable_path=binary_path)
driver = webdriver.Chrome(service=svc)
driver.get("https://www.qa-practice.com/elements/input/simple")
driver.maximize_window()

#Основной код
user_name = driver.find_element(by=By.XPATH,value='//*[@id="id_text_string"]')
user_name.send_keys("Submit")
user_name.send_keys(Keys.ENTER)
value_txt = driver.find_element(by=By.XPATH,value='//*[@id="result-text"]')
print(value_txt.text)

# Закрываем браузер после выполнения команды
input("Нажмите Enter для завершения программы...")

# Закрываем браузер
driver.quit()

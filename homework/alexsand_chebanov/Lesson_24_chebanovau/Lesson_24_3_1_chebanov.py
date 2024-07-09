from selenium.webdriver.support.select import Select
from selenium import webdriver
from chromedriver_py import binary_path
from selenium.webdriver.common.by import By


"""Открытие браузера"""
svc = webdriver.ChromeService(executable_path=binary_path)
driver = webdriver.Chrome(service=svc)
driver.get("https://www.qa-practice.com/elements/select/single_select")
driver.maximize_window()
driver.implicitly_wait(5)

# Основной код
select = driver.find_element(By.CSS_SELECTOR, '#id_choose_language')
dd = Select(select)
dd.select_by_value("2")

select = driver.find_element(By.XPATH, "//select[@name='choose_language']/option[@value='2']")

submit = driver.find_element(By.CSS_SELECTOR, "#submit-id-submit")
submit.click()

value = driver.find_element(By.CSS_SELECTOR, "#result-text")

assert value.text == "Ruby"

# Не закрываем браузер после выполнения команды
input("Нажмите Enter для завершения программы...")

# Подскажите пожалуйста почему не проходит assert select.text == value.text

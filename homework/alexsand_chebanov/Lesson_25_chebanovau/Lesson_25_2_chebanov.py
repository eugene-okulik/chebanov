from selenium.webdriver import ActionChains
from selenium import webdriver
from chromedriver_py import binary_path
from selenium.webdriver.common.by import By


"""Открытие браузера"""
svc = webdriver.ChromeService(executable_path=binary_path)
driver = webdriver.Chrome(service=svc)
driver.get("https://magento.softwaretestingboard.com/gear/bags.html")
driver.maximize_window()
driver.implicitly_wait(10)

# Основной код
element = driver.find_element(By.XPATH, '//li[contains(@class,"item product product-item")][1]')
achains = ActionChains(driver)                  # Импортировали класс октевации действий
achains.move_to_element(element).perform()         # Навели на элемент
driver.find_element(By.CSS_SELECTOR, ".action.tocompare").click()  # Нажали на элемент который появляеться при наведении

driver.execute_script('window.scrollTo(0, 500)')
compare_txt = driver.find_element(By.XPATH, '//*[text()="Push It Messenger Bag"]').text

assert compare_txt == "Push It Messenger Bag"


# Не закрываем браузер после выполнения команды
input("Нажмите Enter для завершения программы...")

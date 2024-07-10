from selenium import webdriver
from chromedriver_py import binary_path
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
"""Открытие браузера"""
svc = webdriver.ChromeService(executable_path=binary_path)
driver = webdriver.Chrome(service=svc)
driver.get("https://www.demoblaze.com/index.html")
driver.maximize_window()

# Основной код
wait = WebDriverWait(driver, 15)

tovar = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Nokia lumia 1520"]')))  # Нашли товар
ActionChains(driver).key_down(Keys.CONTROL).click(tovar).perform()                           # Открыли во второй вкладке

driver.switch_to.window(driver.window_handles[1])                                      # Переключились на вторую вкалдку

add_to_cart = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[text()="Add to cart"]')))  # Добавили в корзину
add_to_cart.click()

driver.send_keys(Keys.ENTER)                                                            # Отработали всплывающие меню
driver.close()                                                                          # Закрыли вкладку
driver.switch_to.window(driver.window_handles[0])                                     # Переключились на первую вкладку


cart = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#cartur")))           # Перешли в карзину
cart.click()

title = driver.find_element(By.XPATH, '//*[text()="Nokia lumia 1520"]').text        # Сравнили товар
assert title == tovar.text

# Закрываем браузер после выполнения команды
input("Нажмите Enter для завершения программы...")

# Закрываем браузер
driver.quit()

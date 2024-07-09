from selenium import webdriver
from chromedriver_py import binary_path
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

"""Открытие браузера"""
svc = webdriver.ChromeService(executable_path=binary_path)
driver = webdriver.Chrome(service=svc)
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
driver.execute_script('window.scrollTo(0, 500)')
wait = WebDriverWait(driver, 5)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#submit")))
driver.execute_script('window.scrollTo(0, 500)')

# Основной код
first_name = driver.find_element(by=By.CSS_SELECTOR, value='#firstName')
first_name.send_keys("Alex")

last_name = driver.find_element(by=By.XPATH, value='//*[@id="lastName"]')
last_name.send_keys("Alexsandrovich")

email = driver.find_element(by=By.XPATH, value='//*[@id="userEmail"]')
email.send_keys("name@mail.ru")

gender = driver.find_element(by=By.XPATH, value='//*[text()="Other"]')
gender.click()

mobile = driver.find_element(by=By.XPATH, value='//*[@id="userNumber"]')
mobile.send_keys("9379992985")

date_of_birth = driver.find_element(by=By.XPATH, value='//*[@id="dateOfBirthInput"]')

subjects = driver.find_element(by=By.CSS_SELECTOR, value='#subjectsInput')
subjects.send_keys("English")
subjects.send_keys(Keys.ENTER)

hobbies = driver.find_element(By.CSS_SELECTOR, 'label.custom-control-label[for="hobbies-checkbox-3"]')
hobbies.click()


driver.execute_script('window.scrollTo(0, 500)')
current_address = driver.find_element(by=By.XPATH, value='//*[@id="currentAddress"]')
current_address.send_keys("Russian,Moscow,Pertovka 38")

state_adn_city_1 = driver.find_element(By.ID, 'react-select-3-input')
state_adn_city_1.send_keys("NCR")
state_adn_city_1.send_keys(Keys.ENTER)

state_adn_city_2 = driver.find_element(By.ID, 'react-select-4-input')
state_adn_city_2.send_keys("Noida")
state_adn_city_2.send_keys(Keys.ENTER)

submit_button = driver.find_element(By.ID, "submit")
submit_button.click()

close_modal = driver.find_element(By.ID, 'closeLargeModal')
close_modal.click()

# Не закрываем браузер после выполнения команды
input("Нажмите Enter для завершения программы...")

# Закрываем браузер
driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

field_username = driver.find_element(By.CSS_SELECTOR, '#user-name')
field_password = driver.find_element(By.CSS_SELECTOR, '#password')
button_submit = driver.find_element(By.CSS_SELECTOR, '#login-button')

if field_username is not None and field_password is not None and button_submit is not None:
    print('Элементы найдены')
else:
    print('Элементы не найдены')







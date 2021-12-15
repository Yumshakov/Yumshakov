from selenium import webdriver
import math
import time

from selenium.webdriver.common.by import By

link = " http://suninjuly.github.io/find_xpath_form"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    input_name = browser.find_element(By.XPATH, '//div[1]/input')
    input_name.send_keys('Ivan')
    input_last_name = browser.find_element(By.NAME, 'last_name')
    input_last_name.send_keys('Petrov')
    input_city = browser.find_element(By.CLASS_NAME, 'form-control.city')
    input_city.send_keys('Moskow')
    input_country = browser.find_element(By.ID, 'country')
    input_country.send_keys('Russia')
    button = browser.find_element(By.XPATH, "//button[text() = 'Submit']")
    button.click()

finally:
    time.sleep(4)
    browser.quit()


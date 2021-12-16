'''
Так же реализовать через tkinter форму для ввода ИНН
'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#INN = input('Введите ИНН: ')

browser = webdriver.Chrome()
url = "https://egrul.nalog.ru/index.html"
browser.get(url)
try:

    input_inn = browser.find_element(By.ID, 'query')
    input_inn.send_keys("7453228020")
    time.sleep(1)
    btn_search = browser.find_element(By.ID, "btnSearch")
    btn_search.click()
    time.sleep(2)
    btn_get_egrul = browser.find_element(By.CLASS_NAME, "btn-with-icon.btn-excerpt.op-excerpt")
    btn_get_egrul.click()

finally:
    time.sleep(1)
    browser.quit()

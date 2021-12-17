from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(url)

def main_functions():

    lst_text = ['Ivan', 'Petrov', 'Ivan@Petrov']
    input_text = browser.find_elements(By.CSS_SELECTOR, 'input[type=text]')
    i = 0
    for elem in input_text:
        elem.send_keys(lst_text[i])
        i += 1
    directory = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(directory, 'text.txt')
    load_file = browser.find_element(By.ID, 'file')
    load_file.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()
if __name__ == '__main__':
    try:
        main_functions()
    finally:
        time.sleep(7)
        browser.quit()

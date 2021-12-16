from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(url)

def main_functions():

    get_num1 = browser.find_element(By.ID, 'num1').text
    get_num2 = browser.find_element(By.ID, 'num2').text
    res = sum(map(int, [get_num1, get_num2]))
    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(str(res))
    browser.find_element(By.TAG_NAME, 'button').click()
if __name__ == '__main__':
    try:
        main_functions()
    finally:
        time.sleep(7)
        browser.quit()

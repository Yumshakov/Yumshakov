from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time


def calc(x):

  return str(math.log(abs(12*math.sin(int(x)))))


def main_functions():

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    browser.find_element(By.ID, "book").click()
    find_attribute = browser.find_element(By.ID, 'input_value')
    y = calc(find_attribute.text)
    input_result = browser.find_element(By.ID, "answer")
    input_result.send_keys(y)
    btn_submit = browser.find_element(By.ID, "solve")
    btn_submit.click()


if __name__ == '__main__':
    try:
        url = 'http://suninjuly.github.io/explicit_wait2.html'
        browser = webdriver.Chrome()
        browser.get(url)
        main_functions()
    finally:
        time.sleep(7)
        browser.quit()




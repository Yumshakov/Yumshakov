from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By

class MainClass():

    def __init__(self, link):
        self.link = link
        self.browser = webdriver.Chrome()
        self.browser.get(link)

    def main_function(self):

        input_fn = self.browser.find_element(By.CSS_SELECTOR, '.first_block input.form-control.first')
        input_ln = self.browser.find_element(By.CSS_SELECTOR, '.first_block input.form-control.second')
        input_email = self.browser.find_element(By.CSS_SELECTOR, '.first_block input.form-control.third')
        input_fn.send_keys('Vasya')
        input_ln.send_keys('Petrov')
        input_email.send_keys('Vasya@Petrov')

        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)

    def quit(self):
        time.sleep(2)
        self.browser.quit()

class Test(unittest.TestCase):

    def test_link_1(self):
        test_one = MainClass('http://suninjuly.github.io/registration1.html')
        test_one.main_function()
        welcome_text = test_one.browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'NoSuchElementException')
        test_one.quit()

    def test_link_2(self):
        test_two = MainClass('http://suninjuly.github.io/registration2.html')
        test_two.main_function()
        welcome_text = test_two.browser.find_element(By.TAG_NAME, "h1").text
        #self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'NoSuchElementException')
        test_two.quit()



if __name__ == '__main__':
    unittest.main()


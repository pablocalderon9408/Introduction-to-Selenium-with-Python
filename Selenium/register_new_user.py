import unittest
from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner

class GoleroHomePage(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = self.driver
        driver.get('https://www.lacasadelgolero.com/')
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_new_user(self):
        driver = self.driver
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/header/div/div[2]/div/a[1]').click()
        driver.implicitly_wait(5)
        driver.find_element_by_id('customer_register_link').click()
        first_name = driver.find_element_by_id('RegisterForm-FirstName')
        last_name = driver.find_element_by_id('RegisterForm-LastName')
        email = driver.find_element_by_id('RegisterForm-email')
        password = driver.find_element_by_id('RegisterForm-password')
        submit_button = driver.find_element_by_xpath('/html/body/div[3]/main/div/div/div/div/form/p/input')
        driver.implicitly_wait(30)

        self.assertTrue(
            first_name.is_enabled()
            and last_name.is_enabled()
            and email.is_enabled()
            and password.is_enabled()
            and submit_button.is_enabled()
        )

        first_name.send_keys('Pablo')
        driver.implicitly_wait(10)
        last_name.send_keys('Calderon')
        email.send_keys('pablocalderon9408@gmail.com')
        password.send_keys('admin123')
        submit_button.click()

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(
        verbosity=2, 
        testRunner=HTMLTestRunner(
            output='reporte',
            report_name='reporte-log-in'
            ))
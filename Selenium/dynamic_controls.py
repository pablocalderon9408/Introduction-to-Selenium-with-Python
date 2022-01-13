import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyunitreport import HTMLTestRunner
from time import sleep

class DynamicControls(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = self.driver
        driver.implicitly_wait(0)
        driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Dynamic Controls').click()

    def test_dinamic(self):
        driver = self.driver
        checkbox = driver.find_element_by_xpath('//*[@id="checkbox-example"]')
        checkbox.click()
        sleep(5)

        remove_add_button = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/form[1]/button')
        remove_add_button.click()

        WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[1]/form[1]/button')))

        enable_disable_button = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/form[2]/button')
        enable_disable_button.click()
        WebDriverWait(driver,15).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[1]/form[2]/button')))

        text_area = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/form[2]/input')
        text_area.send_keys('Platzi')
        sleep(5)
        enable_disable_button.click()

    

    def tearDown(self) -> None:
        return super().tearDown()
        

if __name__ == "__main__":
    unittest.main(
        verbosity=2, 
        testRunner=HTMLTestRunner(
            output='reporte',
            report_name='reporte-search'
            ))
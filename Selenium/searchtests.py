import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner

class HomeTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo.onestepcheckout.com/')

    def test_search_tee(self):
        driver = self.driver 
        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('tee')
        search_field.submit()

    def test_search_salt(self):
        driver = self.driver 
        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('salt shaker')
        search_field.submit()

        products = driver.find_elements_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/a')
        self.assertEqual(1,len(products))

    def tearDown(self) -> None:
        return super().tearDown()
        

if __name__ == "__main__":
    unittest.main(
        verbosity=2, 
        testRunner=HTMLTestRunner(
            output='reporte',
            report_name='reporte-search'
            ))
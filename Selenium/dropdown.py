import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pyunitreport import HTMLTestRunner
from time import sleep

class Fudo(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://app-v2.fu.do/login.html')

    def test_excel_download(self):
        driver = self.driver
        user = self.driver.find_element_by_id('user')
        password = self.driver.find_element_by_id('password')

        self.assertTrue(
            user.is_enabled() 
            and user.is_displayed()
            and password.is_enabled()
            and password.is_displayed()
            )

        user.send_keys('administrador@laspoteiros')
        password.send_keys('calderones2022')
        sleep(5)

        log_in_button = self.driver.find_element_by_xpath('/html/body/div/div/form/button').click()
        sleep(10)

        expenses_button = self.driver.find_element_by_xpath('/html/body/ui-view/ert-take-away-sales/ert-top-bar/header/div/nav/ul/li[3]/a').click()
        sleep(5)

        expenses_option = []
        expenses_time_period = Select(self.driver.find_element_by_xpath(
            '/html/body/ui-view/ert-expenses/div/main/div/div/div[1]/ert-select-date/div/div[2]/div[2]/label/select')
            )

        self.assertEqual(5, len(expenses_time_period.options))

        for option in expenses_time_period.options:
            expenses_option.append(option.text)
        print(expenses_option)

        expenses_time_period.select_by_visible_text('Mensual')
        sleep(5)
        # self.assertTrue('store=Mensual' in self.driver.current_url)

        download = self.driver.find_element_by_xpath(
            '/html/body/ui-view/ert-expenses/div/main/div/h1/div/a').click()
        sleep(5)

        # alert = driver.switch_to.frame('Abriendo gastos.zip')
        ale = driver.current_window_handle()
        self.driver.quit()


    def tearDown(self) -> None:
        return super().tearDown()
        

if __name__ == "__main__":
    unittest.main(
        verbosity=2, 
        testRunner=HTMLTestRunner(
            output='reporte',
            report_name='reporte-search'
            ))
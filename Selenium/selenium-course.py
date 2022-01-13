import unittest
from selenium import webdriver
from pyunitreport import HTMLTestRunner

class HomePageTests(unittest.TestCase):

    # Se puede utilizar el decorador @classmethod para que todo se haga en 
    # una sola ventana: se le pone el @ a setUp y a tearDown, se les cambia
    # el nombre a setUpClass y tearDownClass y todos los self se cambian por cls
    # (Sólo se cambian los self de estos dos def)
    

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = self.driver
        driver.get('http://demo.onestepcheckout.com/')
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_page_is_opening(self):
        driver = self.driver
        driver.get('http://demo.onestepcheckout.com/')

    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element_by_name("q")

    def test_search_text_field_class_name(self):
        search_field = self.driver.find_element_by_class_name("input-text")

    def test_button_enabled(self):
        button = self.driver.find_element_by_class_name("button")

    # Inicialemente escribí find_element_by_tag_name y no me funcionaba, decía q el web object
    # no tenía la propiedad len(). Añadiendo la s en element funcionó
    def test_count_promo_banners(self):
        banner_list = self.driver.find_element_by_class_name("promos")
        banners = banner_list.find_elements_by_tag_name('img')
        self.assertEqual(3, len(banners)) 

    def test_vip_promo(self):
        vip_promo = self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div[2]/div/ul/li[2]/a/img')

    def test_shopping_cart(self):
        shopping_cart = self.driver.find_element_by_css_selector('div.header-minicart span.icon')

    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(
        verbosity=2, 
        testRunner=HTMLTestRunner(
            output='reporte',
            report_name='reporte-log-in'
            ))
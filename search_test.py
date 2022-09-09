import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By

class HomePageTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        driver = cls.driver

        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_search_text_field(self):
        search_element = self.driver.find_element(By.ID, 'search')

    def test_search_text_field_by_name(self):
        search_element = self.driver.find_element(By.NAME, 'q')

    def test_search_text_field_by_class(self):
        search_element = self.driver.find_element(By.CLASS_NAME, 'input-text')

    def test_search_button_enabled(self):
        search_element = self.driver.find_element(By.CLASS_NAME,'search-button')

    def test_count_of_promo_images(self):
        search_list = self.driver.find_element(By.CLASS_NAME, 'promos')

        banners = search_list.find_elements(By.TAG_NAME, 'img')

        self.assertEqual(3, len(banners))

    def test_vip_promo_element_by_xpath(self):
        vip_promo = self.driver.find_element(By.XPATH, '//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[2]/a/img')

    def test_shopping_cart(self):
        shopping_cart_icon = self.driver.find_element(By.CSS_SELECTOR, 'div.header-minicart span.icon')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
        
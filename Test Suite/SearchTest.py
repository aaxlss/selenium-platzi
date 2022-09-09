import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class SearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path=r'../chromedriver.exe')
        driver = cls.driver

        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME, 'q')
        search_field.clear()

        search_field.send_keys('tee')
        search_field.submit()

    def test_seach_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME, 'q')
        search_field.send_keys('salt shaker')
        search_field.submit()

        products = driver.find_elements(By.XPATH, '//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a')

        self.assertEqual(1, len(products))
        
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
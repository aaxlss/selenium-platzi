import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Navigation(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path=r'../chromedriver.exe')
        driver = cls.driver

        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://www.google.com/')

    def test_browser_navigation(self):
        driver = self.driver
        
        search_field = driver.find_element(By.NAME, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        search_field.clear()

        search_field.send_keys('platzi')
        search_field.submit()

        driver.back()
        driver.forward()
        driver.refresh()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
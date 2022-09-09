from os import unlink
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner

class Alerts(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path=r'../chromedriver.exe')
        driver = cls.driver

        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_compare_products_removal_alert(self):
        driver = self.driver
        #Finding element by name 
        search_field = driver.find_element(By.NAME, 'q')
        #Cleaning the search fild. Good practice
        search_field.clear()

        #Inserting tee text in the search field
        search_field.send_keys('tee')
        #Pressing the button to search
        search_field.submit()

        #finding element and click to compare and clear all
        driver.find_element(By.CLASS_NAME, 'link-compare').click()
        driver.find_element(By.LINK_TEXT, 'Clear All').click()

        #focussing to the current alert that is showing up
        alert = driver.switch_to.alert
        #Getting text from alert
        alert_text = alert.text

        #Comparing if the alert contains the specified text
        self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert_text)

        #Pressing the button accept from alert
        alert.accept()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
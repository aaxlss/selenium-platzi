import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from GooglePage import GooglePage

class GoogleTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path=r'../chromedriver.exe')
   
    def test_search(self):
        google = GooglePage(self.driver)

        google.open()
        google.search('Platzi')
        
        self.assertEqual('Platzi', google.keyword)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
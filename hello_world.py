from lib2to3.pgen2 import driver
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        driver = cls.driver

        driver.implicitly_wait(10)

    # def setUp(self) -> None:
    #     self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
    #     driver = self.driver

    #     driver.implicitly_wait(10)

    def test_hello_world(self):
        driver = self.driver
        driver.get('https://www.platzi.com')

    def test_wikipedia(self):
        driver = self.driver
        driver.get('https://www.wikipedia.org')

    """
        @classmethod ayuda a mantener una sola ventada
    """
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    # def tearDown(self) -> None:
    #     self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner= HTMLTestRunner(output='reportes', report_name='hello_world_report'))
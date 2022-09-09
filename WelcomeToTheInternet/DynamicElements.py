import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class DynamicElements(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path=r'../chromedriver.exe')
        driver = cls.driver

        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element(By.LINK_TEXT, 'Disappearing Elements').click()

    def test_name_elements(self):
        driver = self.driver
        
        options = []
        menu = 5
        tries = 1

        while len(options) < 5:
            options.clear()
            for i in range(menu):
                try:
                    option_name = driver.find_element(By.XPATH, f'/html/body/div[2]/div/div/ul/li[{i + 1}]/a')
                    options.append(option_name.text)
                    print(options)
                except:
                    print(f"Option number {i+1} has been found")
                    tries += 1
                    driver.refresh()

        print(f'Finished in {tries} tries')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
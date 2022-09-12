from this import d
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Typos(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path=r'../chromedriver.exe')
        driver = cls.driver

        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element(By.LINK_TEXT, 'Typos').click()

   
    def test_find_typo(self):
        driver = self.driver

        paragraph_to_check = driver.find_element(By.CSS_SELECTOR, '#content > div > p:nth-child(3)')

        text_to_check = paragraph_to_check.text
        tries = 1
        found = False
        correct_text = "Sometimes you'll see a typo, other times you won't."

        while text_to_check != correct_text:
            paragraph_to_check = driver.find_element(By.CSS_SELECTOR, '#content > div > p:nth-child(3)')

            text_to_check = paragraph_to_check.text
            driver.refresh()

        while not found:
            if text_to_check == correct_text:
                tries += 1
                driver.refresh()
                found = True

        self.assertEqual(found, True)

        print(f'It took {tries} tries to find the typo')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
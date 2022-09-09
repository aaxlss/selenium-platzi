import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class AddRemoveElement(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path=r'../chromedriver.exe')
        driver = cls.driver

        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()


    def test_add_remove(self):
        driver = self.driver

        elements_added = int(input('How many elements would you like to add? '))
        elements_removed = int(input('How many elements would you like to remove? '))
        total_elements = elements_added - elements_removed

        add_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/button')

        sleep(3)

        for i in range(elements_added):
            add_button.click()

        for _ in range(elements_removed):
            try:
                remove_button = driver.find_element(By.XPATH, '//*[@id="elements"]/button[1]')
                remove_button.click()
            except:
                print('there are not more elements to delete')
                break

        if total_elements > 0:
            print(f'There are {total_elements} elements')
        else:
            print(f'There are 0 elements')

        sleep(3)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
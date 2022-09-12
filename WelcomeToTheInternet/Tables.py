from this import d
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Tables(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path=r'../chromedriver.exe')
        driver = cls.driver

        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element(By.LINK_TEXT, 'Sortable Data Tables').click()

   
    def test_sort_tables(self):
        driver = self.driver
        table_columns = 5
        table_row = 4
        table_data = [[] for i in range(table_columns)]
        print(table_data)

        for i in range(table_columns):
            header = driver.find_element(By.XPATH, f'//*[@id="table1"]/thead/tr/th[{i + 1}]/span')
            table_data[i].append(header.text)

            for j in range(table_row):
                row = driver.find_element(By.XPATH, f'//*[@id="table1"]/tbody/tr[{j + 1}]/td[{i + 1}]')
                table_data[i].append(row.text)

        print(table_data)
                


    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
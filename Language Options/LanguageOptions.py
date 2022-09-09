import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner

class LanguageOptions(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
       cls.driver = webdriver.Chrome(executable_path=r'../chromedriver.exe')
       
       driver = cls.driver
       driver.implicitly_wait(30)
       driver.maximize_window()
       driver.get('http://demo-store.seleniumacademy.com/')


    def test_select_language(self):
        #Creating list with expected options
        exp_options = ['English', 'French', 'German']
        #List that will store the options that exist from the drowpdown
        active_options = []

        #search language element by id
        select_language = Select(self.driver.find_element(By.ID,'select-language'))

        #Validation if dropdown hast the same leng that the expected options
        self.assertEqual(3, len(exp_options))

        #storing current options from dropdown list
        for option in select_language.options:
            active_options.append(option.text)

        #validating if the expected options are the same options from dropdown list
        self.assertEqual(exp_options, active_options)

        #Validating if the option English is selected 
        self.assertEqual('English', select_language.first_selected_option.text)

        #Validat if German option exist. Getting item by visible text
        select_language.select_by_visible_text('German')

        #selecting again the item
        select_language = Select(self.driver.find_element(By.ID, 'select-language'))
        #validating if the string 'store=german' exists in the URL
        self.assertTrue('store=german' in self.driver.current_url)
        #validating if the first option is the German one
        select_language.select_by_index(0)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner= HTMLTestRunner(output='reportes', report_name='language_report'))
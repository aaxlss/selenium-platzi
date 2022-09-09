import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner
class RegisterNewUser(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path=r'../chromedriver.exe')

        driver = cls.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_new_user(self):
        driver = self.driver

        #it will look for the account button and click it
        driver.find_element(By.XPATH, '//*[@id="header"]/div/div[2]/div/a').click()

        #it will search the option using the text and click it
        driver.find_element(By.LINK_TEXT, 'Log In').click()

        #From the create account window will search button and validate if exists and it is enabled
        create_account_button = driver.find_element(By.XPATH, '//*[@id="login-form"]/div/div[1]/div[2]/a')
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()
        #it will validate if we are in the correct window comparing the title of the page
        self.assertEqual('Create New Customer Account', driver.title)
        
        #Getting the items from the form
        first_name = driver.find_element(By.ID, 'firstname')
        middle_name = driver.find_element(By.ID, 'middlename')
        last_name =  driver.find_element(By.ID, 'lastname')
        email_addres =  driver.find_element(By.ID, 'email_address')
        news_letter_subscrition =  driver.find_element(By.ID, 'is_subscribed')
        password =  driver.find_element(By.ID, 'password')
        confirm_password =  driver.find_element(By.ID, 'confirmation')
        submit_button =  driver.find_element(By.XPATH, '//*[@id="form-validate"]/div[2]/button')

        #Validating if the items exist and if they are enabled
        self.assertTrue(first_name.is_displayed and first_name.is_enabled)
        self.assertTrue(middle_name.is_displayed and middle_name.is_enabled)
        self.assertTrue(last_name.is_displayed and last_name.is_enabled)
        self.assertTrue(email_addres.is_displayed and email_addres.is_enabled)
        self.assertTrue(news_letter_subscrition.is_displayed and news_letter_subscrition.is_enabled)
        self.assertTrue(password.is_displayed and password.is_enabled)
        self.assertTrue(confirm_password.is_displayed and confirm_password.is_enabled)
        self.assertTrue(submit_button.is_displayed and submit_button.is_enabled)

        #Inserting information in the input elements
        first_name.send_keys('Test')
        middle_name.send_keys('Test')
        last_name.send_keys('Test')
        email_addres.send_keys('Test@testing.com')
        password.send_keys('Test123456')
        confirm_password.send_keys('Test123456')
        submit_button.click()

    @classmethod
    def tearDownClass(cls) -> None:
        return super().tearDownClass()

if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner= HTMLTestRunner(output='reportes', report_name='hello_world_report'))
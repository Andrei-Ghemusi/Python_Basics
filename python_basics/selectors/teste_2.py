import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class clasa_de_Test(unittest.TestCase):

    ACCOUNT = (By.XPATH, '//*[@id="customer-account"]/div/i')
    USERNAME = (By.XPATH, '//*[@id="email"]')
    PASSWORD = (By.XPATH, '//*[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="pizokel_customer_submit"]')
    FAILED_LOGIN_MESSAGE = (By.XPATH, '//*[@id="loginform"]/div[1]/div')

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.chrome.maximize_window()
        self.chrome.get("https://www.fashiondays.ro/")
        self.chrome.implicitly_wait(2)

    def tearDown(self) -> None:
        self.chrome.quit()

#Test 1:
    def test_customer_login_url_check(self):
        self.chrome.find_element(*self.ACCOUNT).click()
        current_url = self.chrome.current_url
        expected_url = 'https://www.fashiondays.ro/customer/authentication'
        assert current_url == expected_url, f'ERROR, expected {expected_url} url, but got {current_url} instead'

    def test_failed_login(self):
        self.chrome.find_element(*self.ACCOUNT).click()
        self.chrome.find_element(*self.USERNAME).send_keys("andrei@gmail.com")
        self.chrome.find_element(*self.PASSWORD).send_keys("00000")
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        time.sleep(2)
        actual_message = self.chrome.find_element(*self.FAILED_LOGIN_MESSAGE).text
        expected_message = 'Adresa de email sau parola este incorecta. Te rugam sa introduci o alta combinatie.'
        self.assertTrue(expected_message in actual_message, f'ERROR, expected {expected_message}, but got {actual_message} instead')

    def test_error_message_after_Clear(self):
        self.chrome.find_element(*self.ACCOUNT).click()
        self.chrome.find_element(*self.USERNAME).send_keys("andrei@gmail.com")
        self.chrome.find_element(*self.PASSWORD).send_keys("00000")
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        message = WebDriverWait(self.chrome, 99).until(EC.presence_of_element_located(self.FAILED_LOGIN_MESSAGE))
        error_message = self.chrome.find_element(*self.FAILED_LOGIN_MESSAGE).text
        self.chrome.find_element(*self.USERNAME).clear()
        try:
            self.chrome.find_element(*self.FAILED_LOGIN_MESSAGE)
        except:
            f'Error message {error_message} is no longer displayed'

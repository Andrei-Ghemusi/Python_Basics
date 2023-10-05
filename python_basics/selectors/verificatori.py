import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Intrare(unittest.TestCase):

    FORM_LINK = (By.LINK_TEXT, 'Form Authentication')
    XPATH_VERIFY= (By.XPATH, '//h2')
    LOGIN_BUTTON = (By.XPATH, '//button[@class = "radius" and @type = "submit"]')
    HREF_ELEMENT = (By.XPATH, '//*[@id="page-footer"]/div/div/a')
    ERROR_MESSAGE_NO_CRED = (By.XPATH, '//*[@id="flash"]')
    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    INCORRECT_CRED_ERROR = (By.XPATH, '//*[@id="flash"]')
    CLICK_ON_X = (By.XPATH, '//*[@id="flash"]/a')
    LABEL = (By.XPATH, '//label')
    FLASH_CLASS = (By.XPATH, '//*[@class="flash success"]')
    LOGOUT_BUTTON = (By.XPATH, '//*[@id="content"]/div/a/i')

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.chrome.maximize_window()
        self.chrome.get("https://the-internet.herokuapp.com/")
        self.chrome.find_element(*self.FORM_LINK).click()
        self.chrome.implicitly_wait(2)

    def tearDown(self) -> None:
        self.chrome.quit()


# Test 1 - Verifică dacă noul url e corect
    def test_new_url(self):
        actual_url = self.chrome.current_url
        expected_url = 'https://the-internet.herokuapp.com/login'
        assert actual_url == expected_url, f'Error, expected {expected_url}, got {actual_url} instead'
        print('TEST PASSED')


# Test 2 - Verifică dacă page title e corect
    def test_page_title(self):
        page_title = self.chrome.title
        expected_title = "The Internet"
        assert page_title == expected_title, f'ERROR, expected {expected_title}, got {page_title} instead'


# Test 3 - Verifică textul de pe elementul xpath=//h2 e corect
    def test_page_header(self):
        page_header = self.chrome.find_element(*self.XPATH_VERIFY).text
        expected_header = 'Login Page'
        assert page_header == expected_header, f'ERROR, expected {expected_header}, got {page_header} instead'


# Test 4 - Verifică dacă butonul de login este displayed
    def test_login_display(self):
        is_login_displayed = self.chrome.find_element(*self.LOGIN_BUTTON).is_displayed()
        assert (is_login_displayed == True)


# Test 5 - Verifică dacă butonul de login este displayed
    def test_href_elemental_selenium(self):
        element = self.chrome.find_element(*self.HREF_ELEMENT)
        href_actual = element.get_attribute('href')
        href_expected = 'http://elementalselenium.com/'
        assert href_actual == href_expected, f'ERROR, expected {href_expected}, got {href_actual} instead'


# Test 6 - Lasă goale user și pass, Click login, Verifică dacă eroarea e displayed
    def test_user_and_pass_empty(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        text_error_displayed = self.chrome.find_element(*self.ERROR_MESSAGE_NO_CRED).is_displayed()
        assert (text_error_displayed == True)


# Test 7 - - Completează cu user și pass invalide
    # - Click login
    # - Verifică dacă mesajul de pe eroare e corect
    # - Este și un x pus acolo extra așa că vom folosi soluția de mai jos
    def test_user_and_pass_incorrect(self):
        self.chrome.find_element(*self.USERNAME).send_keys("Tommy")
        self.chrome.find_element(*self.PASSWORD).send_keys('1234')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        actual_error = self.chrome.find_element(*self.INCORRECT_CRED_ERROR).text
        expected_error = 'Your username is invalid!'
        self.assertTrue(expected_error in actual_error, 'ERROR, message is incorrect')


# Test 8 - Lasă goale user și pass
    # - Click login
    # - Apasă x la eroare
    # - Verifică dacă eroarea a dispărut
    def test_is_error_displayed_when_empty(self):
        self.chrome.find_element(*self.USERNAME).clear()
        self.chrome.find_element(*self.PASSWORD).clear()
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        self.chrome.find_element(*self.CLICK_ON_X).click()
        time.sleep(2)
        is_error_displayed = self.chrome.find_element(*self.ERROR_MESSAGE_NO_CRED).is_displayed()
        assert (is_error_displayed == True)

    ''' la asta de mai sus imi da passed, desi nu ar trebui, de ce?'''


# Test 9 - Ia ca o listă toate //label
    # - Verifică textul ca textul de pe ele să fie cel așteptat (Username și
    # Password)
    # - Aici e ok să avem 2 asserturi
    def test_label_list(self):
        lista = self.chrome.find_elements(*self.LABEL)
        actual_username = lista[0].text
        expected_username = 'Username'
        assert (actual_username == expected_username), f'ERROR, expected {expected_username}, got {actual_username} instead'
        actual_pass = lista[1].text
        expected_pass = 'Password'
        assert (actual_pass == expected_pass), f'ERROR, expected {expected_pass}, got {actual_pass} instead'


# Test 10 - Completează cu user și pass valide
    # - Click login
    # - Verifică ca noul url CONTINE /secure
    # - Folosește un explicit wait pentru elementul cu clasa ’flash succes’
    # - Verifică dacă elementul cu clasa=’flash succes’ este displayed
    # - Verifică dacă mesajul de pe acest element CONȚINE textul ‘secure area!’
    def test_user_si_pass_valide_secure(self):
        self.chrome.find_element(*self.USERNAME).send_keys('tomsmith')
        self.chrome.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        actual_url = self.chrome.current_url
        expected_in_url = '/secure'
        self.assertTrue(expected_in_url in actual_url, f'ERROR, THIS IS NOT SECURE, expected {expected_in_url}, but got none in {actual_url}')
        flash_succes = WebDriverWait(self.chrome, 1).until(EC.presence_of_element_located(self.FLASH_CLASS)).is_displayed()
        #is_flash_displayed = self.chrome.find_element(*self.FLASH_CLASS).is_displayed()
        actual_message = self.chrome.find_element(*self.FLASH_CLASS).text
        expected_message = 'secure area!'
        self.assertTrue(expected_message in actual_message, f'ERROR, message {expected_message} not found in {actual_message}')
        assert (flash_succes == True)


# Test 11 - Completează cu user și pass valide
    # - Click login
    # - Click logout
    # - Verifică dacă ai ajuns pe https://the-internet.herokuapp.com/login
    def test_user_si_pass_valide_verify_url(self):
        self.chrome.find_element(*self.USERNAME).send_keys('tomsmith')
        self.chrome.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        self.chrome.find_element(*self.LOGOUT_BUTTON).click()
        actual_url = self.chrome.current_url
        expected_url = "https://the-internet.herokuapp.com/login"
        assert actual_url == expected_url, f'ERROR, expected {expected_url}, got {actual_url} instead'












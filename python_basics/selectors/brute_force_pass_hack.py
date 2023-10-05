import softest
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# Test 12 - brute force password hacking
# - Completează user tomsmith
# - Găsește elementul //h4
# - Ia textul de pe el și fă split după spațiu. Consideră fiecare cuvânt ca o
# potențială parolă.
# - Folosește o structură iterativă prin care să introduci rând pe rând
# parolele și să apeși pe login.
# - La final testul trebuie să îmi printeze fie
# ‘Nu am reușit să găsesc parola’
# ‘Parola secretă este [parola]’


class Brute(softest.TestCase):
    TEXT_TO_BE_EVALUATED = (By.XPATH, '//h4[@class = "subheader"]')
    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login"]/button/i')
    SECURE = (By.XPATH, '//h2')

    def setUp(self) -> None:
        self.chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.chrome.maximize_window()
        self.chrome.get("https://the-internet.herokuapp.com/login")
        self.chrome.implicitly_wait(2)

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_hack(self):
        potential_passwords = self.chrome.find_element(*self.TEXT_TO_BE_EVALUATED).text.split()
        for hacked_password in potential_passwords:
            self.chrome.find_element(*self.USERNAME).send_keys('tomsmith')
            self.chrome.find_element(*self.PASSWORD).send_keys(hacked_password)
            self.chrome.find_element(*self.LOGIN_BUTTON).click()
            login_confirm = self.chrome.find_element(*self.SECURE).text
            if login_confirm == 'Secure Area':
                print(f'Parola secreta este {hacked_password}')
                break
            else:
                print('Nu am reusit sa gasesc parola')




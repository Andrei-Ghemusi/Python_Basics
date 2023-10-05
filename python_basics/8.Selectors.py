from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

'''
!!! REMINDER !!!
Some of these sites might have been taken down or suffered multiple changes, so some of these might crack

I already commented some of these which were known to cause issues.
'''
# we initialize chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

# we maximize the window
chrome.maximize_window()

# ------------------------------------Selectors by ID ---------------------------------------------
# we go to an url
chrome.get('https://the-internet.herokuapp.com/login')
#
# 1
username = chrome.find_element(By.ID, 'username')
username.send_keys('georgie')

# 2
password = chrome.find_element(By.ID, 'password')
password.send_keys('1234')

# we go to an url
chrome.get('http://automationpractice.com/index.php?controller=authentication&back=my-account')

# # 3
# email_create = chrome.find_element(By.ID, 'email_create')
# email_create.send_keys('andreighemusi@gmail.com')

# ------------------------------------Selectors by Link Text ---------------------------------------
# 1
chrome.get('https://www.phptravels.net/')
chrome.find_element(By.LINK_TEXT, 'Blog').click()

# # 2
# chrome.get('http://automationpractice.com/index.php?controller=authentication&back=my-account')
# chrome.find_element(By.LINK_TEXT, 'Contact us').click()

# 3
chrome.get('https://formy-project.herokuapp.com/')
chrome.find_element(By.LINK_TEXT, 'Checkbox').click()
#
# ------------------------------------Selectors by Partial Link Text---------------------------------
# # 1
chrome.get('https://formy-project.herokuapp.com/')
chrome.find_element(By.PARTIAL_LINK_TEXT, 'Press').click()

chrome.get('https://www.techlistic.com/')
chrome.find_element(By.ID,"ez-accept-all").click()
sleep(5)
chrome.find_element(By.ID,"cookieChoiceDismiss").click()
chrome.find_element(By.PARTIAL_LINK_TEXT, 'Choosing Kotlin').click()

# ------------------------------------Selectors by Name ---------------------------------------
# # 1
# chrome.get('http://automationpractice.com/index.php')
# chrome.find_element(By.NAME, 'search_query').send_keys('Drew')

# 2
chrome.get('https://www.phptravels.net/signup')
chrome.find_element(By.NAME, 'phone').send_keys('0730305967')

# # 3
# chrome.get('http://automationpractice.com/index.php')
# chrome.find_element(By.NAME, 'email').send_keys('andreighemusi@gmail.com')

# ------------------------------------Selectors by Tag -------------------------------------
# # 1
chrome.get('https://www.phptravels.net/login')
input_list = chrome.find_elements(By.TAG_NAME, 'input')
input_list[0].send_keys('andrei.ghemusi')
input_list[1].send_keys('12345')

# 2
chrome.get('https://formy-project.herokuapp.com/form')
input_list = chrome.find_elements(By.TAG_NAME, 'Input')
input_list[0].send_keys('Hello')
input_list[1].send_keys('World ')
input_list[2].send_keys('Software tester')

# # 3
# chrome.get('http://automationpractice.com/index.php?controller=contact')
# chrome.find_element(By.TAG_NAME, 'textarea').send_keys('Thanks!')

# ------------------------------------Selectors by Class Name -------------------------------------

chrome.get('https://formy-project.herokuapp.com/autocomplete')
lista_elemente = chrome.find_elements(By.CLASS_NAME,"form-control")
lista_elemente[0].send_keys("Romania")
lista_elemente[1].send_keys("Babadag street")
lista_elemente[2].send_keys("Tulcea")

# ------------------------------------Selectors by CSS -------------------------------------
# 1 after ID
chrome.get('https://formy-project.herokuapp.com/autocomplete')
chrome.find_element(By.CSS_SELECTOR, 'input#autocomplete').send_keys('Andrei')

# 2 after class
chrome.get('https://www.phptravels.net/signup')
chrome.find_element(By.CSS_SELECTOR, 'input.form-control').send_keys('Ghemusi')

# 3 attribute=partial_value
chrome.get('https://www.phptravels.net/signup')
chrome.find_element(By.CSS_SELECTOR, 'input[placeholder*="Last"]').send_keys('QAtesting')

# -----------------------XPATH-----------------------------------------------------------------
# # 3 after attribute = value
chrome.get('https://www.phptravels.net/signup')
chrome.find_element(By.XPATH, '//input[@name="first_name"]').send_keys('Andrei')
chrome.find_element(By.XPATH, '//input[@placeholder="Last Name"]').send_keys('Ghemusi')
chrome.find_element(By.XPATH, '//input[@type="password"]').send_keys('969696')

# # 4 dupa textul de pe element
# chrome.get('http://automationpractice.com/index.php')
# chrome.find_element(By.XPATH, '//a[text()="Best Sellers"]').click()
# chrome.find_element(By.XPATH, '//a[text()="Contact us"]').click()

# 5 after partial text
chrome.get('https://www.phptravels.net/blog')
full_text = chrome.find_element(By.XPATH, '//a[contains(text(), "Independent Cultures")]').text # => here you can't click?
print(full_text)

# 6 with or: |
chrome.get('https://www.phptravels.net/login')
chrome.find_element(By.XPATH, '//input[@name="email"] | //a[@name="email"]').send_keys("andreighemusi@gmail.com")

# 7 with *
chrome.get('https://formy-project.herokuapp.com/autocomplete')
chrome.find_element(By.XPATH, '//*[@id="autocomplete"]').send_keys('OK')

# 8 using parent::
chrome.get('https://formy-project.herokuapp.com/form')
chrome.find_element(By.XPATH, '//label[text()="Job title"]/parent::strong')

# 9 using following-sibling::
chrome.get('https://formy-project.herokuapp.com/form')
chrome.find_element(By.XPATH, '//label[text()="Job title"]/parent::strong/following-sibling::input').send_keys("QA Automation Tester")
sleep(2)

# 10 A function similar to the one in the class that allows you to choose, through a parameter, which element you want to interact with..
def select_years_of_experience(select_by_visible_text):
    years_of_experience_dropdpwn = Select(chrome.find_element(By.ID, 'select-menu'))
    years_of_experience_dropdpwn.select_by_visible_text(select_by_visible_text)

select_years_of_experience("0-1")

sleep(4)
chrome.quit()




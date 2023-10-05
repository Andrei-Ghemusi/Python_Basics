import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())
chrome.maximize_window()
chrome.get('https://the-internet.herokuapp.com/login')
chrome.find_element(By.ID, 'username').clear()
chrome.find_element(By.ID, 'password').clear()
chrome.find_element(By.XPATH, '//button[@class = "radius" and @type = "submit"]').click()
chrome.find_element(By.XPATH, '//*[@id="flash"]/a').click()
is_error_displayed = chrome.find_element(By.XPATH, '//*[@id="flash"]').is_displayed()
assert (is_error_displayed == True)
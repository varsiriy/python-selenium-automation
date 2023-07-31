# HW 2. Amazon signin page Locators

# Amazon logo => By.XPATH, "//i[@aria-lable='Amazon']"
# Email field => By.ID, 'ap_email'
# Continue button => By.ID, 'continue'
# Conditions of use link => By.XPATH, "//a[text()= 'Conditions of Use']"
# Privacy Notice link => By.XPATH, "//a[text()= 'Privacy Notice']"
# Need help link => By.XPATH, "//span[@class='a-expander-prompt']"
# Forgot your password link => By.ID, 'auth-fpp-link-bottom'
# Other issues with Sing-in link => By.ID, 'ap-other-signin-issues-link'
# Create your Amazon accoint button => By.ID, 'createAccountSubmit'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

 # create a new Chrome browser instance

service = Service(executable_path=r'C:\Users\varsi\python-selenium-automation\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('http://www.amazon.com/')

# click Orders

driver.find_element(By.XPATH, "//span[text()='& Orders' and @ class='nav-line-2']"). click()

expected_result1 = 'Sign in'
actual_result1 = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text   ## Doesn't work with "//h1[text()= 'Sign in']"

assert expected_result1 == actual_result1, f'Expected {expected_result1} did not match Actual {actual_result1}'
print('Test case 1 passed')

email_input_field = driver.find_element(By.ID, 'ap_email')
expected_result2 = 'Email input field is presented'
actual_result2 = 'Email input field is presented' if email_input_field.is_displayed() else 'Email inpit field is NOT presented'

assert expected_result2 == actual_result2, f'Expected {expected_result2} did not match Actual {actual_result2}'
print('Test case 2 passed')

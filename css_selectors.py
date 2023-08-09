from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# create a new Chrome browser instance
service = Service(executable_path = '<provide your absolute path>')
driver = webdriver.Chrome(service=service)

# By ID
driver.find_element(By.ID, 'nav-search-submit-button')
driver.find_element(By.ID, 'nav-cart-count')

# CSS Selectors
# By  Class(es)
driver.find_element(By.CSS_SELECTOR, '.nav-input.nav-progressive-attribute')
driver.find_element(By.CSS_SELECTOR, '.nav-input')

# By ID
driver.find_element(By.CSS_SELECTOR, '#nav-search-submit-button')
# By ID, using tag
driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox')

# By ID + Class
driver.find_element(By.CSS_SELECTOR, '#nav-search-submit-button.nav-input.nav-progressive-attribute')
#By ID + Clas + tag
driver.find_element(By.CSS_SELECTOR, 'input#nav-search-submit-button.nav-input.nav-progressive-attribute')

# By other attributes: [attribute ='value']
driver.find_element(By.CSS_SELECTOR, "[name='field-keywords']")
driver.find_element(By.CSS_SELECTOR, "[type='text'][name='field-keywords']")

# By class + other attributes: .class[attributr='value']
driver.find_element(By.CSS_SELECTOR, ".nav-input[type='text'][name='field-keywords']")

# By partial attribute *
driver.find_element(By.CSS_SELECTOR, '[href*="ap_signin_notification_condition_of_use"]')

# By parent - child element   use space in between
driver.find_element(By.CSS_SELECTOR, "#legalTextRow a[href*='condition_of_use']")


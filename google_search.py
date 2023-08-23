from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep



# create a new Chrome browser instance
service = Service(executable_path=r'C:\Users\varsi\python-selenium-automation\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.maximize_window()
# define once
# will be applied to all find_element
# check fo element every 100 ms
driver.implicitly_wait(5)

driver.wait = WebDriverWait(driver, 10)

# open the url
driver.get('https://www.google.com/')

# populate search field
search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('cats')

search_btn = (By.NAME, 'btnK')

# Have to be defined in the codee where this wait is used
# It checks for the condition to be met every 500 ms
# always fail with TimeoutException
# support custom conditions, usually taken EC

driver.wait.until(EC.element_to_be_clickable(search_btn), message='Search btn not clickable').click()

# click search button
# driver.find_element(*search_btn).click()

# verify search results
assert 'cats' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()

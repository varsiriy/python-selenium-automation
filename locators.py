from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

 # create a new Chrome browser instance

service = Service(executable_path=r'C:\Users\varsi\python-selenium-automation\chromedriver.exe')
driver = webdriver.Chrome(service=service)

 # By ID
driver.find_element(By.ID, 'nav-search-submit-button')
driver.find_element(By.ID, 'nav-cart-count')

 # Xpath locator $x("//input[@placeholder='Search Amazon']")

 # Xpath can have 2 locators  $x("//a[@class='nav-a  ' and @data-csa-c-content-id='nav_cs_bestsellers']")

 # Tag and attribute

driver.find_element(By.XPATH, "//a[data-csa-c-content-id='nav_cs_bestsellers']")
driver.find_element(By.XPATH, "//input[@aria-lable='Search Amazon']")

 # Multiple attributes

driver.find_element(By.XPATH, "//a[@class='nav-a  ' and @data-csa-c-content-id='nav_cs_bestsellers']")

 # By Xpath, text

driver.find_element(By.XPATH, "//a[text()='Best Sellers']")
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a  ']")

 # Any tag = *

driver.find_element(By.XPATH, "//*[text()='Best Sellers' and @class='nav-a  ']")

 # Contains

driver.find_element(By.XPATH, "//a[contains( @href,'nav_cs_bestsellers')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Best Sellers') and class='nav-a  ']")


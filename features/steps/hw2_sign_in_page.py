
from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


# Click Orders
@when('Click orders')
def click_orders(context):
    context.driver.find_element(By.XPATH, "//span[text()='& Orders' and @ class='nav-line-2']"). click()


@then('Verify Sing in page opened')
def verify_sign_in_page_opened(context):
    expected_result1 = 'Sign in'
    actual_result1 = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text

    assert expected_result1 == actual_result1, f'Expected {expected_result1} did not match Actual {actual_result1}'
    print('Test case 1 passed')
    sleep(2)


@then('Verify email input field presented')
def verify_email_field(context):
    email_input_field = context.driver.find_element(By.ID, 'ap_email')
    assert email_input_field.is_displayed(), f'The element is not displayed'
    print('Test case 2 passed')
    sleep(2)

 ## Or   driver.find_element(By.ID, 'ap_email')     This is it. No assert needed

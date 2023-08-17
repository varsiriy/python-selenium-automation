from behave import given, when, then
from selenium.webdriver.common.by import By


@then('Verify that Amazon cart is empty')
def amazon_card_empty(context):
    expected_result = 'Your Amazon Cart is empty'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, '.a-row.sc-your-amazon-cart-is-empty').text
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'


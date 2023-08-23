from behave import given, when, then
from selenium.webdriver.common.by import By


SEARCH_RESULT = (By.CSS_SELECTOR, '.a-color-state.a-text-bold')

@then('Verify search results is {expected_result}')
def verify_search_result(context, expected_result):
    actual_result = context.driver.find_element(*SEARCH_RESULT).text
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match {actual_result}'



@when('Click on the fist product')
def click_on_the_product(context):
    context.driver.find_element(By.CSS_SELECTOR, '.a-link-normal.s-no-outline[href*="FWag-Salmon-Sweet-Potato-Recipe"]').click()
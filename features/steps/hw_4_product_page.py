from behave import given, when, then
from selenium.webdriver.common.by import By

@then ('Click One-time purchase radio btn')
def click_one_time_purchase(context):
    context.driver.find_element(By.CSS_SELECTOR, 'i.a-icon.a-accordion-radio.a-icon-radio-inactive').click()


@then('Click Add to Cart btn')
def click_add_to_cart_btn(context):
    context.driver.find_element(By.ID, "add-to-cart-button").click()


@then('Verify the product is Added to Cart')
def added_to_cart(context):
    expected_result = 'Added to Cart'
    actual_result = context.driver.find_element(By.CSS_SELECTOR,'span.a-size-medium-plus').text
    assert expected_result == actual_result, f'Error expected {expected_result} did not match actual {actual_result}'
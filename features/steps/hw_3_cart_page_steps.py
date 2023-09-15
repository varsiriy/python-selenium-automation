from behave import given, when, then
from selenium.webdriver.common.by import By

CART = (By.ID, 'nav-cart-count')
CART_ITEMS = (By.ID, 'sc-subtotal-label-buybox')
PRODUCT_NAME = (By.CSS_SELECTOR, "#sc-active-cart li")
CART_EMPTY = (By.CSS_SELECTOR, '.a-row.sc-your-amazon-cart-is-empty')

@when('Open cart page')
def open_cart_page(context):
    # context.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')
    context.app.shopping_cart.open_shopping_cart()


@then('Verify Your Shopping cart is empty')
def amazon_card_empty(context):
    # expected_result = 'Your Amazon Cart is empty'
    # actual_result = context.driver.find_element(*CART_EMPTY).text
    # assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
    context.app.shopping_cart.verify_amazon_card_empty()


@then('Verify cart has {expected_count} item(s)')
def verify_cart_count(context, expected_count):
    # actual_text = context.driver.find_element(*CART).text
    # assert expected_count == actual_text, f'Expected {expected_count}, but got {actual_text}'
    context.app.shopping_cart.verify_cart_has_correct_count(expected_count)


@then ('Verify cart has correct product')
def verify_product_name(context):
    # actual_name = context.driver.find_element(*PRODUCT_NAME).text
    # assert context.product_name[:35] in actual_name, f'Expected {context.product_name} but got {actual_name}'
    context.app.product_page.verify_cart_has_correct_product()


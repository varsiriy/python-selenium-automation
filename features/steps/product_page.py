from behave import given, when, then
from selenium.webdriver.common.by import By
#from time import sleep
from selenium.webdriver.support import expected_conditions as EC

FIRST_PRODUCT_NAME = (By.ID, 'title')
ADD_TO_CART_BTN = (By.ID, "add-to-cart-button")
COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")


@given('Open Amazon product {product_id} page')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')


@when ('Click One-time purchase radio btn')
def click_one_time_purchase(context):
    context.driver.find_element(By.CSS_SELECTOR, 'i.a-icon.a-accordion-radio.a-icon-radio-inactive').click()


@when('Click Add to Cart btn')
def click_add_to_cart_btn(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()



@then('Verify the product is Added to Cart')
def added_to_cart(context):
    expected_result = 'Added to Cart'
    actual_result = context.driver.find_element(By.CSS_SELECTOR,'span.a-size-medium-plus').text
    assert expected_result == actual_result, f'Error expected {expected_result} did not match actual {actual_result}'


@when ('Store product name')
def get_product_name(context):
    context.product_name = context.driver.find_element(*FIRST_PRODUCT_NAME).text
    print(f'Current product: {context.product_name}')


@then('Verify user can click through colors')
def verify_can_click_colors(context):
    expected_colors = ['Army Green', 'Black', 'Blue']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for color in colors[:3]:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text

        actual_colors.append(current_color)

    assert actual_colors == expected_colors, f'Expected {expected_colors} did not match actual {actual_colors}'


@then('Verify user can select through colors')
def verify_can_select_colors(context):
    expected_colors = ['Black', 'Blue Over Dye', 'Dark Blue Vintage']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for color in colors[:3]:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text

        actual_colors.append(current_color)

    assert actual_colors == expected_colors, f'Expected {expected_colors} did not match actual {actual_colors}'
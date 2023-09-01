from behave import given, when, then
from selenium.webdriver.common.by import By


SEARCH_RESULT = (By.CSS_SELECTOR, '.a-color-state.a-text-bold')
#PRODUCT_PRICE
SEARCH_RESULTS = (By.CSS_SELECTOR, '[data-component-type="s-search-result"]')
PRODUCT_TITLE = (By.CSS_SELECTOR, 'h2 span.a-text-normal')
PRODUCT_IMG = (By.CSS_SELECTOR, ".s-image[data-image-latency='s-product-image']")

@then('Verify search results is {expected_result}')
def verify_search_result(context, expected_result):
    context.app.search_result_page.verify_search_result(expected_result)



@when('Click on the fist product')
def click_on_the_product(context):
    context.driver.find_element(By.CSS_SELECTOR, '.a-link-normal.s-no-outline[href*="FWag-Salmon-Sweet-Potato-Recipe"]').click()


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    all_products = context.driver.find_elements(*SEARCH_RESULTS)

    for product in all_products:
        product_title = product.find_element(*PRODUCT_TITLE).text
        print(product_title)
        assert product_title, 'Product title not shown'
        product.find_element(*PRODUCT_IMG)
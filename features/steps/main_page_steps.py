from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
ORDERS_BTN = (By.ID, 'nav-orders')
CART_ICN = (By.CSS_SELECTOR, 'span.nav-cart-icon.nav-sprite')
FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterDescItem')
SIGNIN_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip .nav-action-signin-button')


@given('Open Amazon page')
def open_amazon(context):
    # context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main()


@when('Search for {product}')
def search_on_amazon(context, product):
    # context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    # context.driver.find_element(*SEARCH_BTN).click()
    context.app.header.search_product(product)


@when('Click orders')
def click_orders(context):
    # context.driver.find_element(*ORDERS_BTN).click()
    context.app.header.click_orders()


@when('Click on the cart icon')
def click_cart_icon(context):
    context.driver.find_element(*CART_ICN).click()


@when('Click on button from SignIn popup')
def click_signin_from_popup(context):
    # context.driver.wait.until(
    #     EC.element_to_be_clickable(SIGNIN_BTN),
    #     message='SignIn btn from popup not clickable'
    # ).click()
    context.app.header.click_signin_from_popup()


@when('Wait for 3 sec')
def wait_sec(context):
    sleep(3)


@when('Hover over language options')
def hover_lang(context):
    context.app.header.hover_lang()


@when('Select department by alias {dept}')
def select_dept(context, dept):
    context.app.header.select_dept(dept)


@then('Verify Sign In is clickable')
def verify_signin_btn_clickable(context):
    # context.driver.wait.until(
    #     EC.element_to_be_clickable(SIGNIN_BTN),
    #     message='SignIn btn from popup not clickable'
    # )
    context.app.header.verify_signin_btn_clickable()


@then('Verify Sign In disappears')
def verify_signin_btn_disappears(context):
    # context.driver.wait.until(
    #     EC.invisibility_of_element_located(SIGNIN_BTN),
    #     message='SignIn btn did not disappear'
    # )
    context.app.header.verify_signin_btn_disappears()


@then('Verify footer has {expected_amount} links')
def verify_link_amount(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*FOOTER_LINKS)
    assert len(links) == expected_amount, f'Expected {expected_amount} links but got {len(links)}'


@then('Verify many links are shown in the footer')
def verify_many_links(context):
    links = context.driver.find_elements(*FOOTER_LINKS)
    assert len(links) > 1


@then('Verify Spanish option present')
def verify_spanish_lang(context):
    context.app.header.verify_spanish_lang()


@then('Verify {dept} department is selected')
def verify_dept_selected(context, dept):
    context.app.header.verify_dept_selected(dept)
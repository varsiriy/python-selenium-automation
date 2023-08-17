from behave import given, when, then
from selenium.webdriver.common.by import By

LOWER_HEADER_LINKS = (By.CSS_SELECTOR, '#zg_header a')

@given('Open BestSellers page')
def open_bestsellers(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify lower header has {expected_amount} links')
def verify_link_amount(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*LOWER_HEADER_LINKS)
    assert len(links) == expected_amount, f'Expected {expected_amount} links but got {len(links)}'
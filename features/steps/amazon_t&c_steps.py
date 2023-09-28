from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

@given('Open Amazon T&C page')
def open_amazon_t_and_c(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/'
                       'ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')
    # sleep(2)
    # context.driver.refresh()


@when('Store original windows')
def store_original_windows(context):
    context.original_windows = context.app.amazon_t_and_c_page.store_original_windows()


@when('Click on Amazon Privacy Notice link')
def click_privacy_notice(context):
    context.app.amazon_t_and_c_page.click_privacy_notice()


@when('Switch to the newly opened window')
def switch_window(context):
    context.app.amazon_t_and_c_page.switch_to_new_window()
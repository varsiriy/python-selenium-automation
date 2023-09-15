from behave import given, when, then


@then('Verify Sign in page opened')
def verify_sign_in_page_opened(context):
    # actual_text = context.driver.find_element(*SIGNIN_HEADER).text
    # assert actual_text == 'Sign in', f'Expected Sign in but got {actual_text}'
    # # Verify email field present
    # context.driver.find_element(*EMAIL_INPUT)
    context.app.signin_page.verify_sign_in_page_opened()




from behave import given, when, then


@then('Verify Sign in page opened')
def verify_sign_in_page_opened(context):
    context.app.signin_page.verify_sign_in_page_opened()




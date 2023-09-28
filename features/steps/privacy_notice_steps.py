from behave import then


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_notice_opened(context):
    context.app.privacy_notice_page.verify_pn_opened()


@then('User can close new window and switch back to original')
def close_and_switch_back(context):
    context.app.privacy_notice_page.close_page()
    context.app.privacy_notice_page.switch_to_window(context.original_window)
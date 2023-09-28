from selenium.webdriver.common.by import By

from pages.base_page import Page


class TermsAndConditionsPage(Page):
    PRIVACY_NOTICE = (By.CSS_SELECTOR, 'a[href*="www.amazon.com/privacy"')

    def store_original_windows(self):
        return self.get_current_window()

    def click_privacy_notice(self):
        self.click(*self.PRIVACY_NOTICE)
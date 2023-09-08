from selenium.webdriver.common.by import By
from pages.base_page import Page

class SearchResultPage(Page):
    SEARCH_RESULT = (By.CSS_SELECTOR, '.a-color-state.a-text-bold')
    FIRST_PRODUCT = (By.CSS_SELECTOR, 'div[data-asin] a.a-link-normal')

    def verify_search_result(self, result):
        self.verify_text(result, *self.SEARCH_RESULT)

    def click_on_the_product(self):
        self.click(*self.FIRST_PRODUCT)
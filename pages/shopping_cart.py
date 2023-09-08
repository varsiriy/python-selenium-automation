from selenium.webdriver.common.by import By
from pages.base_page import Page

class ShoppingCart(Page):
    CART_EMPTY = (By.CSS_SELECTOR, '.a-row.sc-your-amazon-cart-is-empty')

    def verify_amazon_card_empty(self):
        self.verify_text('Your Amazon Cart is empty', *self.CART_EMPTY)

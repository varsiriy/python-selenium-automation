from selenium.webdriver.common.by import By
from pages.base_page import Page

class ShoppingCart(Page):
    CART_EMPTY = (By.CSS_SELECTOR, '.a-row.sc-your-amazon-cart-is-empty')
    ADDED_TO_CART = (By.CSS_SELECTOR, 'span.a-size-medium-plus')
    CART = (By.ID, 'nav-cart-count')
    PRODUCT_NAME = (By.CSS_SELECTOR, "#sc-active-cart li")

    def open_shopping_cart(self):
        self.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')

    def verify_amazon_card_empty(self):
        self.verify_text('Your Amazon Cart is empty', *self.CART_EMPTY)

    def verify_product_added_to_cart(self):
        self.verify_text('Added to Cart', *self.ADDED_TO_CART)

    def verify_cart_has_correct_count(self, expected_text):
        self.verify_text(expected_text, *self.CART)

    # def verify_cart_has_correct_product(self, expected_text):
    #    self.verify_text(expected_text, *self.PRODUCT_NAME)

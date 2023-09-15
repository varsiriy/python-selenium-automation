from selenium.webdriver.common.by import By
from pages.base_page import Page

class ProductPage(Page):
    FIRST_PRODUCT_NAME = (By.ID, 'productTitle')
    ADD_TO_CART_BTN = (By.ID, "add-to-cart-button")


    def product_name(self,expected_text):
        self.verify_text(expected_text,*self.FIRST_PRODUCT_NAME)

    def click_add_to_cart_btn(self):
        self.click(*self.ADD_TO_CART_BTN)


from selenium.webdriver.common.by import By
from pages.base_page import Page

class ProductPage(Page):
    FIRST_PRODUCT_NAME = (By.ID, 'productTitle')
    ADD_TO_CART_BTN = (By.ID, "add-to-cart-button")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#sc-active-cart li")


 #   def product_name(self,expected_text):
 #       self.verify_text(expected_text,*self.FIRST_PRODUCT_NAME)

    def product_name(self):
        global expected_text
        expected_text = self.find_element(*self.FIRST_PRODUCT_NAME).text
        print(expected_text)

    def click_add_to_cart_btn(self):
        self.click(*self.ADD_TO_CART_BTN)


    def verify_cart_has_correct_product(self):
        self.verify_text(expected_text, *self.PRODUCT_NAME)

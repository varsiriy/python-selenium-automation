from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page

class ProductPage(Page):
    FIRST_PRODUCT_NAME = (By.ID, 'productTitle')
    ADD_TO_CART_BTN = (By.ID, "add-to-cart-button")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#sc-active-cart li")
    NEW_ARRIVALS = (By.CSS_SELECTOR, '#nav-subnav [href*="New-Arrivals"]')
    WOMEN_CATEGORY = (By.CSS_SELECTOR, 'a.mm-merch-panel[href*="/s?i=fashion-womens"]')


 #   def product_name(self,expected_text):
 #       self.verify_text(expected_text,*self.FIRST_PRODUCT_NAME)

    def product_name(self):
        global expected_text
        expected_text = self.find_element(*self.FIRST_PRODUCT_NAME).text
        print(expected_text)

    def click_add_to_cart_btn(self):
        self.click(*self.ADD_TO_CART_BTN)

    def hover_new_arrivals(self):
        actions = ActionChains(self.driver)
        new_arrivals = self.find_element(*self.NEW_ARRIVALS)
        actions.move_to_element(new_arrivals)
        actions.perform()

    def verify_cart_has_correct_product(self):
        self.verify_text(expected_text, *self.PRODUCT_NAME)

    def verify_deals(self):
        self.wait_for_element_appear(*self. WOMEN_CATEGORY)

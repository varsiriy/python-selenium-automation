from selenium.webdriver.common.by import By
from pages.base_page import Page

class ProductPage(Page):
    PRODUCT_NAME = (By.ID, 'title')


    def get_product_name(self):
        self


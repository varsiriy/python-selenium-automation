from pages.main_page import MainPage
from pages.header import Header
from pages.search_result_page import SearchResultPage
from pages.signin_page import SignInPage
from pages.shopping_cart import ShoppingCart
from pages.product_page import ProductPage

class Application:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_result_page = SearchResultPage(driver)
        self.signin_page = SignInPage(driver)
        self.shopping_cart = ShoppingCart(driver)
        self.product_page = ProductPage(driver)


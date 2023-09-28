from pages.main_page import MainPage
from pages.blog import BlogPage
from pages.not_found_page import NotFoundPage
from pages.header import Header
from pages.search_result_page import SearchResultPage
from pages.signin_page import SignInPage
from pages.shopping_cart import ShoppingCart
from pages.product_page import ProductPage
from pages.bestsellers_page import BestsellersPage
from pages.amazon_t_and_c_page import TermsAndConditionsPage
from pages.privacy_notice_page import PrivacyNoticePage

class Application:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.blog = BlogPage(driver)
        self.not_found_page = NotFoundPage(driver)
        self.header = Header(driver)
        self.search_result_page = SearchResultPage(driver)
        self.signin_page = SignInPage(driver)
        self.shopping_cart = ShoppingCart(driver)
        self.product_page = ProductPage(driver)
        self.bestsellers_page = BestsellersPage(driver)
        self.amazon_t_and_c_page = TermsAndConditionsPage(driver)
        self.privacy_notice_page = PrivacyNoticePage


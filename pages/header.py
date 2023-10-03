from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from pages.base_page import Page

class Header(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    ORDERS_BTN = (By.ID, 'nav-orders')
    SIGNIN_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip .nav-action-signin-button')
    LANG_SELECTION = (By.CSS_SELECTOR, ".icp-nav-flag-us")
    SPANISH_LANG = (By.CSS_SELECTOR, '#nav-flyout-icp [href="#switch-lang=es_US"]')
    DEPT_SELECTION = (By.ID, 'searchDropdownBox')
    SUBHEADER_DEPT = (By.CSS_SELECTOR, '#nav-subnav[data-category="{SUB_STR}"]')  # [0, 1]

    # creating DYNAMIC locator
    def get_subheader_dept_locator(self, dept):
        # return SUBHEADER_DEPT with "{SUB_STR}" replaced => dept
        # return [By.CSS_SELLECTOR, "#nav-subnav[data-category='books']"]
        return [self.SUBHEADER_DEPT[0], self.SUBHEADER_DEPT[1].replace('{SUB_STR}', dept)]

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)

    def click_orders(self):
        self.click(*self.ORDERS_BTN)

    def click_signin_from_popup(self):
        self.wait_for_element_clickable_click(*self. SIGNIN_BTN)

    def hover_lang(self):
        actions = ActionChains(self.driver)
        lang = self.find_element(*self.LANG_SELECTION)
        actions.move_to_element(lang)
        actions.perform()

    def select_dept(self, dept):
        dept_selection = self.find_element(*self.DEPT_SELECTION)
        select = Select(dept_selection)
        select.select_by_value(f'search-alias={dept}')

    def verify_signin_btn_clickable(self):
        self.wait_for_element_clickable(*self. SIGNIN_BTN)

    def verify_signin_btn_disappears(self):
        self.wait_for_element_disappear(*self. SIGNIN_BTN)

    def verify_spanish_lang(self):
        self.wait_for_element_appear(*self. SPANISH_LANG)

    def verify_dept_selected(self, dept):
        # self.wait_for_element_appear(*self. SUBHEADER_DEPT)

        subheader_locator = self.get_subheader_dept_locator(dept)
        self.wait_for_element_appear(*subheader_locator)

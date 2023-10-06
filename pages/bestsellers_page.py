from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class BestsellersPage(Page):
    TOP_LINKS = (By.CSS_SELECTOR, '#zg_header a')
    HEADER = (By.CSS_SELECTOR, '#zg_banner_text')

    def open_bestsellers(self):
        # self.driver.get('https://www.amazon.com/gp/bestsellers/')
        # sleep(2)
        # self.driver.refresh()
        self.open_url('gp/bestsellers/')

    def click_thru_top_links(self):
        top_links = self.find_elements(*self.TOP_LINKS)

        for i in range(len(top_links)):  #0, 1, 2, 3, 4
            link_to_click = self.find_elements(*self.TOP_LINKS)[i]
            link_text = link_to_click.text
            link_to_click.click()
            self.verify_partial_text(link_text, *self.HEADER)
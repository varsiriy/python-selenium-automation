from pages.base_page import Page


class PrivacyNoticePage(Page):

    def verify_pn_opened(self):
        self.verify_partial_url('www.amazon.com/gp/help/customer/')
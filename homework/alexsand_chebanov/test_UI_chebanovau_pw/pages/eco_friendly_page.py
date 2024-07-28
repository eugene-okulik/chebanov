from .base_page import BasePage
from .locators import eco_friendly_locators as loc


class EcoPage(BasePage):
    page_url = '/collections/eco-friendly.html'

    def check_page_header_title_is(self, text):
        assert self.find(loc.header_title_loc).text_content()[1:-1] == text

    def check_item_category(self, text):
        assert self.find(loc.item_category_loc).text_content() == text

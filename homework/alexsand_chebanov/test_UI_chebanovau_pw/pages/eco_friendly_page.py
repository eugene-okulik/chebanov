from .base_page import BasePage
from .locators import eco_friendly_locators as loc
from playwright.sync_api import expect


class EcoPage(BasePage):
    page_url = '/collections/eco-friendly.html'

    def check_page_header_title_is(self, text):
        expect(self.find(loc.header_title_loc)).to_have_text(text)

    def check_item_category(self, text):
        expect(self.find(loc.item_category_loc)).to_have_text(text)

from playwright.sync_api import BrowserContext
import pytest
from pages.sale_page import SalePage
from pages.customer_login import CustomerLogin
from pages.eco_friendly_page import EcoPage


@pytest.fixture()
def page(context: BrowserContext, playwright):
    playwright.selectors.set_test_id_attribute("id")
    page = context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    return page


@pytest.fixture()
def sale_page(page):
    return SalePage(page)


@pytest.fixture()
def login_page(page):
    return CustomerLogin(page)


@pytest.fixture()
def eco_page(page):
    return EcoPage(page)

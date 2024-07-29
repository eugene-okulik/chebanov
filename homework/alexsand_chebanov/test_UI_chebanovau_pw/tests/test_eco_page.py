
def test_header_title(eco_page):
    eco_page.open_page()
    eco_page.check_page_header_title_is('Eco Friendly')


def test_current_url(eco_page):
    eco_page.open_page()
    eco_page.get_current_url("https://magento.softwaretestingboard.com/collections/eco-friendly.html")


def test_check_item_title(eco_page):
    eco_page.open_page()
    eco_page.check_item_category("Eco Friendly")

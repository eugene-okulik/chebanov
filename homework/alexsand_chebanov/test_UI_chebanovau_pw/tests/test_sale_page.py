

def test_header_title(sale_page):
    sale_page.open_page()
    sale_page.check_page_header_title_is('Sale')


def test_current_url(sale_page):
    sale_page.open_page()
    sale_page.get_current_url("https://magento.softwaretestingboard.com/sale.html")


def test_chak_item_category(sale_page):
    sale_page.open_page()
    sale_page.check_item_category("Sale")

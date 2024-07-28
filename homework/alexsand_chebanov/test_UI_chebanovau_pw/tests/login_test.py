

def test_correct_login(login_page):
    login_page.open_page()
    login_page.fill_login_form()
    login_page.check_alert_text("Thank you for registering with Main Website Store.")


def test_busy_mail(login_page):
    login_page.open_page()
    login_page.busy_mail("chebanov.al23@yandex.ru")
    login_page.check_error_alert_text_is(
        "There is already an account with this email address. "
        "If you are sure that it is your email address, click here to get your password and access your account."
    )


def test_current_url(login_page):
    login_page.open_page()
    login_page.get_current_url("https://magento.softwaretestingboard.com/customer/account/create/")

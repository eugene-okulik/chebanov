from playwright.sync_api import expect
from .base_page import BasePage
from .locators import login_locators as loc
from faker import Faker


class CustomerLogin(BasePage):
    page_url = '/customer/account/create/'

    def fill_login_form(self):
        faker = Faker("en_US")
        password = faker.password()
        first_name = self.find(loc.first_name_loc)
        last_name = self.find(loc.last_name_loc)
        email_field = self.find(loc.email_field_loc)
        password_field = self.find(loc.password_field_loc)
        password_confirm = self.find(loc.password_confirm_loc)
        button_create = self.find(loc.button_create_an_account_loc)
        first_name.fill(faker.first_name())
        last_name.fill(faker.last_name())
        email_field.fill(faker.email())
        password_field.fill(password)
        password_confirm.fill(password)
        button_create.click()

    def check_alert_text(self, text):
        expect(self.find(loc.error_locator_loc)).to_have_text(text)

    def busy_mail(self, email):
        faker = Faker("en_US")
        password = faker.password()
        first_name = self.find(loc.first_name_loc)
        last_name = self.find(loc.last_name_loc)
        email_field = self.find(loc.email_field_loc)
        password_field = self.find(loc.password_field_loc)
        password_confirm = self.find(loc.password_confirm_loc)
        button_create = self.find(loc.button_create_an_account_loc)
        first_name.fill(faker.first_name())
        last_name.fill(faker.last_name())
        email_field.fill(email)
        password_field.fill(password)
        password_confirm.fill(password)
        button_create.click()

    def check_error_alert_text_is(self, text):
        expect(self.find(loc.error_locator_loc)).to_have_text(text)

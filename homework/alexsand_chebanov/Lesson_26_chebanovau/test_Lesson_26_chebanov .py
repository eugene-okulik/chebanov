from playwright.sync_api import Page, expect


def test_one(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    search_field = page.get_by_role("link", name="Form Authentication")
    search_field.click()
    user_name = page.get_by_role('textbox', name="username")
    user_name.fill('tomsmith')
    password = page.get_by_role('textbox', name="password")
    password.fill('SuperSecretPassword!')
    submit = page.get_by_role("button", name=" Login")
    submit.click()
    expected_text = "Welcome to the Secure Area. When you are done click logout below."
    locator_text = page.locator("#content > div > h4")
    expect(locator_text).to_contain_text(expected_text)


def test_two(page: Page):
    page.goto('https://demoqa.com/automation-practice-form', timeout=837000)

    first_name = page.locator('#firstName')
    first_name.fill("Alex")

    last_name = page.locator('//*[@id="lastName"]')
    last_name.fill("Alexsandrovich")

    email = page.locator('//*[@id="userEmail"]')
    email.fill("name@mail.ru")

    gender = page.locator('//*[text()="Other"]')
    gender.click()

    mobile = page.locator('//*[@id="userNumber"]')
    mobile.fill("9379992985")

    subjects = page.locator('#subjectsInput')
    subjects.fill("English")
    subjects.press("Enter")

    hobbies = page.locator('label.custom-control-label[for="hobbies-checkbox-3"]')
    hobbies.click()

    current_address = page.locator('//*[@id="currentAddress"]')
    current_address.fill("Russian,Moscow,Pertovka 38")

    state_adn_city_1 = page.locator('#react-select-3-input')
    state_adn_city_1.fill("NCR")
    state_adn_city_1.press("Enter")

    state_adn_city_2 = page.locator('#react-select-4-input')
    state_adn_city_2.fill("Noida")
    state_adn_city_2.press("Enter")

    submit_button = page.locator("#submit")
    submit_button.click()

    expected_text = "Thanks for submitting the form"
    locator_text = page.locator("#example-modal-sizes-title-lg")
    expect(locator_text).to_contain_text(expected_text)

    close_modal = page.locator('#closeLargeModal')
    close_modal.click()

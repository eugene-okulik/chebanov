from playwright.sync_api import Page, expect, Dialog, BrowserContext


def test_one(page: Page):
    def canal_alert(alert: Dialog):
        alert.accept()

    page.on("dialog", canal_alert)

    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.locator(".a-button").click()

    expected_text = "You selected\n\nOk"
    locator_text = page.locator("#result")

    expect(locator_text).to_contain_text(expected_text)


def test_two(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    page.locator("#new-page-button").click()
    with context.expect_page() as new_page_event:
        new_page = new_page_event.value
        result = new_page.locator('#result-text')
        expect(result).to_have_text('I am a new page in a new tab')
        expect(page.locator("#new-page-button")).to_be_enabled()


def test_three(page: Page):
    page.goto('https://demoqa.com/dynamic-properties', timeout=83701)
    button = page.locator("#colorChange")
    red = "rgb(220, 53, 69)"
    expect(button).to_have_css("color", red)
    button.click()
    expect(button).to_be_enabled()

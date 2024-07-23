import re
import json


from playwright.sync_api import Page, Route, expect


def test_change_request(page: Page):
    new_header = 'яблокофон 15 про'

    def change_response(route: Route):
        response = route.fetch()
        body = response.json()
        body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = new_header
        body = json.dumps(body)
        route.fulfill(
            response=response,
            body=body
        )
    page.route(re.compile('library/step0_iphone/digitalmat'), change_response)
    page.goto('https://www.apple.com/shop/buy-iphone')
    btn_iphone = page.get_by_role("heading", name="iPhone 15 Pro & iPhone 15 Pro")
    btn_iphone.click()
    header = page.get_by_role("heading", name=new_header)
    expect(header).to_have_text(new_header)

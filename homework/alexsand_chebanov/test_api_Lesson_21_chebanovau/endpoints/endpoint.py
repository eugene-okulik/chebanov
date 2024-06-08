import allure
from test_api_Lesson_21_chebanovau.scr.global_enums import GlobalErrorMessages


class Endpoint:
    url = 'https://api.restful-api.dev/objects'
    response = None
    json = None

    @allure.step('Check that response is 200')
    def check_that_status_is_200(self):
        assert self.response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value

    def check_response_name_is_correct(self, name):
        assert self.json["name"] == name, GlobalErrorMessages.WRONG_NAME.value

import allure
from test_api_final_Lesson_23_chebanovau.scr.global_enums import GlobalErrorMessages


class Endpoint:
    url = 'http://167.172.172.115:52355'
    response = None
    json = None
    headers = {'Authorization': None}
    meme_id = None

    @allure.step("Проверка схемы")
    def validate_schema(self, schema):
        """Метод валидации ответа по схеме"""
        if isinstance(self.response.json(), list):
            for item in self.response.json():
                schema(item)
            else:
                schema(self.response.json())
            return self

    @allure.step('Check that id is equal to expected')
    def check_response_id_is_correct(self, meme_id):
        """ Проверка ID"""
        assert self.json['id'] == meme_id, GlobalErrorMessages.WRONG_ID.value

    @allure.step('Check that response is 200')
    def check_that_status_is_200(self):
        assert self.response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value

    @allure.step('Check that response is 400')
    def check_that_status_is_400(self):
        assert self.response.status_code == 400, GlobalErrorMessages.WRONG_STATUS_CODE.value

    @allure.step('Check that response is 401')
    def check_that_status_is_401(self):
        assert self.response.status_code == 401, GlobalErrorMessages.WRONG_STATUS_CODE.value

    @allure.step('Check that response is 403')
    def check_that_status_is_403(self):
        assert self.response.status_code == 403, GlobalErrorMessages.WRONG_STATUS_CODE.value

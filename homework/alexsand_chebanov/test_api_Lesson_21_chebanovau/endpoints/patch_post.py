import requests
import allure
from test_api_Lesson_21_chebanovau.endpoints.endpoint import Endpoint


class PatchPost(Endpoint):
    @allure.step("Частичное обновление объекта")
    def path_changes_in_post(self, post_id, body):
        self.response = requests.put(
            url=f'{self.url}/{post_id}',
            json=body
        )
        self.json = self.response.json()
        return self.response

    def check_response_name_is_correct(self, name):
        assert self.json["name"] == name

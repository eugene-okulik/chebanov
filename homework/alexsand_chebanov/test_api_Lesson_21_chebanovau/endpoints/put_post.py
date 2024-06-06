import requests
import allure

from test_api_Lesson_21_chebanovau.endpoints.endpoint import Endpoint


class UpdatePost(Endpoint):
    @allure.step("Обновление объекта")
    def make_changes_in_post(self, post_id, body):
        self.response = requests.put(
            url=f'{self.url}/{post_id}',
            json=body
        )
        self.json = self.response.json()
        return self.response

    def check_response_color_is_correct(self, color):
        assert self.json["data"]["color"] == color

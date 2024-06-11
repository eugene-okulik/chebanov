import requests
import allure

from test_api_Lesson_21_chebanovau.endpoints.endpoint import Endpoint


class UpdatePost(Endpoint):
    @allure.step("Обновление объекта")
    def make_changes_in_post(self, obj_id, body):
        self.response = requests.put(
            f'{self.url}/{obj_id}',
            json=body
        )
        self.json = self.response.json()
        return self.response

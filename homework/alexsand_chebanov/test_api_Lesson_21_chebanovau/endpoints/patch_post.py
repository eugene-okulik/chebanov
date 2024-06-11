import requests
import allure
from test_api_Lesson_21_chebanovau.endpoints.endpoint import Endpoint


class PatchPost(Endpoint):
    @allure.step("Частичное обновление объекта")
    def path_changes_in_post(self, obj_id, body):
        self.response = requests.patch(
            url=f'{self.url}/{obj_id}',
            json=body
        )
        self.json = self.response.json()
        return self.response

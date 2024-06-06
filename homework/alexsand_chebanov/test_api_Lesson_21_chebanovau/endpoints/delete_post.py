import allure
import requests
from test_api_Lesson_21_chebanovau.endpoints.endpoint import Endpoint


class DeletePost(Endpoint):
    @allure.step("Удаление объекта")
    def delite_a_delite(self, post_id, body):
        self.response = requests.delete(
            url=f'{self.url}/{post_id}',
            json=body
        )
        self.json = self.response.json()
        return self.response

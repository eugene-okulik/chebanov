import allure
import requests
from test_api_final_Lesson_23_chebanovau.endpoints.endpoint import Endpoint


class DeletePost(Endpoint):
    @allure.step("Удаление объекта")
    def delite_a_delite(self, mem_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(
            url=f'{self.url}/meme/{mem_id}',
            json=body,
            headers=headers
        )
        try:
            self.json = self.response.json()
            return self.response
        except requests.exceptions.JSONDecodeError:
            return None

    @allure.step("Удаление объекта")
    def delite_no_object(self, value, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(
            f'{self.url}/{value}',
            json=body,
            headers=headers
        )
        try:
            self.json = self.response.json()
            return self.response
        except requests.exceptions.JSONDecodeError:
            return None

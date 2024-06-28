import requests
import allure

from test_api_final_Lesson_23_chebanovau.endpoints.endpoint import Endpoint


class UpdatePost(Endpoint):
    @allure.step("Обновление объекта")
    def put_update_post(self, mem_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            url=f'{self.url}/meme/{mem_id}',
            json=body,
            headers=headers
        )
        try:
            self.json = self.response.json()
            return self.response
        except requests.exceptions.JSONDecodeError:
            return None

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

    def check_response_delete(self, mem_id):
        assert self.response.text == f"Meme with id {mem_id} successfully deleted"

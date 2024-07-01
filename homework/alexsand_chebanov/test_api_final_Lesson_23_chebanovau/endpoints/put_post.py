import requests
import allure
from test_api_final_Lesson_23_chebanovau.scr.global_enums import GlobalErrorMessages
from test_api_final_Lesson_23_chebanovau.endpoints.endpoint import Endpoint


class UpdatePost(Endpoint):
    @allure.step("Обновление объекта")
    def put_update_meme(self, mem_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            url=f'{self.url}/meme/{mem_id}',
            json=body,
            headers=headers
        )
        try:
            self.json = self.response.json()
            self.meme_id = self.json['id']
            return self.response
        except requests.exceptions.JSONDecodeError:
            return None

    def check_response_info_rating(self, rating):
        assert self.json["info"]["rating"] == rating, GlobalErrorMessages.WRONG_NAME.value

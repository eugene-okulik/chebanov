import requests
import allure
from test_api_Lesson_21_chebanovau.endpoints.endpoint import Endpoint


class CreatePost(Endpoint):
    def __init__(self):
        self.post_id = None

    @allure.step('Создание объекта')
    def create_new_post(self, body):
        self.response = requests.post(
            self.url,
            json=body,
        )
        self.json = self.response.json()
        self.post_id = self.json['id']
        return self.response

import requests
import allure
from test_api_final_Lesson_23_chebanovau.endpoints.endpoint import Endpoint


class GetPost(Endpoint):

    @allure.step('Get all posts')
    def get_all_meme(self, headers=None):
        """ Метод получения всех постов"""
        headers = headers if headers else self.headers
        self.response = requests.get(
            url=f'{self.url}/meme',
            headers=headers
        )
        try:
            self.json = self.response.json()
            return self.response
        except requests.exceptions.JSONDecodeError:
            return None

    """"Запрос одного мема"""

    @allure.step('Запрос мема по ID')
    def get_one_meme(self, mem_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            url=f'{self.url}/meme/{mem_id}',
            headers=headers
        )
        self.json = self.response.json()
        self.meme_id = self.json['id']
        return self.response

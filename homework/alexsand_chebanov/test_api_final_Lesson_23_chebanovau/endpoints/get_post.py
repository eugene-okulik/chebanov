import requests
import allure
from test_api_final_Lesson_23_chebanovau.endpoints.endpoint import Endpoint


class GetPost(Endpoint):
    length = None

    @allure.step('Get all posts')
    def get_all_posts(self, headers=None):
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

import requests
import allure
from test_api_Lesson_21_chebanovau.endpoints.endpoint import Endpoint


class GetPost(Endpoint):
    length = None

    @allure.step('Get all posts')
    def get_all_posts(self):
        """ Метод получения всех постов"""
        self.response = requests.get(self.url)
        return self.response.json()

    @allure.step('Get a single post id')
    def get_single_post_id(self, obj_id):
        self.response = requests.get(
            f'{self.url}/{obj_id}',
        )
        self.json = self.response.json()
        return self.response

    @allure.step('Check that id is equal to expected')
    def check_response_id_is_correct(self, obj_id):
        assert self.json['id'] == obj_id

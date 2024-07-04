import allure
import requests
from bs4 import BeautifulSoup

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

    # def check_response_delete(self, mem_id):
    #     assert self.response.text == f"Meme with id {mem_id} successfully deleted"

    def check_response_delete(self, mem_id, headers=None):
        if self.response.status_code == 200:
            assert self.response.text == f"Meme with id {mem_id} successfully deleted"
            response_get = requests.get(url=f'{self.url}/meme/{mem_id}', headers=headers)
            html_content = response_get.text
            soup = BeautifulSoup(html_content, 'html.parser')
            assert soup.find('p').text == "The requested URL was not found on the server. If you entered the URL " \
                                          "manually please check your spelling and try again."
        elif self.response.status_code == 403:
            html_content_2 = self.response.text
            soup_2 = BeautifulSoup(html_content_2, 'html.parser')
            assert soup_2.find('p').text == "You are not the meme owner"
        else:
            print("Не верный запрос")
            print(self.response.text)
            print(self.response.status_code)

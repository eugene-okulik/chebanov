import allure


class Endpoint:
    url = 'https://api.restful-api.dev/objects'
    response = None
    json = None

    @allure.step("Проверка статус кода 200")
    def status_code(self):
        assert self.response.status_code == 200

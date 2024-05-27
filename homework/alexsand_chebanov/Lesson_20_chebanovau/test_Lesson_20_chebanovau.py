import requests
import pytest
import allure


@pytest.fixture(scope='session', autouse=True)
def session_start():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.fixture(autouse=True)
def before_test():
    print("before test")
    yield
    print("after test")


@allure.title("Создание объекта")
@allure.feature("Создание объекта")
@pytest.mark.xfail
def test_2_post_a_post(before_test):
    with allure.step('Создание объекта'):
        url = 'https://api.restful-api.dev/objects'
        body = {
            "name": "Apple MacBook Pro 0",
            "data": {
                "year": 19,
                "price": 9999.99,
                "CPU model": "Baikal",
                "Hard disk size": "10 TB"
            }
        }
        response = requests.post(
            url,
            json=body,

        )
        value_id = response.json()["id"]
        print(value_id)
    with allure.step("Проверка создался ли объект"):
        assert response.status_code == 200
    yield value_id
    requests.delete(f'https://api.restful-api.dev/objects/{value_id}')


print("Создание прошло успешно ")


@allure.title("Запрос на потверждение создания объекта")
def test_get_a_get(test_post_a_post, before_test):
    with allure.step("Запрос на созданного объекта"):
        response = requests.get(f'https://api.restful-api.dev/objects/{test_post_a_post}')
    with allure.step('Проверка созданного объекта'):
        assert response.json()['id'] == test_post_a_post


@allure.title("Обновление объекта")
@allure.story("Обновление объекта")
@pytest.mark.medium
def test_put_a_put(test_post_a_post, before_test):
    with allure.step("Update value"):
        url = f'https://api.restful-api.dev/objects/{test_post_a_post}'
        body = {
            "name": "Apple MacBook Pro 16",
            "data": {
                "year": 2019,
                "price": 2049.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB",
                "color": "silver"
            }
        }

        response = requests.put(
            url,
            json=body,

        )

        value_color = response.json()
    with allure.step("Провоерка обновлений объекта "):
        assert response.status_code == 200
        assert value_color["data"]["color"] == 'silver'
    print("Обновление прошло успешно")


@allure.title("Частичное обновление объекта")
@allure.feature("New users")
@allure.story('Uptade users')
@pytest.mark.critical
def test_patch_a_patch(test_post_a_post, before_test):
    with allure.step('Частичное обновление объекта'):
        url = f'https://api.restful-api.dev/objects/{test_post_a_post}'
        body = {
            "name": "Apple MacBook Pro 999 (Updated Name)"
        }

        response = requests.patch(
            url,
            json=body,

        )

        value = response.json()
    with allure.step("Проверка обновления объекта"):
        assert response.status_code == 200
        assert value["name"] == "Apple MacBook Pro 999 (Updated Name)"
    print("Изминение прошло успешно")


@allure.title('Удаление объекта')
@allure.feature("Delite value")
def test_delite_a_delite(test_post_a_post, before_test):
    with allure.step("Создание запроса на удаление созданного значения"):
        url = f'https://api.restful-api.dev/objects/{test_post_a_post}'

        response = requests.delete(
            url
        )

        value = response.json()
    with allure.step("Проверка удаления объекта"):
        assert response.status_code == 200
        assert value["message"] == f"Object with id = {test_post_a_post} has been deleted."
    print("Удаление прошло успешно")


class Class_Worning:
    pass


@allure.title("Генерация множества юзеров")
@allure.feature("Generation users")  # фиктура для обозночения фичи
@pytest.mark.parametrize('body', [
    ({"name": "Apple MacBook Pro 16",
      "data": {"year": 1994, "price": 9999.99, "CPU model": "Baikal",
               "Hard disk size": "10 TB"}}),
    ({"name": "Apple MacBook Pro 17",
      "data": {"year": 1995, "price": 1000.99, "CPU model": "Baikal-1",
               "Hard disk size": "11 TB"}}),
    ({"name": "Apple MacBook Pro 18",
      "data": {"year": 1996, "price": 2000.99, "CPU model": "Baikal-2",
               "Hard disk size": "12 TB"}})
])
def test_post_and_post(before_test, body):
    url = 'https://api.restful-api.dev/objects'
    response = requests.post(
        url,
        json=body,

    )
    assert response.status_code == 200


def test_delite_post(test_post_a_post, before_test):
    url = f'https://api.restful-api.dev/objects/{test_post_a_post}'

    response = requests.delete(
        url
    )

    value = response.json()
    assert response.status_code == 200
    assert value["message"] == f"Object with id = {test_post_a_post} has been deleted."
    print("Удаление прошло успешно")

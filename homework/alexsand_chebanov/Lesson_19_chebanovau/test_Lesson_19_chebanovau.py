import requests
import pytest


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


@pytest.fixture()
def test_post_a_post(session_start, before_test):
    url = 'https://api.restful-api.dev/objects'
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 1994,
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
    assert response.status_code == 200
    yield value_id
    requests.delete(f'https://api.restful-api.dev/objects/{value_id}')


print(f"Создание прошло успешно ")


def test_get_a_get(test_post_a_post, before_test):
    response = requests.get(f'https://api.restful-api.dev/objects/{test_post_a_post}')
    assert response.json()['id'] == test_post_a_post


@pytest.mark.medium
def test_put_a_put(test_post_a_post, before_test):
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

    assert response.status_code == 200
    assert value_color["data"]["color"] == 'silver'
    print("Обновление прошло успешно")


@pytest.mark.critical
def test_patch_a_patch(test_post_a_post, before_test):
    url = f'https://api.restful-api.dev/objects/{test_post_a_post}'
    body = {
        "name": "Apple MacBook Pro 999 (Updated Name)"
    }

    response = requests.patch(
        url,
        json=body,

    )

    value = response.json()

    assert response.status_code == 200
    assert value["name"] == "Apple MacBook Pro 999 (Updated Name)"
    print("Изминение прошло успешно")


def test_delite_a_delite(test_post_a_post, before_test):
    url = f'https://api.restful-api.dev/objects/{test_post_a_post}'

    response = requests.delete(
        url
    )

    value = response.json()
    assert response.status_code == 200
    assert value["message"] == f"Object with id = {test_post_a_post} has been deleted."
    print("Удаление прошло успешно")


class Class_Worning:
    pass


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

import requests
import pytest


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


print("Создание прошло успешно ")
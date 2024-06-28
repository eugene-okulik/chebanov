import requests
import pytest
from test_api_final_Lesson_23_chebanovau.endpoints.create_post import CreatePost
from test_api_final_Lesson_23_chebanovau.endpoints.put_post import UpdatePost
from test_api_final_Lesson_23_chebanovau.endpoints.delete_post import DeletePost
from test_api_final_Lesson_23_chebanovau.endpoints.get_post import GetPost


@pytest.fixture()
def crete_post_endpoints():
    return CreatePost()


@pytest.fixture()
def update_post_endpoints():
    return UpdatePost()


@pytest.fixture()
def delete_post_endpoints():
    return DeletePost()


@pytest.fixture()
def get_post_endpoint():
    return GetPost()


@pytest.fixture()
def meme_id(token_post, crete_post_endpoints):
    body = {
        "text": "1",
        "url": "string",
        "tags": [
            "piu",
            "pi-piu"
        ],
        "info": {
            "fun": 2,
            "rating": 1
        }
    }
    crete_post_endpoints.create_new_post(body, token_post)
    yield crete_post_endpoints.response.json()['id']


@pytest.fixture()
def token_post():
    url = 'http://167.172.172.115:52355/authorize'
    body = {"name": "Chebanov_au"}

    response = requests.post(
        url,
        json=body,
    )
    token = response.json()["token"]
    assert response.status_code == 200
    return token

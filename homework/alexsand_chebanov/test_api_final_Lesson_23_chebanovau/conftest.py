import requests
import pytest
from test_api_final_Lesson_23_chebanovau.endpoints.create_post import CreatePost
from test_api_final_Lesson_23_chebanovau.endpoints.put_post import UpdatePost
from test_api_final_Lesson_23_chebanovau.endpoints.delete_post import DeletePost
from test_api_final_Lesson_23_chebanovau.endpoints.get_post import GetPost


@pytest.fixture()
def crete_meme_endpoints():
    return CreatePost()


@pytest.fixture()
def update_meme_endpoints():
    return UpdatePost()


@pytest.fixture()
def delete_meme_endpoints():
    return DeletePost()


@pytest.fixture()
def get_meme_endpoint():
    return GetPost()


@pytest.fixture()
def meme_id(token_post, crete_meme_endpoints):
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
    crete_meme_endpoints.create_new_meme(body, token_post)
    yield crete_meme_endpoints.response.json()['id']


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

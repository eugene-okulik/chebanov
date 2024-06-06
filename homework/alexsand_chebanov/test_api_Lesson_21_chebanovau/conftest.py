import pytest
from test_api_Lesson_21_chebanovau.endpoints.create_post import CreatePost
from test_api_Lesson_21_chebanovau.endpoints.put_post import UpdatePost
from test_api_Lesson_21_chebanovau.endpoints.delete_post import DeletePost
from test_api_Lesson_21_chebanovau.endpoints.patch_post import PatchPost


@pytest.fixture()
def crete_post_endpoints():
    return CreatePost()


@pytest.fixture()
def update_post_endpoints():
    return UpdatePost()


@pytest.fixture()
def path_post_endpoints():
    return PatchPost


@pytest.fixture()
def delete_post_endpoints():
    return DeletePost


@pytest.fixture()
def post_id(create_post_endpoint):
    body = {
        "name": "HOME-PC",
        "data": {
            "year": 2023,
            "price": 1600,
            "CPU model": " Intel Xeon E5 2650 v2 OEM ",
            "Hard disk size": "2 TB",
        }
    }
    create_post_endpoint.create_new_post(body)
    yield create_post_endpoint.post_id

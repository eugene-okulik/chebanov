from test_api_final_Lesson_23_chebanovau.scr.pydantic_schemas.valid_shema import MemeShema
import pytest

TEST_VALID = [
    ({"text": "string", "url": "string", "tags": ["piu", "pi-piu"], "info": {"fun": 2, "rating": 1}}),
    ({"text": "аываыва", "url": "ываываыв", "tags": ["piu", "pi-piu"], "info": {"fun": 5, "rating": 3}}),
    ({"text": "sfsdfsdf", "url": "sdfsdfsd", "tags": ["piu", "pi-piu"], "info": {"fun": 8, "rating": 8}})
]

TEST_INVALID_DATA = [
    ({"text": 3, "url": "string", "tags": ["piu", "pi-piu"], "info": {"fun": 2, "rating": 1}}),
    ({"text": False, "url": 123, "tags": ["piu", "pi-piu"], "info": {"fun": 5, "rating": 3}}),
    ({"text": [], "url": "sdfsdfsd", "tags": ["piu", "pi-piu"], "info": {"fun": 8, "rating": 8}})
]


@pytest.mark.parametrize("body", TEST_VALID)
def test_post_valid(crete_post_endpoints, token_post, body):
    crete_post_endpoints.create_new_post(body, token_post)
    crete_post_endpoints.check_that_status_is_200()
    crete_post_endpoints.validate_schema(MemeShema)


@pytest.mark.parametrize("body", TEST_INVALID_DATA, )
def test_post_invalid(crete_post_endpoints, token_post, body):
    crete_post_endpoints.create_new_post(body, token_post)
    crete_post_endpoints.check_that_status_is_400()


"""Обновление обьекта с прверкой что обновили элемент"""


def test_put_valid(update_post_endpoints, meme_id, token_post):
    body = {
        "id": meme_id,
        "text": "funny cat meme",
        "url": "https://s09.stc.yc.kpcdn.net/share/i/4/2235353/wr-750.webp",
        "tags": ["oputi", "niputy"],
        "info": {
            "cute": 1,
            "rating": 2
        }
    }

    update_post_endpoints.put_update_post(mem_id=meme_id, body=body, headers={'Authorization': f'{token_post}'})
    update_post_endpoints.validate_schema(MemeShema)
    update_post_endpoints.check_that_status_is_200()
    update_post_endpoints.check_response_id_is_correct(update_post_endpoints.response.json()['id'])
    update_post_endpoints.check_response_info_rating(2)


"""Обновление объекта с невалидными данными"""


def test_put_invalid(update_post_endpoints, meme_id, token_post):
    body = {
        "id": meme_id,
        "text": 2,
        "url": "https://s09.stc.yc.kpcdn.net/share/i/4/2235353/wr-750.webp",
        "tags": ["oputi", "niputy"],
        "info": {
            "cute": 1,
            "rating": 2
        }
    }

    update_post_endpoints.put_update_post(mem_id=meme_id, body=body, headers={'Authorization': f'{token_post}'})
    update_post_endpoints.check_that_status_is_400()


"""Обновление объекта без токена авторизации"""


def test_put_net_token(update_post_endpoints, meme_id):
    body = {
        "id": meme_id,
        "text": "funny cat meme",
        "url": "https://s09.stc.yc.kpcdn.net/share/i/4/2235353/wr-750.webp",
        "tags": ["oputi", "niputy"],
        "info": {
            "cute": 1,
            "rating": 2
        }
    }

    update_post_endpoints.put_update_post(mem_id=meme_id, body=body)
    update_post_endpoints.check_that_status_is_401()


"""Запрос всех мемов"""


def test_get_all_posts(get_post_endpoint, token_post):
    get_post_endpoint.get_all_posts(headers={'Authorization': f'{token_post}'})
    get_post_endpoint.validate_schema(MemeShema)
    get_post_endpoint.check_that_status_is_200()


"""Запрос мемов по айди"""


def test_getting_meme_by_id(get_post_endpoint, meme_id, token_post):
    get_post_endpoint.get_one_meme(mem_id=meme_id, headers={'Authorization': f'{token_post}'})
    get_post_endpoint.validate_schema(MemeShema)
    get_post_endpoint.check_response_id_is_correct(meme_id)
    get_post_endpoint.check_that_status_is_200()


"""Удаление поста"""


def test_delete_posts_valid(delete_post_endpoints, meme_id, token_post):
    body = {
        "id": meme_id,
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
    delete_post_endpoints.delite_a_delite(mem_id=meme_id, body=body, headers={'Authorization': f'{token_post}'})
    delete_post_endpoints.check_that_status_is_200()
    delete_post_endpoints.check_response_delete(mem_id=meme_id)


"""Удаление поста созданного другим пользователем"""


def test_delete_not_valid(delete_post_endpoints, token_post):
    delete_post_endpoints.delite_a_delite(mem_id=15, body=None, headers={'Authorization': f'{token_post}'})
    delete_post_endpoints.check_that_status_is_403()

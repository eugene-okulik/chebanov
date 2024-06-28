import allure
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
    with allure.step("Создание объекта"):
        crete_post_endpoints.create_new_post(body, token_post)
        crete_post_endpoints.check_that_status_is_200()
        print(crete_post_endpoints.post_id)


@pytest.mark.parametrize("body", TEST_INVALID_DATA, )
def test_post_invalid(crete_post_endpoints, token_post, body):
    crete_post_endpoints.create_new_post(body, token_post)
    crete_post_endpoints.check_that_status_is_400()
    print(crete_post_endpoints.response)


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
    print(update_post_endpoints.response.text)
    update_post_endpoints.check_that_status_is_200()
    update_post_endpoints.check_response_name_is_correct(2)


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
    print(update_post_endpoints.response.text)


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
    print(update_post_endpoints.response.text)


def test_get_all_posts(get_post_endpoint, token_post):
    get_post_endpoint.get_all_posts(headers={'Authorization': f'{token_post}'})
    get_post_endpoint.check_that_status_is_200()


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
    print(delete_post_endpoints.response.text)


def test_delete_posts_no_my_objekt(delete_post_endpoints, token_post):
    value = 15
    body = {
        "id": value,
        "info": {
            "fun": 2,
            "rating": 1
        },
        "tags": [
            "piu",
            "pi-piu"
        ],
        "text": "Piu-pau oy oy oy",
        "updated_by": "vkuklin",
        "url": "https://imgflip.com/i/8ngjno"
    }
    delete_post_endpoints.delite_no_object(value=value, body=body, headers={'Authorization': f'{token_post}'})
    delete_post_endpoints.check_that_status_is_403()
    print(delete_post_endpoints.response.text)

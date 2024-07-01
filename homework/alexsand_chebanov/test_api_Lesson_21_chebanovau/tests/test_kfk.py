import allure
import pytest

TEST_DATA = [
    ({"name": "Apple MacBook Pro 16",
      "data": {"year": 1994, "price": 9999.99, "CPU model": "Baikal",
               "Hard disk size": "10 TB"}}),
    ({"name": "Apple MacBook Pro 17",
      "data": {"year": 1995, "price": 1000.99, "CPU model": "Baikal-1",
               "Hard disk size": "11 TB"}}),
    ({"name": "Apple MacBook Pro 18",
      "data": {"year": 1996, "price": 2000.99, "CPU model": "Baikal-2",
               "Hard disk size": "12 TB"}})
]


@pytest.mark.parametrize("body", TEST_DATA)
def test_post_a_post(crete_meme_endpoints, body):
    with allure.step('Создание объекта'):
        crete_meme_endpoints.create_new_post(body)
        crete_meme_endpoints.check_that_status_is_200()
        crete_meme_endpoints.check_response_name_is_correct(body['name'])
        print(crete_meme_endpoints.post_id)


def test_put_a_put(update_meme_endpoints, post_id):
    body = {
        "name": "HOME-PC-12",
        "data": {
            "year": 2021,
            "price": 1610,
            "CPU model": " Intel Xeon E5 2650 v2 12OEM ",
            "Hard disk size": "21 TB",
        }
    }
    update_meme_endpoints.make_changes_in_post(post_id, body)
    update_meme_endpoints.check_that_status_is_200()
    update_meme_endpoints.check_response_name_is_correct("HOME-PC-12")
    print(update_meme_endpoints.make_changes_in_post)


def test_patch_a_patch(path_post_endpoints, post_id):
    body = {
        "name": "Apple MacBook Pro 999 (Updated Name)"
    }
    value = path_post_endpoints.check_that_status_is_200
    path_post_endpoints.path_changes_in_post(post_id, body)
    path_post_endpoints.check_response_name_is_correct("Apple MacBook Pro 999 (Updated Name)")
    path_post_endpoints.check_that_status_is_200()
    print(value)


def test_get_all_posts(get_post_endpoint):
    get_post_endpoint.get_all_posts()
    get_post_endpoint.check_that_status_is_200()


def test_get_single_post(get_post_endpoint, post_id):
    get_post_endpoint.get_single_post_id(post_id)
    get_post_endpoint.check_that_status_is_200()
    get_post_endpoint.check_response_id_is_correct(post_id)


def test_delete_posts(delete_post_endpoints, post_id):
    delete_post_endpoints.delite_a_delite(post_id)
    delete_post_endpoints.check_that_status_is_200()

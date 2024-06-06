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
def test_post_a_post(crete_post_endpoints, body):
    with allure.step('Создание объекта'):
        crete_post_endpoints.create_new_post(body)
        crete_post_endpoints.status_code()


print("Создание прошло успешно ")


def test_put_a_put(update_post_endpoints, post_id, crete_post_endpoints):
    with allure.step("Update value"):
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
        update_post_endpoints.make_changes_in_post(body, post_id)
        update_post_endpoints.status_code()
        update_post_endpoints.check_response_color_is_correct('silver')


print("Обновление прошло успешно")


def test_patch_a_patch(path_post_endpoints, post_id, crete_post_endpoints):
    with allure.step("Update value"):
        body = {
            "name": "Apple MacBook Pro 999 (Updated Name)"
        }

        path_post_endpoints.path_changes_in_post(body, post_id)
        path_post_endpoints.check_response_name_is_correct()
        path_post_endpoints.status_code()


print("Частичное обновление прошло успешно")


def test_delete_posts(delete_post_endpoints, post_id, crete_post_endpoints):
    delete_post_endpoints.delite_a_delite(post_id)
    delete_post_endpoints.status_code()

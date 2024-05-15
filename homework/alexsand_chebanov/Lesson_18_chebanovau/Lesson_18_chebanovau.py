import requests


def post_a_post():
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
    assert response.status_code == 200
    return value_id


print("Создание прошло успешно")

post_a_post()


def put_a_put():
    url = f'https://api.restful-api.dev/objects/{post_a_post()}'
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


put_a_put()


def patch_a_patch():
    url = f'https://api.restful-api.dev/objects/{post_a_post()}'
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


patch_a_patch()


def delite_a_delite():
    url = f'https://api.restful-api.dev/objects/{post_a_post()}'

    response = requests.delete(
        url
    )

    value = response.json()
    assert response.status_code == 200
    assert value["message"] == f"Object with id = {post_a_post()} has been deleted."
    print("Удаление прошло успешно")


delite_a_delite()

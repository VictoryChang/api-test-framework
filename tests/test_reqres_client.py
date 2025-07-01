from icecream import ic
import jsonschema

from tests.conftest import load_schema


def test_get_user(client):
    response = client.get_user(user_id=2)
    assert response.status_code == 200
    get_user_data = response.json()

    get_user_schema = load_schema("schemas/get_user.json")
    jsonschema.validate(get_user_data, get_user_schema)

    assert get_user_data["data"]["avatar"] == "https://reqres.in/img/faces/2-image.jpg"
    assert get_user_data["data"]["email"] == "janet.weaver@reqres.in"
    assert get_user_data["data"]["first_name"] == "Janet"
    assert get_user_data["data"]["id"] == 2
    assert get_user_data["data"]["last_name"] == "Weaver"


def test_list_user(client):
    response = client.list_users(page=2)
    assert response.status_code == 200
    list_user_data = response.json()

    list_user_schema = load_schema("schemas/list_users.json")
    jsonschema.validate(list_user_data, list_user_schema)

    assert list_user_data["page"] == 2
    assert list_user_data["per_page"] == 6
    assert list_user_data["total"] == 12
    assert list_user_data["total_pages"] == 2
    assert len(list_user_data["data"]) == 6
    assert list_user_data["data"][0] == {
        "id": 7,
        "email": "michael.lawson@reqres.in",
        "first_name": "Michael",
        "last_name": "Lawson",
        "avatar": "https://reqres.in/img/faces/7-image.jpg"
    }


def test_create_user(client):
    payload = {"name": "steven", "job": "architect"}
    response = client.create_user(payload)
    assert response.status_code == 201
    create_user_data = response.json()

    create_user_schema = load_schema("schemas/create_user.json")
    jsonschema.validate(create_user_data, create_user_schema)

    assert create_user_data["id"].isnumeric() and int(create_user_data["id"]) > 1
    assert create_user_data["name"] == payload["name"]
    assert create_user_data["job"] == payload["job"]


def test_update_user(client):
    payload = {"name": "steven", "job": "construction manager"}
    response = client.update_user(user_id=2, payload=payload)
    assert response.status_code == 200
    update_user_data = response.json()

    update_user_schema = load_schema("schemas/update_user.json")
    jsonschema.validate(update_user_data, update_user_schema)
    
    assert update_user_data["name"] == payload["name"]
    assert update_user_data["job"] == payload["job"]


def test_delete_user(client):
    response = client.delete_user(user_id=2)
    assert response.status_code == 204
    assert response.text == ''

import jsonschema

from tests.conftest import load_schema


def test_get_user(client):
    response = client.get_user(user_id=2)
    assert response.status_code == 200
    get_user_data = response.json()

    user_schema = load_schema("schemas/user.json")
    jsonschema.validate(get_user_data, user_schema)

    assert get_user_data["data"]["avatar"] == "https://reqres.in/img/faces/2-image.jpg"
    assert get_user_data["data"]["email"] == "janet.weaver@reqres.in"
    assert get_user_data["data"]["first_name"] == "Janet"
    assert get_user_data["data"]["id"] == 2
    assert get_user_data["data"]["last_name"] == "Weaver"


def test_list_user(client):
    response = client.list_users(page=2)
    assert response.status_code == 200


def test_create_user(client):
    request_body = {"name": "steven", "job": "architect"}
    response = client.create_user(request_body=request_body)
    assert response.status_code == 201


def test_update_user(client):
    request_body = {"name": "steven", "job": "construction manager"}
    response = client.update_user(user_id=2, request_body=request_body)
    assert response.status_code == 200


def test_delete_user(client):
    response = client.delete_user(user_id=2)
    assert response.status_code == 204
    assert response.text == ''

# API Test Framework

## Motivation
Create a Python API Test Framework, built with requests and pytest, that is simple to read, run, and extend.

## Design Pattern
Encapsulating an API into a "Client" helps make the client more extensible and the tests more readable.

Example Client:
```python
import os

from requests import Response
from requests_toolbelt.sessions import BaseUrlSession


class ReqResClient:
    def __init__(self):
        self.session = BaseUrlSession(base_url="https://reqres.in/")
        self.session.headers = {"x-api-key": os.environ["REQRES_API_KEY"]}

    def get_user(self, user_id: int) -> Response:
        return self.session.get(f"/api/users/{user_id}")

    def list_users(self, page: int) -> Response:
        return self.session.get("/api/users", params={"page": page})

    def create_user(self, payload: dict) -> Response:
        return self.session.post("/api/users", json=payload)

    def update_user(self, user_id: int, payload: dict) -> Response:
        return self.session.put(f"/api/users/{user_id}", json=payload)
    
    def delete_user(self, user_id: int) -> Response:
        return self.session.delete(f"/api/users/{user_id}")
```

Example Test Case:
```python
import jsonschema

from tests.conftest import load_schema


def test_get_user(client):
    response = client.get_user(user_id=2)

    # status code validation
    assert response.status_code == 200
    get_user_data = response.json()

    # schema validation
    get_user_schema = load_schema("schemas/get_user.json")
    jsonschema.validate(get_user_data, get_user_schema)

    # response validation
    assert get_user_data["data"]["avatar"] == "https://reqres.in/img/faces/2-image.jpg"
    assert get_user_data["data"]["email"] == "janet.weaver@reqres.in"
    assert get_user_data["data"]["first_name"] == "Janet"
    assert get_user_data["data"]["id"] == 2
    assert get_user_data["data"]["last_name"] == "Weaver"
```

## Running Test Cases
1. python -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. ./run_tests.sh

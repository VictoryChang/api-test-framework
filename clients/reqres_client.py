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

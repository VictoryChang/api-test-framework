from requests import Response
from requests_toolbelt.sessions import BaseUrlSession



class ReqResClient:
    def __init__(self):
        self.session = BaseUrlSession(base_url="https://reqres.in/")
        self.session.headers = {"x-api-key": "reqres-free-v1"}

    def get_user(self, user_id: int) -> Response:
        return self.session.get(f"/api/users/{user_id}")
    
    def list_users(self, page: int) -> Response:
        return self.session.get(f"/api/users", params={"page": page})
    
    def create_user(self, request_body: dict) -> Response:
        return self.session.post("/api/users", json=request_body)
    
    def update_user(self, user_id: int, request_body: dict) -> Response:
        return self.session.put(f"/api/users/{user_id}", json=request_body)

    def delete_user(self, user_id: int) -> Response:
        return self.session.delete(f"/api/users/{user_id}")

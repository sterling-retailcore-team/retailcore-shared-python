import os

from sterling_shared.services.base import BaseRequest


class AuthService(BaseRequest):
    base_url = None

    def __init__(self, request):
        super().__init__(request)
        base_url = f"{os.getenv('AUTH_SERVICE_URL', 'http://localhost:10050')}/api/v1"
        self.base_url = f"{base_url}"

    def get_user_by_id(self, id):
        path = f'users/{id}'
        return self.send_request("GET", path)

    def get_users_by_ids(self, ids: list, to_dict: bool = False):
        string_ids = ",".join(ids)
        path = f'users/fetch/by-id/?id={string_ids}'
        users = self.send_request("GET", path)
        if to_dict:
            return {x["id"]: x for x in users['data']}
        return users['data']

    def get_users_by_permissions(self, permissions: list, to_dict: bool = False):
        string_permissions = ",".join(permissions)
        path = f'users/fetch/by-permission/?permissions={string_permissions}'
        users = self.send_request("GET", path)
        if to_dict:
            return {x["id"]: x for x in users['data']}
        return users['data']

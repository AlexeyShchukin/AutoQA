import requests


class EmployeeApi:
    def __init__(self, url):
        self.url = url

    # def get_employee_list(self):
    #     resp = requests.get(f"{self.url}/employee/list")
    #     assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
    #     return resp.json()

    # def get_token(self, user, password):
    #     creds = {"username": user, "password": password}
    #     resp = requests.post(self.url + '/auth/login', json=creds)
    #     assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
    #     return resp.json()["user_token"]

    def create_employee(self, **kwargs):
        resp = requests.post(f"{self.url}/employee/create", json=kwargs)
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()

    def get_employee(self, employee_id):
        resp = requests.get(self.url + f'/employee/info/{employee_id}')
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()
    #
    # def update_employee(self, **kwargs):
    #     resp = requests.post(self.url + f'/employee/update', json=kwargs)
    #
    #     assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
    #     return resp.json()

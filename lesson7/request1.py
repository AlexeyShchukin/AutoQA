import requests

def test_simple_req():
    resp = requests.get('http://5.101.50.27:8000/company/list')
    assert resp.status_code == 200  # Проверяем, что сервер вернул статус 200 (OK)


def test_simple_req_2():
    resp = requests.get('http://5.101.50.27:8000/company/list')
    assert resp.status_code == 200  # Проверяем, что сервер вернул статус 200 (OK)
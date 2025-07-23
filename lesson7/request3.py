import requests

base_url ="http://5.101.50.27:8000"


def test_create_company():
    company = {
        "name": "python",
        "description": "requests"
    }
    resp = requests.post(base_url + '/company/create', json=company)

    assert resp.status_code == 201  # 201 означает, что компания успешно создана
    
import requests


def test_simple_req():
    resp = requests.post('http://5.101.50.27:8000/company/create')
    data = resp.json()
    assert resp.status_code == 422
    assert data['detail'][0]['msg'] == 'Field required'
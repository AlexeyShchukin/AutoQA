import json

import requests


def test_simple_req():
    resp = requests.get('http://5.101.50.27:8000/company/list')
    assert resp.status_code == 200
    obj = resp.json()
    # obj = json.loads(resp.text)
    l = []
    for d in obj:
        if d['is_active'] == True:
            l.append(d)

    assert len(l) >= 3


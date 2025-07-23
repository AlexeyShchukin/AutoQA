import json

company_json = """
{
    "id": 111,
    "isActive": true,
    "createDateTime": "2024-04-05T17:30:00.713Z",
    "lastChangedDateTime": "2024-04-05T17:30:00.713Z",
    "name": "Барбершоп 'Цирюльникъ'",  
    "description": "Крутые стрижки для крутых шишек"
}
"""

def test_parse_json():
    company = json.loads(company_json)  # Преобразуем JSON в словарь
    assert company["id"] == 111  # Проверяем значение ключа "id"
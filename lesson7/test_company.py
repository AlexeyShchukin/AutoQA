from company_api import CompanyApi  # Импортируем класс


def test_create_company_increases_count():
    """Тест: создание компании увеличивает список компаний на 1"""

    base_url = "http://5.101.50.27:8000"
    api = CompanyApi(base_url)  # Инициализация API-клиента
    # 1. Получаем текущий список компаний
    companies_before = api.get_company_list()
    initial_count = len(companies_before)

    # 2. Создаём новую компанию
    api.create_company(name="Test Company", description="Automated test creation")
    # 3. Повторно получаем список компаний
    companies_after = api.get_company_list()
    final_count = len(companies_after)

    # 4. Проверяем, что длина списка увеличилась на 1
    assert final_count == initial_count + 1, f"Ожидалось {initial_count + 1} компаний, найдено {final_count}"
    print(f"Тест пройден: до {initial_count}, после {final_count} (добавлена 1 компания).")


def test_get_one_company():
    base_url = "http://5.101.50.27:8000"
    api = CompanyApi(base_url)
    # Создаем компанию
    name = "PyCharm"
    descr = "IDE"
    result = api.create_company(name, descr)
    new_id = result["id"]
    # Обращаемся к компании
    new_company = api.get_company(new_id)
    # Проверим название, описание и статус новой компании:
    assert new_company["name"] == name
    assert new_company["description"] == descr
    assert new_company["is_active"] is True
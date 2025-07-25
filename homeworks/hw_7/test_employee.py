from homeworks.hw_7.employee_api import EmployeeApi

base_url = "http://5.101.50.27:8000"
api = EmployeeApi(base_url)


def test_create_employee():
    employee = api.create_employee(
        first_name="John",
        last_name="Doe",
        middle_name="Edward",
        company_id=1,
        email="johndoe@example.com",
        phone="+1234567890",
        birthdate="1990-01-15",
        is_active=True
    )

    assert employee["first_name"] == "John", f"Ожидалось 'John', получено '{employee['first_name']}'"
    assert employee["last_name"] == "Doe", f"Ожидалось 'Doe', получено '{employee['last_name']}'"
    assert employee["middle_name"] == "Edward", f"Ожидалось 'Edward', получено '{employee['middle_name']}'"
    assert employee["company_id"] == 1, f"Ожидалось 1, получено '{employee['company_id']}'"
    assert employee[
               "email"] == "johndoe@example.com", f"Ожидалось 'johndoe@example.com', получено '{employee['email']}'"
    assert employee["phone"] == "+1234567890", f"Ожидалось '+1234567890', получено '{employee['phone']}'"
    assert employee["birthdate"] == "1990-01-15", f"Ожидалось '1990-01-15', получено '{employee['birthdate']}'"
    assert employee["is_active"] is True, "Ожидалось, что сотрудник активен"

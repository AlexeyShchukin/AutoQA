# pip install pytest allure-pytest
# pytest --alluredir=allure-results - билдим тесты при любом изменении из текущей папки

# iwr -useb get.scoop.sh | iex  - установка scoop

# scoop install allure (on Windows)
# brew install allure (on MAC)

# allure serve allure-results - интерфейс

# allure generate allure-results -o allure-report --clean - генерирует папку с отчётом

import allure

from lesson8.booker_api import BookerApi

base_url = "https://restful-booker.herokuapp.com"
api = BookerApi(base_url)


@allure.epic("бронирование")
@allure.severity("blocker")
def test_get_token():
    resp = api.get_token("admin", "password123")
    assert resp["token"] != "", f"Токен пустой"


@allure.severity("minor")
def test_get_booking_ids():
    api.get_booking_ids()

# def test_get_booking_list():
#     resp = api.get_booking_list()
#     assert all(d.get("bookingig") for d in resp)

@allure.severity("critical")
def test_create_booking():
    with allure.step("создает ресурс брони"):
        booking = {
            "firstname": "Roman",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }
    with allure.step("создает бронь через API"):
        resp = api.create_booking(booking)
    with allure.step("проверяет создание брони"):
        assert resp["bookingid"] != "", "Нет id"


def test_get_booking():
    booking = {
        "firstname": "Jil",
        "lastname": "White",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    new_booking = api.create_booking(booking)
    booking_id = new_booking["bookingid"]

    resp = api.get_booking(booking_id)
    assert resp["firstname"] == "Jil"

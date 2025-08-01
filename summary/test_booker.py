import requests

from booker_api import BookerApi
import allure

base_url = "https://restful-booker.herokuapp.com"
api = BookerApi(base_url)


def test_authentication():
    api.authenticate()


def test_get_booking_ids():
    api.get_booking_ids()


def test_create_booking():
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
    resp = api.create_booking(booking)
    assert resp["bookingid"] != "", "Нет id"


def test_get_booking():
    booking = {
        "firstname": "Rom",
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
    assert resp["firstname"] == "Rom"


@allure.title("Update Booking")
@allure.severity("critical")
def test_update_booking():

    token = api.authenticate()


    booking = {
        "firstname": "Tom",
        "lastname": "Smith",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-01-01",
            "checkout": "2023-01-10"
        },
        "additionalneeds": "Dinner"
    }
    new_booking = api.create_booking(booking)
    booking_id = new_booking["bookingid"]


    updated_booking = {
        "firstname": "Tommy",
        "lastname": "Smith",
        "totalprice": 200,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2023-01-02",
            "checkout": "2023-01-12"
        },
        "additionalneeds": "Lunch"
    }

    updated_resp = api.update_booking(booking_id, updated_booking, token)

    with allure.step("Check that Booking is changed"):
        assert updated_resp["firstname"] == "Tommy", "Имя не обновилось"
        assert updated_resp["totalprice"] == 200, "Цена не обновилась"
        assert updated_resp["depositpaid"] is False, "Статус депозита не обновился"


@allure.title("Partial Update Booking")
@allure.severity("critical")
def test_patch_booking():
    token = api.authenticate()

    booking = {
        "firstname": "Anna",
        "lastname": "Taylor",
        "totalprice": 300,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-05-01",
            "checkout": "2023-05-10"
        },
        "additionalneeds": "Dinner"
    }
    new_booking = api.create_booking(booking)
    booking_id = new_booking["bookingid"]

    patch_data = {
        "firstname": "Anastasia",
        "lastname": "Ivanova"
    }

    patched_resp = api.patch_booking(booking_id, patch_data, token)

    with allure.step("Check that Booking is partially updated"):
        assert patched_resp["firstname"] == "Anastasia", "Имя не обновилось"
        assert patched_resp["lastname"] == "Ivanova", "Фамилия не обновилась"
        assert patched_resp["totalprice"] == 300, "Цена не должна была измениться"


def test_delete_booking():
    token = api.authenticate()

    booking = {
        "firstname": "DeleteMe",
        "lastname": "Now",
        "totalprice": 123,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2022-10-01",
            "checkout": "2022-10-05"
        },
        "additionalneeds": "None"
    }
    new_booking = api.create_booking(booking)
    booking_id = new_booking["bookingid"]

    result = api.delete_booking(booking_id, token)
    assert result is True, "Удаление не удалось"

    resp = requests.get(f"{api.url}/booking/{booking_id}")
    assert resp.status_code == 404, "Бронирование не удалено (ожидался 404)"

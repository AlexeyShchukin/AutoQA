from page_object_model.tests.base_test import BaseTest


class TestLogin(BaseTest):
    def test_successful_login(self):
        self.login_page.enter_username("standard_user")
        self.login_page.enter_password("secret_sauce")
        self.login_page.click_on_login_button()
        assert "inventory.html" in self.driver.current_url, "Не удалось войти в систему."

    def test_invalid_password(self):
        self.login_page.enter_username("standard_user")
        self.login_page.enter_password("wrong_password")
        self.login_page.click_on_login_button()
        assert "Username and password do not match" in self.login_page.error_message().text, "Неверное сообщение об ошибке."

    def test_locked_out_user(self):
        self.login_page.enter_username("locked_out_user")
        self.login_page.enter_password("secret_sauce")
        self.login_page.click_on_login_button()
        assert "Sorry, this user has been locked out." in self.login_page.error_message().text, "Неверное сообщение об ошибке."

    def test_empty_username(self):
        self.login_page.enter_password("secret_sauce")
        self.login_page.click_on_login_button()
        assert "Username is required" in self.login_page.error_message().text, "Неверное сообщение об ошибке."

    def test_empty_password(self):
        self.login_page.enter_username("standard_user")
        self.login_page.click_on_login_button()
        assert "Password is required" in self.login_page.error_message().text, "Неверное сообщение об ошибке."

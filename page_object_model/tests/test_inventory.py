from page_object_model.base_test import BaseTest



class TestInventory(BaseTest):
    def test_items_amount(self):
        self.login_page.login("standard_user", "secret_sauce")
        assert self.inventory_page.get_items_amount() == 6, "Количество товаров не совпадает."

    def test_all_items_are_displayed(self):
        self.login_page.login("standard_user", "secret_sauce")
        assert self.inventory_page.all_items_are_displayed(), "Не все товары отображаются."

    def test_all_items_names_are_displayed(self):
        self.login_page.login("standard_user", "secret_sauce")
        assert self.inventory_page.all_items_names_are_displayed(), "Не все названия товаров отображаются."

    def test_all_item_names_are_not_empty(self):
        self.login_page.login("standard_user", "secret_sauce")
        assert self.inventory_page.all_item_names_are_not_empty(), "Есть товары с пустыми названиями."

    def test_all_item_names_contains_sauce_labs(self):
        self.login_page.login("standard_user", "secret_sauce")
        assert self.inventory_page.all_item_names_contains_sauce_labs(), "Не все товары начинаются с 'Sauce Labs'."

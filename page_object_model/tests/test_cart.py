from page_object_model.base_test import BaseTest


class TestCart(BaseTest):
    # def test_backpack_cost(self):
    # 1. Login with valid data
    # self.login_page.success_login("standard_user", "secret_sauce")

    # 2. Remember the cost of the item "Backpack"
    # backpack_price = self.inventory_page.get_item_price("Sauce Labs Backpack")

    # 3. Add item "Backpack" to the cart
    # self.inventory_page.add_item_to_cart("Sauce Labs Backpack")

    # 4. Click on the cart button
    # self.inventory_page.go_to_cart()

    # 5. Check that the cost of the item in the cart equals to the cost of the item on the Inventory page
    # cart_price = self.cart_page.get_cart_item_price("Sauce Labs Backpack")
    # assert backpack_price == cart_price, "Цена товара в корзине не совпадает с ценой на странице инвентаря."

    def test_total_price(self):
        self.login_page.login("standard_user", "secret_sauce")

        nth_child_item_numbers = [1, 3, 5]
        self.inventory_page.add_items_to_cart(nth_child_item_numbers)
        self.inventory_page.click_cart_button()

        self.cart_page.click_checkout()

        self.checkout_first_page.fill_checkout_form("Oleksii", "Shchukin", "39288")
        self.checkout_first_page.click_continue()

        assert self.checkout_second_page.get_total_price() == "Total: $58.29"

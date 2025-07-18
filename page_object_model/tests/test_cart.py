from page_object_model.base_test import BaseTest


class TestCart(BaseTest):
    def test_backpack_cost(self):
        self.login_page.login("standard_user", "secret_sauce")

        backpack_nth_child_number = 1
        bike_light_nth_child_number = 2
        bolt_t_short_nth_child_number = 3

        backpack_price = self.inventory_page.get_price_per_item(backpack_nth_child_number)
        bike_light_price = self.inventory_page.get_price_per_item(bike_light_nth_child_number)
        bolt_t_short_price = self.inventory_page.get_price_per_item(bolt_t_short_nth_child_number)

        nth_child_item_numbers = [
            backpack_nth_child_number,
            bike_light_nth_child_number,
            bolt_t_short_nth_child_number
        ]

        self.inventory_page.add_items_to_cart(nth_child_item_numbers)
        self.inventory_page.click_cart_button()

        cart_backpack_nth_child_num = 3
        cart_bolt_t_short_nth_child_num = 4
        cart_bike_light_nth_child_num = 5

        cart_backpack_price = self.cart_page.get_cart_item_price(cart_backpack_nth_child_num)
        cart_bike_light_price = self.cart_page.get_cart_item_price(cart_bolt_t_short_nth_child_num)
        cart_bolt_t_short_price = self.cart_page.get_cart_item_price(cart_bike_light_nth_child_num)

        assert backpack_price == cart_backpack_price, "Цена товара в корзине не совпадает с ценой на странице инвентаря."
        assert bike_light_price == cart_bike_light_price, "Цена товара в корзине не совпадает с ценой на странице инвентаря."
        assert bolt_t_short_price == cart_bolt_t_short_price, "Цена товара в корзине не совпадает с ценой на странице инвентаря."

    def test_total_price(self):
        self.login_page.login("standard_user", "secret_sauce")

        nth_child_item_numbers = [1, 3, 5]
        self.inventory_page.add_items_to_cart(nth_child_item_numbers)
        self.inventory_page.click_cart_button()

        self.cart_page.click_checkout()

        self.checkout_first_page.fill_checkout_form("Oleksii", "Shchukin", "39288")
        self.checkout_first_page.click_continue()

        assert self.checkout_second_page.get_total_price() == "Total: $58.29"

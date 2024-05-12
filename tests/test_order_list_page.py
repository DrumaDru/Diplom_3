import pytest

from Diplom_3.pages.order_list_page import OrderListPage

class TestOrderListPage:

    # def test_get_order_modal(self, driver, log_in):
    #     order_list_page = OrderListPage(driver)
    #     result = order_list_page.get_order_modal()
    #
    #     assert result == "Cостав"

    # def test_history_order_in_order_list(self, driver, log_in, create_order):
    #     order_list_page = OrderListPage(driver)
    #     result = order_list_page.get_history_order_in_order_list()
    #
    #     assert result is True

    # def test_get_all_time_orders(self, driver, log_in):
    #     order_list_page = OrderListPage(driver)
    #
    #     result = order_list_page.get_all_time_orders()
    #
    #     assert result is True

    # def test_get_today_orders(self, driver, log_in):
    #     order_list_page = OrderListPage(driver)
    #     result = order_list_page.get_today_orders()
    #
    #     assert result is True


    def test_get_order_in_work(self, driver, log_in):
        order_list_page = OrderListPage(driver)
        result = order_list_page.get_order_in_work()

        assert result is True


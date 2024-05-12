import pytest
from Diplom_3.pages.main_page import MainPage


class TestMainPage:

    # def test_go_to_order_list(self, driver):
    #     main_page = MainPage(driver)
    #     result = main_page.go_to_order_list()
    #
    #     assert result == "Лента заказов"


    # def test_go_to_constructor(self, driver, log_in):
    #     main_page = MainPage(driver)
    #     main_page.go_to_order_list()
    #     result = main_page.go_to_constructor()
    #
    #     assert result == "Оформить заказ"

    # def test_get_ingredient(self,driver, log_in):
    #     main_page = MainPage(driver)
    #     result = main_page.get_ingredient()
    #
    #     assert result == 'Флюоресцентная булка R2-D3'

    # def test_close_modal(self, driver, log_in):
    #     main_page = MainPage(driver)
    #     result = main_page.close_modal()
    #
    #     assert result == False

    # def test_get_counter(self, driver, log_in):
    #     main_page = MainPage(driver)
    #     result = main_page.get_counter()
    #
    #     assert result == "2"

    def test_get_order(self, driver, log_in, create_order):
        main_page = MainPage(driver)
        result = main_page.get_order()

        assert result == "идентификатор заказа"







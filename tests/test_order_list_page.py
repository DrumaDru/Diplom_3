import pytest
import allure
from Diplom_3.pages.order_list_page import OrderListPage
from Diplom_3.pages.start_page import StartPage
from Diplom_3.pages.main_page import MainPage
from Diplom_3.pages.personal_account_page import PersonalAccount


class TestOrderListPage:
    @allure.title('Проверка открытия модального окна по клику на заказ, на странице "Лента заказов"')
    @allure.description(
        'На странице лента заказов, находим элемент заказа и по клику на него открываем модальное окно с информацией о заказе.'
        'В окрывшемся модальом окне, находим заголовок "Состав" и проверяем, что метод возвращает текст заголовка.')
    def test_get_order_modal(self, driver):
        main_page = MainPage(driver)
        order_list_page = OrderListPage(driver)

        main_page.go_to_order_list()

        result = order_list_page.get_order_modal()

        assert result == "Cостав"

    @allure.title('Проверка, что заказ во вкладке "История заказов", отображается в списке заказов на странице "Лента заказов')
    @allure.description(
        'На главной странице, находим элемент вкладки "Личный кабинет" и по клику переходим на страницу "Личный кабинет.'
        'На странице "Личный кабинет, находим элемент вкладки "История заказов" и переходим на нее по клику.'
        'Получам текст элемента заказа, находим элемент вкладки "Лента заказов" и по клику переходим на страницу "Лента заказов".'
        'На странице "Лента заказов", находим элемент заказа в списке заказов и проверяем, что номер закзаа из'
        'вкладки "История заказаов", совпадает с номером заказа в списке заказаов, во вкладке "Лента заказов".')
    def test_history_order_in_order_list(self, driver, registration_user_data):
        main_page = MainPage(driver)
        order_list_page = OrderListPage(driver)
        start_page = StartPage(driver)
        personal_account_page = PersonalAccount(driver)

        main_page.go_to_log_in()
        start_page.log_in(registration_user_data)
        main_page.create_order()
        main_page.go_to_personal_account()
        source_element = personal_account_page.get_order_from_history()
        main_page.go_to_order_list()
        expected_element = order_list_page.get_order_list()

        assert source_element == expected_element

    @allure.title('Проверка, что кол-во заказов за все время увеличивается после создания нового заказа.')
    @allure.description(
        'На главной странице, находим элемент вкладки "Лента заказов" и переходм на нее по клику.'
        'На странице "Лента заказов", находим элемент кол-ва заказов за все время и сохраняем его в переменную.'
        'На главной странице выполняем заказ, переходим на вкладку "Лента заказов" и находим'
        'элемент кол-ва заказов за все время, значение которого увеличилось, после нового заказка.'
        'Выполняем проверку, что кол-во заказов за все время до оформления нового заказа, меньше чем количество после. ')
    def test_get_all_time_orders(self, driver, registration_user_data):
        main_page = MainPage(driver)
        order_list_page = OrderListPage(driver)
        start_page = StartPage(driver)

        main_page.go_to_log_in()
        start_page.log_in(registration_user_data)
        main_page.go_to_order_list()

        all_time_order_before = order_list_page.get_all_time_orders()
        main_page.go_to_constructor()
        main_page.create_order()
        main_page.go_to_order_list()

        all_time_order_after = order_list_page.get_all_time_orders()

        assert all_time_order_before < all_time_order_after

    @allure.title('Проверка, что кол-во заказов за сегодня, увеличивается после создания нового заказа')
    @allure.description(
        'На главной странице, находим элемент вкладки "Лента заказов" и переходм на нее по клику.'
        'На странице "Лента заказов", находим элемент кол-ва заказов за сегодня и сохраняем его в переменную.'
        'На главной странице выполняем заказ, переходим на вкладку "Лента заказов" и находим'
        'элемент кол-ва заказов за сегодня, значение которого увеличилось, после нового заказка. Проверяем,'
        'что количество заказов за сегодня до оформления нового заказа, меньше, чем количество после.')
    def test_get_today_orders(self, driver, registration_user_data):
        main_page = MainPage(driver)
        order_list_page = OrderListPage(driver)
        start_page = StartPage(driver)

        main_page.go_to_log_in()
        start_page.log_in(registration_user_data)
        main_page.go_to_order_list()

        today_orders_before = order_list_page.get_today_orders()

        main_page.go_to_constructor()
        main_page.create_order()
        main_page.go_to_order_list()

        today_orders_after = order_list_page.get_today_orders()


        assert today_orders_before < today_orders_after


    @allure.title('Проверка, что созданный новый заказ, отображается в разделе "В работе" на странице "Лента заказов"')
    @allure.description(
        'С помощью вспомогательного метода, создаем новый заказ, затем на главной странице, находим элемент вкладки '
        '"Лента заказов" и переходм на нее по клику.'
        'На странице "Лента заказов", находим элемент заказа, получаем его текст и сохраняем в переменную, затем'
        'находим элемент значения вкладки "В работе" и ожидаем, когда текст элемента заказа, отобразится в значении'
        'элемента раздела в "Работе" и сохраняем текст элемента в переменную.'
        'Проверяем, что метод возвращает равеноство текста заказа в ленте заказов и в разделе "В работе".')
    def test_get_order_in_work(self, driver, registration_user_data):
        main_page = MainPage(driver)
        order_list_page = OrderListPage(driver)
        start_page = StartPage(driver)

        main_page.go_to_log_in()
        start_page.log_in(registration_user_data)
        main_page.create_order()
        main_page.go_to_order_list()

        result = order_list_page.get_order_in_work()

        assert result is True


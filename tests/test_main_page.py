import pytest
import allure
from Diplom_3.pages.start_page import StartPage
from Diplom_3.pages.main_page import MainPage
from Diplom_3.pages.order_list_page import OrderListPage
class TestMainPage:
    @allure.title('Проверка перехода по клику "Лента заказов"')
    @allure.description('На главной странице, находим элемент вкладки "Лента заказов", переходим на него по клику,'
                        'находим заголовок страницу "Лента заказов" и проверяем, что метод возвращает текст заголовка.')
    def test_go_to_order_list(self, driver):
        main_page = MainPage(driver)
        order_list_page = OrderListPage(driver)

        main_page.go_to_order_list()
        result = order_list_page.get_order_list_title()

        assert result == "Лента заказов"

    @allure.title('Проверка перехода по клику "Конструктор"')
    @allure.description('На главной странице, находим элемент вкладки "Лента заказов", переходим на него по клику,'
                        'находим зэлемент вкладки "Конструктор" и переходим на него по клику. На главной странице'
                        'находим элемент кнопки "Формить заказ" и проверяем, что метод возвращает текст элемента кнопки.')
    def test_get_constructor_title(self, driver):
         main_page = MainPage(driver)

         result = main_page.get_constructor_title()

         assert result == "Соберите бургер"

    @allure.title('Проверка открытия модального окна "Детали ингредиента" по клиику на ингредиент')
    @allure.description('На главной странице, находим элемент ингредиента и открываем модальное окно по клику на ингредиент.'
                        'В окрывшемся модальом окне, находим заголовок и проверяем, что метод возвращает текст заголовка.')
    def test_get_ingredient_details(self, driver):
         main_page = MainPage(driver)

         result = main_page.get_ingredient_details()

         assert result == 'Детали ингредиента'

    @allure.title('Проверка закрытия модального окна "Детали ингредиента" по клиику на крестик')
    @allure.description(
        'На главной странице, находим элемент ингредиента и открываем модальное окно по клику на ингредиент.'
        'В окрывшемся модальом окне, находим элемент крестика и проверяем, что метод возвращет логическое значение,'
        'которое соответствует тому, что элемент модального окна не отображается на странице.')
    def test_close_modal(self, driver):
         main_page = MainPage(driver)

         result = main_page.close_modal()

         assert result == False

    @allure.title('Проверка, что счетчик ингредиента меняется, если его переместить в конструктор заказа')
    @allure.description(
        'На главное странице находим элемент ингредиента и конструктора заказа и элемент счетчика кол-ва ингредиента,'
        'добавленного в заказ. Переносим ингредиент в конструктор заказа и проверяем, что метод возвращает, измененное'
        'значение счетчика кол-ва ингредиента.')
    def test_get_counter(self, driver):
         main_page = MainPage(driver)

         result = main_page.get_counter()

         assert result == "2"

    @allure.title('Проверка открытия модального окна по клику на кнопку "Оформить заказ"')
    @allure.description(
        'На главной странице, находим элемент кнопки "оформить заказ" и открываем модальное окно по клику на кнопке.'
        'В окрывшемся модальом окне, находим элемент текста "идентификатор заказа" и проверяем, что метод возвращает этот текст.')
    def test_get_order_modal(self, driver, registration_user_data):
        main_page = MainPage(driver)
        start_page = StartPage(driver)

        main_page.go_to_log_in()
        start_page.log_in(registration_user_data)

        result = main_page.get_order()

        assert result == "идентификатор заказа"







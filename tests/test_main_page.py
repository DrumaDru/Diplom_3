import pytest
import allure
from Diplom_3.pages.main_page import MainPage
class TestMainPage:
    @allure.title('Проверка перехода по клику "Лента заказов"')
    @allure.description('На главной странице, находим элемент вкладки "Лента заказов", переходим на него по клику,'
                        'находим заголовок страницу "Лента заказов" и проверяем, что метод возвращает текст заголовка.')
    def test_go_to_order_list(self, driver):
         main_page = MainPage(driver)
         result = main_page.go_to_order_list()

         assert result == "Лента заказов"

    @allure.title('Проверка перехода по клику "Конструктор"')
    @allure.description('На главной странице, находим элемент вкладки "Лента заказов", переходим на него по клику,'
                        'находим зэлемент вкладки "Конструктор" и переходим на него по клику. На главной странице'
                        'находим элемент кнопки "Формить заказ" и проверяем, что метод возвращает текст элемента кнопки.')
    def test_go_to_constructor(self, driver, log_in):
         main_page = MainPage(driver)
         main_page.go_to_order_list()
         result = main_page.go_to_constructor()

         assert result == "Оформить заказ"

    @allure.title('Проверка открытия модального окна "Детали ингредиента" по клиику на ингредиент')
    @allure.description('На главной странице, находим элемент ингредиента и открываем модальное окно по клику на ингредиент.'
                        'В окрывшемся модальом окне, находим заголовок и проверяем, что метод возвращает текст заголовка.')
    def test_get_ingredient_details(self, driver, log_in):
         main_page = MainPage(driver)
         result = main_page.get_ingredient_details()

         assert result == 'Детали ингредиента'

    @allure.title('Проверка закрытия модального окна "Детали ингредиента" по клиику на крестик')
    @allure.description(
        'На главной странице, находим элемент ингредиента и открываем модальное окно по клику на ингредиент.'
        'В окрывшемся модальом окне, находим элемент крестика и проверяем, что метод возвращет логическое значение,'
        'которое соответствует тому, что элемент модального окна не отображается на странице.')
    def test_close_modal(self, driver, log_in):
         main_page = MainPage(driver)
         result = main_page.close_modal()

         assert result == False

    @allure.title('Проверка, что счетчик ингредиента меняется, если его переместить в конструктор заказа')
    @allure.description(
        'На главное странице находим элемент ингредиента и конструктора заказа и элемент счетчика кол-ва ингредиента,'
        'добавленного в заказ. Переносим ингредиент в конструктор заказа и проверяем, что метод возвращает, измененное'
        'значение счетчика кол-ва ингредиента.')
    def test_get_counter(self, driver, log_in):
         main_page = MainPage(driver)
         result = main_page.get_counter()

         assert result == "2"

    @allure.title('Проверка открытия модального окна по клику на кнопку "Оформить заказ"')
    @allure.description(
        'На главной странице, находим элемент кнопки "оформить заказ" и открываем модальное окно по клику на кнопке.'
        'В окрывшемся модальом окне, находим элемент текста "идентификатор заказа" и проверяем, что метод возвращает этот текст.')
    def test_get_order(self, driver, log_in, create_order):
        main_page = MainPage(driver)
        result = main_page.get_order()

        assert result == "идентификатор заказа"







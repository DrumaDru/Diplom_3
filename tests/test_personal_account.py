import pytest
import allure
from Diplom_3.pages.personal_account_page import PersonalAccount
class TestPersonalAccount:

    @allure.title('Проверка, что по клику на вкладку "Личный кабинет", открывается странциа личного кабинета.')
    @allure.description(
        'На главной странице, находим элемент вкладки "Личный кабинет" и переходим на нее по клику.'
        'На странице личного кабинета, находим элемент вкладки "Профиль" и проверяем, что метод возвращает'
        'текст элемента вкладки.')
    def test_personal_account(self, driver, log_in):
          personal_account = PersonalAccount(driver)
          result = personal_account.go_to_personal_account()

          assert result == "Профиль"
    @allure.title('Проверка, что по клику на вкладку "История заказов", вкладка становится активной.')
    @allure.description(
        'На главной странице, находим элемент вкладки "Личный кабинет" и переходим на нее по клику.'
        'На странице личного кабинета, находим элемент вкладки "История заказов" и проверяем, что значение класса, '
        'которое возвращает метод, содержит текст, который соответствует активной вкладке.')
    def test_go_to_orders_history(self, driver, log_in):
          personal_account = PersonalAccount(driver)
          result = personal_account.go_to_orders_history()

          assert "Account_link_active" in result
    @allure.title('Проверка, что по клику на вкладку "Выход", происходит выход из аккаунта пользователя')
    @allure.description(
        'На главной странице, находим элемент вкладки "Личный кабинет" и переходим на нее по клику.'
        'На странице личного кабинета, находим элемент кнопки "Выход" и выполняем по ней клик.'
        'После выхода из аккаунта пользователя и перехода на страницу авторизации, находим элемент кнопки "Войти"'
        'и проверяем, что метод возвращает текст кнопки.')
    def test_exit_from_account(self, driver, log_in):
        personal_account = PersonalAccount(driver)
        result = personal_account.exit_from_account()

        assert result == "Войти"


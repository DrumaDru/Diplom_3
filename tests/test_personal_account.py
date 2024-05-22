import pytest
import allure
from Diplom_3.pages.personal_account_page import PersonalAccount
from Diplom_3.pages.start_page import StartPage
from Diplom_3.pages.main_page import MainPage
class TestPersonalAccount:

    @allure.title('Проверка, что по клику на вкладку "Личный кабинет", открывается странциа личного кабинета.')
    @allure.description(
        'На главной странице, находим элемент вкладки "Личный кабинет" и переходим на нее по клику.'
        'На странице личного кабинета, находим элемент вкладки "Профиль" и проверяем, что метод возвращает'
        'текст элемента вкладки.')
    def test_go_to_personal_account(self, driver, registration_user_data):
          personal_account = PersonalAccount(driver)
          main_page = MainPage(driver)
          start_page = StartPage(driver)

          main_page.go_to_log_in()
          start_page.log_in(registration_user_data)
          main_page.go_to_personal_account()

          result = personal_account.get_profile_tab_text()

          assert result == "Профиль"

    @allure.title('Проверка, что по клику на вкладку "История заказов", вкладка становится активной.')
    @allure.description(
        'На главной странице, находим элемент вкладки "Личный кабинет" и переходим на нее по клику.'
        'На странице личного кабинета, находим элемент вкладки "История заказов" и проверяем, что значение класса, '
        'которое возвращает метод, содержит текст, который соответствует активной вкладке.')
    def test_go_to_orders_history(self, driver, registration_user_data):
          personal_account = PersonalAccount(driver)
          main_page = MainPage(driver)
          start_page = StartPage(driver)

          main_page.go_to_log_in()
          start_page.log_in(registration_user_data)
          main_page.go_to_personal_account()

          result = personal_account.go_to_orders_history()

          assert "Account_link_active" in result

    @allure.title('Проверка, что по клику на вкладку "Выход", происходит выход из аккаунта пользователя')
    @allure.description(
        'На главной странице, находим элемент вкладки "Личный кабинет" и переходим на нее по клику.'
        'На странице личного кабинета, находим элемент кнопки "Выход" и выполняем по ней клик.'
        'После выхода из аккаунта пользователя и перехода на страницу авторизации, находим элемент кнопки "Войти"'
        'и проверяем, что метод возвращает текст кнопки.')
    def test_exit_from_account(self, driver, registration_user_data):
        personal_account = PersonalAccount(driver)
        main_page = MainPage(driver)
        start_page = StartPage(driver)

        main_page.go_to_log_in()
        start_page.log_in(registration_user_data)
        main_page.go_to_personal_account()
        personal_account.exit_from_account()

        result = start_page.get_enter_button_text()

        assert result == "Войти"


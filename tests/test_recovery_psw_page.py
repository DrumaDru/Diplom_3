import pytest
import allure
from Diplom_3.pages.start_page import StartPage
from Diplom_3.pages.recovery_pwd_page import RecoveryPwdPage
from Diplom_3.pages.main_page import MainPage

class TestRecoveryPassword:
    @allure.title('Проверка, что по клику на кнопку "Восстановить пароль", происходт переход на страницу восстановления пароля.')
    @allure.description(
        'На главной странице, находим элемент кнопки "Войти в аккаунт" и выполняем по ней клик.'
        'На странице авторизации, находим гиперссылку "Восстановить пароль" и переходим на нее по клику.'
        'На странице восстановления пароля, находим элемент кнопки "Восстановить" и проверяем, что '
        'метод возращает текст кнопки.')
    def test_recovery_pwd_link(self, driver):
        recovery_pass_page = RecoveryPwdPage(driver)
        start_page = StartPage(driver)
        main_page = MainPage(driver)

        main_page.go_to_log_in()
        start_page.go_to_recovery_pwd_link()

        result = recovery_pass_page.get_recovery_button_text()

        assert result == "Восстановить"

    @allure.title('Проверка, ввода почты и клик по кнопке "Восстановить", на странице восстановления пароля.')
    @allure.description(
        'На главной странице, находим элемент кнопки "Войти в аккаунт" и выполняем по ней клик.'
        'На странице авторизации, находим гиперссылку "Восстановить пароль" и переходим на нее по клику.'
        'На странице восстановления пароля, находим элемент поля ввода почты и заполняем поле почтой.'
        'Затем находим элемент кнопки "Восстановить" и выполняем по ней клик. На странице ввода нового пароля,'
        'находим элемент кнопки "Сохранить" и проверяем, что метод возвращает текст кнопки.')
    def test_recovery_pwd_email_input(self, driver, registration_user_data):
        recovery_pass_page = RecoveryPwdPage(driver)
        start_page = StartPage(driver)
        main_page = MainPage(driver)
        email = registration_user_data

        main_page.go_to_log_in()
        start_page.go_to_recovery_pwd_link()

        result = recovery_pass_page.recovery_pwd_email_input(email)

        assert result == "Сохранить"

    @allure.title('Проверка, что поле ввода нового пароля становится активным и подсвечивается после клика на кнопку'
                  'показать/скрыть пароль.')
    @allure.description(
        'На главной странице, находим элемент кнопки "Войти в аккаунт" и выполняем по ней клик.'
        'На странице авторизации, находим гиперссылку "Восстановить пароль" и переходим на нее по клику.'
        'На странице восстановления пароля, находим элемент кнопки показать/скрыть пароль и выполняем по ней клик.'
        'Проверяем, что значение, которое возвращает метод, соответствует значению нажатой кнопки показать/скрыть пароль.' )
    def test_click_hide_icon(self, driver, registration_user_data):
        recovery_pass_page = RecoveryPwdPage(driver)
        start_page = StartPage(driver)
        main_page = MainPage(driver)
        email = registration_user_data

        main_page.go_to_log_in()
        start_page.go_to_recovery_pwd_link()
        recovery_pass_page.go_to_saving_recovered_pass(email)

        result = recovery_pass_page.click_hide_icon()

        assert result == 'text'


import pytest
import allure
from Diplom_3.pages.start_page import StartPage
from Diplom_3.pages.recovery_pwd_page import RecoveryPwdPage

class TestRecoveryPassword:
    @allure.title('Проверка, что по клику на кнопку "Восстановить пароль", происходт переход на страницу восстановления пароля.')
    @allure.description(
        'На главной странице, находим элемент кнопки "Войти в аккаунт" и выполняем по ней клик.'
        'На странице авторизации, находим гиперссылку "Восстановить пароль" и переходим на нее по клику.'
        'На странице восстановления пароля, находим элемент кнопки "Восстановить" и проверяем, что '
        'метод возращает текст кнопки.')
    def test_recovery_pwd_link(self, driver):
        start_page = StartPage(driver)
        result = start_page.recovery_pwd_link()

        assert result == "Восстановить"

    @allure.title('Проверка, ввода почты и клик по кнопке "Восстановить", на странице восстановления пароля.')
    @allure.description(
        'На главной странице, находим элемент кнопки "Войти в аккаунт" и выполняем по ней клик.'
        'На странице авторизации, находим гиперссылку "Восстановить пароль" и переходим на нее по клику.'
        'На странице восстановления пароля, находим элемент поля ввода почты и заполняем поле почтой.'
        'Затем находим элемент кнопки "Восстановить" и выполняем по ней клик. На странице ввода нового пароля,'
        'находим элемент кнопки "Сохранить" и проверяем, что метод возвращает текст кнопки. '
        'метод возращает текст кнопки.')
    def test_recovery_pwd_email_input(self, driver, registration_user):
        recovery_pass_page = RecoveryPwdPage(driver)
        email = registration_user
        result = recovery_pass_page.recovery_pwd_email_input(email)

        assert result == "Сохранить"

    @allure.title('Проверка, что поле ввода нового пароля становится активным и подсвечивается после клика на кнопку'
                  'показать/скрыть пароль.')
    @allure.description(
        'На главной странице, находим элемент кнопки "Войти в аккаунт" и выполняем по ней клик.'
        'На странице авторизации, находим гиперссылку "Восстановить пароль" и переходим на нее по клику.'
        'На странице восстановления пароля, находим элемент кнопки показать/скрыть пароль и выполняем по ней клик.'
        'Проверяем, что значение, которое возвращает метод, соответствует значению нажатой кнопки показать/скрыть пароль.' )
    def test_click_hide_icon(self, driver, registration_user):
        recovery_pass_page = RecoveryPwdPage(driver)
        email = registration_user
        result = recovery_pass_page.click_hide_icon(email)
        assert result == 'text'


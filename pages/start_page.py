import allure
from Diplom_3.pages.base_page import BasePage
from Diplom_3.locators.start_page_locators import StartPageLocators
import test_data


class StartPage(BasePage):
    enter_button_login = StartPageLocators.ENTER_BUTTON_LOGIN
    input_email_login = StartPageLocators.INPUT_EMAIL_LOGIN
    input_password_login = StartPageLocators.INPUT_PASSWORD_LOGIN
    recovery_password_link = StartPageLocators.RECOVERY_PASSWORD_LINK

    @allure.step('Создаем метод, который  переходит на страницу ввода электронной почты,по гипер ссылке "Восстановить пароль".')
    def go_to_recovery_pwd_link(self):
        self.click_to_element(self.recovery_password_link)

    @allure.step('Создаем метод, которвый выполняет ввод данных для авториации в поля "Email" и "Пароль" и нажимает'
                 'на кнопку "Войти", для выполнения авторизации пользователя.')
    def log_in(self, email):
        password = test_data.payload["password"]
        self.add_text_to_element(self.input_email_login, email)
        self.add_text_to_element(self.input_password_login, password)
        self.click_to_element(self.enter_button_login)

    @allure.step('Создаем метод, который возвращает текст элемента кнопки "Войти".')
    def get_enter_button_text(self):
        return self.get_text_from_element(self.enter_button_login)










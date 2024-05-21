import allure
from Diplom_3.pages.base_page import BasePage
from Diplom_3.locators.main_page_locators import MainPageLocators
from Diplom_3.locators.start_page_locators import StartPageLocators
from Diplom_3.locators.password_recovery_page_locators import PasswordRecoveryPageLocators
import test_data


class StartPage(BasePage):
    enter_button_login = StartPageLocators.ENTER_BUTTON_LOGIN
    input_email_login = StartPageLocators.INPUT_EMAIL_LOGIN
    input_password_login = StartPageLocators.INPUT_PASSWORD_LOGIN
    recovery_password_link = StartPageLocators.RECOVERY_PASSWORD_LINK
    recovery_password_button = PasswordRecoveryPageLocators.RECOVERY_PASSWORD_BUTTON

    @allure.step('Создаем метод, который переход на страницу авторизации и переходит на страницу ввода электронной почты,'
                 'по гипер ссылке "Восстановить пароль". На странице ввода почты, метод возвращает текст кнопки "Восстановить"')
    def recovery_pwd_link(self):
        account_button = self.find_element_with_wait(self.enter_to_account_button)
        account_button.click()
        self.click_to_element(self.recovery_password_link)
        return self.get_text_from_element(self.recovery_password_button)


    def log_in(self, email):
        password = test_data.payload["password"]
        self.add_text_to_element(self.input_email_login, email)
        self.add_text_to_element(self.input_password_login, password)
        self.click_to_element(self.enter_button_login)













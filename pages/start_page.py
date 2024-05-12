import allure
from Diplom_3.pages.base_page import BasePage
from Diplom_3.locators.main_page_locators import MainPageLocators
from Diplom_3.locators.start_page_locators import StartPageLocators
from Diplom_3.locators.password_recovery_page_locators import PasswordRecoveryPageLocators


class StartPage(BasePage):
    enter_to_account_button = MainPageLocators.ENTER_TO_ACCOUNT_BUTTON
    recovery_password_link = StartPageLocators.RECOVERY_PASSWORD_LINK
    recovery_password_button = PasswordRecoveryPageLocators.RECOVERY_PASSWORD_BUTTON

    @allure.step('Создаем метод, который переход на страницу авторизации и переходит на страницу ввода электронной почты,'
                 'по гипер ссылке "Восстановить пароль". На странице ввода почты, метод возвращает текст кнопки "Восстановить"')
    def recovery_pwd_link(self):
        account_button = self.find_element_with_wait(self.enter_to_account_button)
        account_button.click()
        self.click_to_element(self.recovery_password_link)
        return self.get_text_from_element(self.recovery_password_button)


















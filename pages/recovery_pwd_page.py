import allure
from Diplom_3.pages.base_page import BasePage
from Diplom_3.locators.main_page_locators import MainPageLocators
from Diplom_3.locators.start_page_locators import StartPageLocators
from Diplom_3.locators.password_recovery_page_locators import PasswordRecoveryPageLocators

class RecoveryPwdPage(BasePage):
    enter_to_account_button = MainPageLocators.ENTER_TO_ACCOUNT_BUTTON
    recovery_password_link = StartPageLocators.RECOVERY_PASSWORD_LINK
    recovery_password_button = PasswordRecoveryPageLocators.RECOVERY_PASSWORD_BUTTON
    email_input = PasswordRecoveryPageLocators.EMAIL_INPUT
    save_button = PasswordRecoveryPageLocators.SAVE_BUTTON
    hide_icon = PasswordRecoveryPageLocators.HIDE_ICON
    pass_input_type = PasswordRecoveryPageLocators.PASS_INPUT_TYPE

    @allure.step('Создаем метод, который переходит на страницу авторизации, затем по гиперссылке на страницу ввода электронное почты, '
                 'выполняет ввод почты и переходит на страниу восстановления пароля.')
    def recovery_pwd_email_input(self, email):
        self.click_to_element(self.enter_to_account_button)
        self.click_to_element(self.recovery_password_link)
        self.add_text_to_element(self.email_input, email)
        self.click_to_element(self.recovery_password_button)

        return self.get_text_from_element(self.save_button)

    @allure.step('Создаем метод, который переходит на страницу авторизации, затем по гиперссылке на страницу ввода электронное почты, '
                 'выполняет ввод почты и переходит на страниу восстановления пароля. На странице восстановления пароля,'
                 'метод выполняет клик по кнопке показать/скрыть пароль и возвращает атрибут элемента, который меняется,'
                 'если поле ввода становится активным и подсвечивется.')
    def click_hide_icon(self, email):
        self.click_to_element(self.enter_to_account_button)
        self.click_to_element(self.recovery_password_link)
        self.add_text_to_element(self.email_input, email)
        self.click_to_element(self.recovery_password_button)

        hide_icon = self.find_element_with_wait(self.hide_icon)
        hide_icon.click()

        attr_value = self.get_attribute_from_element(self.pass_input_type, "type")
        return attr_value



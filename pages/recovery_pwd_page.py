import allure
from Diplom_3.pages.base_page import BasePage
from Diplom_3.locators.password_recovery_page_locators import PasswordRecoveryPageLocators

class RecoveryPwdPage(BasePage):
    recovery_password_button = PasswordRecoveryPageLocators.RECOVERY_PASSWORD_BUTTON
    email_input = PasswordRecoveryPageLocators.EMAIL_INPUT
    save_button = PasswordRecoveryPageLocators.SAVE_BUTTON
    hide_icon = PasswordRecoveryPageLocators.HIDE_ICON
    pass_input_type = PasswordRecoveryPageLocators.PASS_INPUT_TYPE

    @allure.step('Создаем метод, который возвращет текст элемента кнопки "Восстановить".')
    def get_recovery_button_text(self):
        return self.get_text_from_element(self.recovery_password_button)

    @allure.step('Создаем метод, который выполняет ввод почты в поле ввода и нажимает на кнопку "Восстановить",'
                 'для перехода на станицу ввода восстановленного пароля.')
    def go_to_saving_recovered_pass(self, email):
        self.add_text_to_element(self.email_input, email)
        self.click_to_element(self.recovery_password_button)


    @allure.step('Создаем метод, который выполняет ввод почты в поле ввода, переходит на страницу '
                 'сохранения восстановленного пароля.')
    def recovery_pwd_email_input(self, email):
        self.add_text_to_element(self.email_input, email)
        self.click_to_element(self.recovery_password_button)

        return self.get_text_from_element(self.save_button)


    @allure.step('Создаем метод, который на странице восстановления пароля выполняет клик по кнопке показать/скрыть пароль '
                 'и возвращает атрибут элемента, который меняется, если поле ввода становится активным и подсвечивется.')
    def click_hide_icon(self):
        self.click_to_element(self.hide_icon)

        attr_value = self.get_attribute_from_element(self.pass_input_type, "type")

        return attr_value



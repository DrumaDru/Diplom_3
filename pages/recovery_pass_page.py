import time

from Diplom_3.pages.base_page import BasePage
from Diplom_3.locators.main_page_locators import MainPageLocators
from Diplom_3.locators.start_page_locators import StartPageLocators
from Diplom_3.locators.password_recovery_page_locators import PasswordRecoveryPageLocators

class RecoveryPassPage(BasePage):
    recovery_password_link = StartPageLocators.RECOVERY_PASSWORD_LINK
    recovery_password = PasswordRecoveryPageLocators.RECOVERY_PASSWORD
    create_order_button = MainPageLocators.CREATE_ORDER_BUTTONT
    email_input = PasswordRecoveryPageLocators.EMAIL_INPUT
    save_button = PasswordRecoveryPageLocators.SAVE_BUTTON
    hide_icon = PasswordRecoveryPageLocators.HIDE_ICON
    pass_input_type = PasswordRecoveryPageLocators.PASS_INPUT_TYPE

    def recovery_pass_email_input(self, email):
        self.click_to_element(self.create_order_button)
        self.click_to_element(self.recovery_password_link)
        self.add_text_to_element(self.email_input, email)
        self.click_to_element(self.recovery_password)

        return self.get_text_from_element(self.save_button)


    def click_hide_icon(self, email):
        self.recovery_pass_email_input(email)
        hide_icon = self.find_element_with_wait(self.hide_icon)
        hide_icon.click()
        time.sleep(3)
        attr_value = self.get_attribute_from_element(self.pass_input_type, "type")
        return attr_value



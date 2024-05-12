import time
from Diplom_3.pages.base_page import BasePage
from Diplom_3.locators.main_page_locators import MainPageLocators
from Diplom_3.locators.start_page_locators import StartPageLocators
from Diplom_3.locators.password_recovery_page_locators import PasswordRecoveryPageLocators


class StartPage(BasePage):
    create_order_button = MainPageLocators.CREATE_ORDER_BUTTONT
    recovery_password_link = StartPageLocators.RECOVERY_PASSWORD_LINK
    recovery_password = PasswordRecoveryPageLocators.RECOVERY_PASSWORD
    personal_account = MainPageLocators.PERSONAL_ACCOUNT


    def recovery_pass_link(self):
        personal_account = self.find_element_with_wait(self.create_order_button)
        personal_account.click()
        self.click_to_element(self.recovery_password_link)
        return self.get_text_from_element(self.recovery_password)


















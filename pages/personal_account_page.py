import time
from Diplom_3.pages.base_page import BasePage
from Diplom_3.locators.personal_account_page_locators import PersonalAccountLocators
from Diplom_3.locators.start_page_locators import StartPageLocators
from Diplom_3.locators.main_page_locators import MainPageLocators

class PersonalAccount(BasePage):
    personal_account = MainPageLocators.PERSONAL_ACCOUNT
    profile_tab = PersonalAccountLocators.PROFILE_TAB
    orders_history = PersonalAccountLocators.ORDERS_HISTORY
    order_number = MainPageLocators.ORDER_NUMBER
    order_list_tab = MainPageLocators.ORDER_LIST_TAB
    exit_tab = PersonalAccountLocators.EXIT_TAB
    enter_button_login = StartPageLocators.ENTER_BUTTON_LOGIN


    def go_to_personal_account(self):
        self.click_to_element(self.personal_account)
        return self.get_text_from_element(self.profile_tab)

    def go_to_orders_history(self):
         self.click_to_element(self.personal_account)
         self.click_to_element(self.orders_history)

         return self.get_attribute_from_element(self.orders_history, "class")

    def exit_from_account(self):
        self.click_to_element(self.personal_account)
        self.click_to_element(self.exit_tab)

        return self.get_text_from_element(self.enter_button_login)



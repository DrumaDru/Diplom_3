import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Diplom_3.helpers import Helpers
from Diplom_3.pages.base_page import BasePage
from Diplom_3.locators.main_page_locators import MainPageLocators
from Diplom_3.locators.order_list_page_locators import OrderPageListLocators
from Diplom_3.locators.personal_account_page_locators import PersonalAccountLocators
class OrderListPage(BasePage):
    constructor_tab = MainPageLocators.CONSTRUCTOR_TAB
    personal_account = MainPageLocators.PERSONAL_ACCOUNT
    orders_history = PersonalAccountLocators.ORDERS_HISTORY
    constructor_element = MainPageLocators.CONSTRUCTOR_ELEMENT
    bun = MainPageLocators.BUN
    order_list_tab = MainPageLocators.ORDER_LIST_TAB
    order = OrderPageListLocators.ORDER
    order_modal = OrderPageListLocators.ORDER_MODAL
    order_from_history = PersonalAccountLocators.ORDER_FROM_HISTORY
    order_from_order_list = OrderPageListLocators.ORDER_FROM_ORDER_LIST
    all_time_orders = OrderPageListLocators.ALL_TIME_ORDERS
    today_orders = OrderPageListLocators.TODAY_ORDERS
    order_in_work = OrderPageListLocators.ORDER_IN_WORK


    def get_order_modal(self):
         self.click_to_element(self.order_list_tab)
         self.click_to_element(self.order)

         return self.get_text_from_element(self.order_modal)

    def get_history_order_in_order_list(self):
        self.click_to_element(self.personal_account)
        self.click_to_element(self.orders_history)
        source_element = self.get_text_from_element(self.order_from_history)
        self.click_to_element(self.order_list_tab)
        expected_element = self.get_text_from_element(self.order_from_order_list)

        return source_element == expected_element

    def get_all_time_orders(self):
        helpers = Helpers(self.driver)
        self.click_to_element(self.order_list_tab)
        count_order_before = int(self.get_text_from_element(self.all_time_orders))
        self.click_to_element(self.constructor_tab)

        helpers.create_order()

        self.click_to_element(self.order_list_tab)
        count_order_after = int(self.get_text_from_element(self.all_time_orders))

        return count_order_after > count_order_before



    def get_today_orders(self):
        helpers = Helpers(self.driver)
        self.click_to_element(self.order_list_tab)
        count_order_before = int(self.get_text_from_element(self.today_orders))
        self.click_to_element(self.constructor_tab)

        helpers.create_order()

        self.click_to_element(self.order_list_tab)
        count_order_after = int(self.get_text_from_element(self.today_orders))

        return count_order_after > count_order_before


    def get_order_in_work(self):
        helpers = Helpers(self.driver)
        helpers.create_order()
        self.click_to_element(self.order_list_tab)
        new_order = self.get_text_from_element(self.order_from_order_list)
        new_order_stripped = new_order.lstrip("#")
        order_in_work_locator = self.order_in_work

        WebDriverWait(self.driver, 30).until(
            EC.text_to_be_present_in_element(order_in_work_locator, new_order_stripped)
        )
        order_in_work = self.get_text_from_element(order_in_work_locator)

        return new_order_stripped == order_in_work










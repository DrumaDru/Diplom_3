import time
from selenium.webdriver.common.action_chains import ActionChains
from Diplom_3.pages.base_page import BasePage
from Diplom_3.locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    order_list_tab = MainPageLocators.ORDER_LIST_TAB
    order_list_title = MainPageLocators.ORDER_LIST_TITLE
    constructor_tab = MainPageLocators.CONSTRUCTOR_TAB
    ingredient = MainPageLocators.INGREDIENT
    close_button = MainPageLocators.CLOSE_BUTTON
    modal_title = MainPageLocators.MODAL_TITLE
    counter = MainPageLocators.COUNTER
    constructor_element = MainPageLocators.CONSTRUCTOR_ELEMENT
    bun = MainPageLocators.BUN
    create_order_button = MainPageLocators.CREATE_ORDER_BUTTON
    order_modal = MainPageLocators.ORDER_MODAL



    def go_to_order_list(self):
        self.click_to_element(self.order_list_tab)
        return self.get_text_from_element(self.order_list_title)



    def go_to_constructor(self):
        self.click_to_element(self.order_list_tab)
        time.sleep(3)
        self.click_to_element(self.constructor_tab)
        return self.get_text_from_element(self.create_order_button)

    def get_ingredient(self):
        self.click_to_element(self.ingredient)
        return self.get_attribute_from_element(self.ingredient, 'alt')

    def close_modal(self):
        self.click_to_element(self.ingredient)
        self.click_to_element(self.close_button)
        element = self.find_element_with_wait(self.modal_title)
        self.wait_until_close(self.modal_title)

        return element.is_displayed()

    def get_counter(self):
        action_chains = ActionChains(self.driver)
        source_element = self.find_element_with_wait(self.bun)
        target_element = self.find_element_with_wait(self.constructor_element)
        action_chains.drag_and_drop(source_element, target_element).perform()

        return self.get_text_from_element(self.counter)

    def get_order(self):
        self.click_to_element(self.create_order_button)

        return self.get_text_from_element(self.order_modal)









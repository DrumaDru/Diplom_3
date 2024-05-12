from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Diplom_3.pages.base_page import BasePage
from Diplom_3.locators.main_page_locators import MainPageLocators
import time


class Helpers(BasePage):
    constructor_element = MainPageLocators.CONSTRUCTOR_ELEMENT
    bun = MainPageLocators.BUN
    create_order_button = MainPageLocators.CREATE_ORDER_BUTTON
    close_button = MainPageLocators.CLOSE_BUTTON


    def create_order(self):
        action_chains = ActionChains(self.driver)
        source_element = self.find_element_with_wait(self.bun)
        target_element = self.find_element_with_wait(self.constructor_element)
        action_chains.drag_and_drop(source_element, target_element).perform()
        self.click_to_element(self.create_order_button)
        time.sleep(3)
        WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located(self.close_button))
        close_button = self.driver.find_element(*self.close_button)
        close_button.click()
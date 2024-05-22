import allure
from Diplom_3.pages.base_page import BasePage
from Diplom_3.locators.personal_account_page_locators import PersonalAccountLocators

class PersonalAccount(BasePage):
    profile_tab = PersonalAccountLocators.PROFILE_TAB
    orders_history = PersonalAccountLocators.ORDERS_HISTORY
    exit_tab = PersonalAccountLocators.EXIT_TAB
    order_from_history = PersonalAccountLocators.ORDER_FROM_HISTORY

    @allure.step('Создаем метод, который возвращает текст влкадки "Профиль"')
    def get_profile_tab_text(self):
        return self.get_text_from_element(self.profile_tab)

    @allure.step('Создаем метод, который возвращает атрибут элемента вкладки "История заказов"')
    def go_to_orders_history(self):
         self.click_to_element(self.orders_history)

         return self.get_attribute_from_element(self.orders_history, "class")

    @allure.step('Создаем метод, который возвращает текст элемента номера заказа во влкадке "История заказов"')
    def get_order_from_history(self):
        self.click_to_element(self.orders_history)
        return self.get_text_from_element(self.order_from_history)

    @allure.step('Создаем метод, который выполняет нажатие на кнопку "Выход"')
    def exit_from_account(self):
        self.click_to_element(self.exit_tab)




import allure
from Diplom_3.pages.base_page import BasePage
from Diplom_3.locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    order_list_tab = MainPageLocators.ORDER_LIST_TAB
    order_list_title = MainPageLocators.ORDER_LIST_TITLE
    constructor_tab = MainPageLocators.CONSTRUCTOR_TAB
    ingredient = MainPageLocators.INGREDIENT
    ingredient_details = MainPageLocators.INGREDIENT_DETAILS
    close_button = MainPageLocators.CLOSE_BUTTON
    modal_title = MainPageLocators.MODAL_TITLE
    counter = MainPageLocators.COUNTER
    constructor_element = MainPageLocators.CONSTRUCTOR_ELEMENT
    bun = MainPageLocators.BUN
    create_order_button = MainPageLocators.CREATE_ORDER_BUTTON
    order_modal = MainPageLocators.ORDER_MODAL

    @allure.step('Создаем метод, который переходи на вкладку "Лента заказаов" и получает заголовок страницы "Лента заказов"')
    def go_to_order_list(self):
        self.click_to_element(self.order_list_tab)
        return self.get_text_from_element(self.order_list_title)

    @allure.step('Создаем метод, который переходи на вкладку "Конструктор" и получает текст кнопки "Оформить заказ')
    def go_to_constructor(self):
        self.click_to_element(self.order_list_tab)
        self.click_to_element(self.constructor_tab)
        return self.get_text_from_element(self.create_order_button)

    @allure.step('Создаем метод, который переходит на вкладку "Лента заказаов" и получает заголовок страницы "Лента заказов"')
    def get_ingredient_details(self):
        self.click_to_element(self.ingredient)
        return self.get_text_from_element(self.ingredient_details)

    @allure.step('Создаем метод, который открывает модальное окно "Детали ингредиента" и закрыват его по нажатию крестика')
    def close_modal(self):
        self.click_to_element(self.ingredient)
        close_button = self.find_element_with_wait(self.close_button)
        close_button.click()
        element = self.find_element_with_wait(self.modal_title)
        self.wait_until_close(self.modal_title)

        return element.is_displayed()

    @allure.step('Создаем метод, который перемещает ингредиент в поле конструктора заказа и получает значение счетчика ингредиента')
    def get_counter(self):
        source_element = self.find_element_with_wait(self.bun)
        target_element = self.find_element_with_wait(self.constructor_element)

        self.drug_and_drop(source_element, target_element)

        return self.get_text_from_element(self.counter)

    @allure.step('Созжаем метод, который находит локатор с интгредиетом "булочка" и локатор "конструктор заказа".'
                 'Далее с помощью метода drug_and_drop, добавляем ингредиент в констуктора заказа, оформляем заказ'
                 'и закрываем модальное окно заказа. ')
    def create_order(self):
        source_element = self.find_element_with_wait(self.bun)
        target_element = self.find_element_with_wait(self.constructor_element)

        self.drug_and_drop(source_element, target_element)

        self.click_to_element(self.create_order_button)
        self.click_to_element(self.close_button)


    @allure.step('Создаем метод, который открывает модальное окно с идентификатором заказа и получает текст в модальном окне')
    def get_order(self):
        self.click_to_element(self.create_order_button)

        return self.get_text_from_element(self.order_modal)









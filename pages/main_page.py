import allure
from Diplom_3.pages.base_page import BasePage
from Diplom_3.locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    enter_to_account_button = MainPageLocators.ENTER_TO_ACCOUNT_BUTTON
    order_list_tab = MainPageLocators.ORDER_LIST_TAB
    constructor_tab = MainPageLocators.CONSTRUCTOR_TAB
    constructor_title = MainPageLocators.CONSTRUCTOR_TITLE
    personal_account = MainPageLocators.PERSONAL_ACCOUNT
    ingredient = MainPageLocators.INGREDIENT
    ingredient_details = MainPageLocators.INGREDIENT_DETAILS
    close_button = MainPageLocators.CLOSE_BUTTON
    modal_title = MainPageLocators.MODAL_TITLE
    counter = MainPageLocators.COUNTER
    constructor_element = MainPageLocators.CONSTRUCTOR_ELEMENT
    bun = MainPageLocators.BUN
    create_order_button = MainPageLocators.CREATE_ORDER_BUTTON
    order_modal = MainPageLocators.ORDER_MODAL
    order_number = MainPageLocators.ORDER_NUMBER

    @allure.step('Создаем метод, который выполняет клик по кнопке "Войти в аккаунт, для перехода на страницу авторизации')
    def go_to_log_in(self):
        self.click_to_element(self.enter_to_account_button)

    @allure.step('Создаем метод, который переходи на вкладку "Лента заказаов"')
    def go_to_order_list(self):
        self.click_to_element(self.order_list_tab)


    @allure.step('Создаем метод, который переходи на вкладку "Конструктор"')
    def go_to_constructor(self):
        self.click_to_element(self.constructor_tab)

    @allure.step('Создаем метод, который переходи на вкладку "Личный кабинет"')
    def go_to_personal_account(self):
        self.click_to_element(self.personal_account)

    @allure.step('Создаем метод, который переходи на вкладку "Конструктор" и получает текст кнопки "Оформить заказ')
    def get_constructor_title(self):
        self.click_to_element(self.order_list_tab)
        self.click_to_element(self.constructor_tab)
        return self.get_text_from_element(self.constructor_title)

    @allure.step('Создаем метод, который открывает модальное окно "Детали ингредиента" и возвращает текст, заголовка окна.')
    def get_ingredient_details(self):
        self.click_to_element(self.ingredient)
        return self.get_text_from_element(self.ingredient_details)

    @allure.step('Создаем метод, который открывает модальное окно "Детали ингредиента" и закрыват его по нажатию крестика')
    def close_modal(self):
        self.click_to_element(self.ingredient)
        self.click_to_element(self.close_button)
        element = self.find_element_with_wait(self.modal_title)
        self.wait_until_close(self.modal_title)

        return element.is_displayed()

    @allure.step('Создаем метод, который перемещает ингредиент в поле конструктора заказа и получает значение счетчика ингредиента')
    def get_counter(self):
        self.drug_and_drop(self.bun, self.constructor_element)

        return self.get_text_from_element(self.counter)

    @allure.step('Создаем метод, который перемещает ингредиент в поле конструктора заказа, нажимает на кнопку "Оформить заказ"'
        'и закрывает модальное окно.')
    def create_order(self):
        self.drug_and_drop(self.bun, self.constructor_element)
        self.click_to_element(self.create_order_button)
        self.click_to_element(self.close_button)



    @allure.step('Создаем метод, который открывает модальное окно с идентификатором заказа и получает текст в модальном окне')
    def get_order_modal(self):
        self.drug_and_drop(self.bun, self.constructor_element)
        self.click_to_element(self.create_order_button)

        return self.get_text_from_element(self.order_modal)

    @allure.step(
        'Создаем метод, который выполняет оформлнеие ногового закаказа, открывает модальное окно с идентификатором заказа'
        'получает текст элемента номера заказа и возвращает текст элемента.')
    def get_order_number(self):
        self.drug_and_drop(self.bun, self.constructor_element)
        self.click_to_element(self.create_order_button)
        self.click_to_element(self.close_button)

        return self.get_text_from_element(self.order_number)









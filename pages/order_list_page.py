import allure
from Diplom_3.pages.base_page import BasePage
from Diplom_3.pages.main_page import MainPage
from Diplom_3.locators.main_page_locators import MainPageLocators
from Diplom_3.locators.order_list_page_locators import OrderPageListLocators
from Diplom_3.locators.personal_account_page_locators import PersonalAccountLocators
class OrderListPage(BasePage):
    constructor_tab = MainPageLocators.CONSTRUCTOR_TAB
    personal_account = MainPageLocators.PERSONAL_ACCOUNT
    orders_history = PersonalAccountLocators.ORDERS_HISTORY
    order_list_tab = MainPageLocators.ORDER_LIST_TAB
    order_list_title = OrderPageListLocators.ORDER_LIST_TITLE
    order = OrderPageListLocators.ORDER
    order_modal = OrderPageListLocators.ORDER_MODAL
    order_from_history = PersonalAccountLocators.ORDER_FROM_HISTORY
    order_from_order_list = OrderPageListLocators.ORDER_FROM_ORDER_LIST
    all_time_orders = OrderPageListLocators.ALL_TIME_ORDERS
    today_orders = OrderPageListLocators.TODAY_ORDERS
    order_in_work = OrderPageListLocators.ORDER_IN_WORK

    def get_order_list_title(self):
        return self.get_text_from_element(self.order_list_title)

    @allure.step('Создаем метод, который переходи на вкладку "Лента заказаов", открывает модальное окно заказа и получает'
                 'текст в модальном окне')
    def get_order_modal(self):
         self.click_to_element(self.order)

         return self.get_text_from_element(self.order_modal)

    @allure.step('Создаем метод, который переходит в раздел "Личный кабинет", во вкладку "История заказов", получает'
                 'текст заказа, затем переходит во вкладку "Лента заказов" и получает текст заказа из списка, после чего,'
                 'возвращает сравнение текста заказа из вкладки "История заказа" и текста заказа из списка заказов')
    def get_order_list(self):
        return self.get_text_from_element(self.order_from_order_list)

    @allure.step('Создаем метод, который переходит на вкладку "Лента заказов", получает значение кол-ва заказов, за все время,'
                 'создает новый заказ и получает новое значение кол-ва заказов за все время, а затем возвращает сравнение, которое '
                 'показывает, что после выполнения нового заказа, значение кол-ва заказов за все время увеличивается')
    def get_all_time_orders(self):
        count_order = int(self.get_text_from_element(self.all_time_orders))

        return count_order

    @allure.step(
        'Создаем метод, который переходит на вкладку "Лента заказов", получает значение кол-ва заказов, за сегодня'
        'создает новый заказ и получает новое значение кол-ва заказов за сегодня, а затем возвращает сравнение, которое '
        'показывает, что после выполнения нового заказа, значение кол-ва заказов за сегодня увеличивается')
    def get_today_orders(self):
        main_page = MainPage(self.driver)
        self.click_to_element(self.order_list_tab)
        count_order_before = int(self.get_text_from_element(self.today_orders))
        self.click_to_element(self.constructor_tab)

        main_page.create_order()

        self.click_to_element(self.order_list_tab)
        count_order_after = int(self.get_text_from_element(self.today_orders))

        return count_order_after > count_order_before

    @allure.step(
        'Создаем метод, который создает новый заказ, переходит на вкладку "Лента заказов", получает текст нового заказа '
        'и текст в разделе в "В работе", а затем возвращает равенство текста двух элементов.')
    def get_order_in_work(self):
        main_page = MainPage(self.driver)
        main_page.create_order()
        self.click_to_element(self.order_list_tab)
        new_order = self.get_text_from_element(self.order_from_order_list)
        new_order_stripped = new_order.lstrip("#")
        order_in_work_locator = self.order_in_work

        #условное ожидание, когда значнеие локатора new_order_stripped, появится в локаторе order_in_work_locator
        self.to_be_present_in_element(order_in_work_locator, new_order_stripped)

        order_in_work = self.get_text_from_element(order_in_work_locator)

        return new_order_stripped == order_in_work








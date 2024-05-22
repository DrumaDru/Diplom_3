import allure
from Diplom_3.pages.base_page import BasePage
from Diplom_3.locators.order_list_page_locators import OrderPageListLocators
class OrderListPage(BasePage):
    order_list_title = OrderPageListLocators.ORDER_LIST_TITLE
    order = OrderPageListLocators.ORDER
    order_modal = OrderPageListLocators.ORDER_MODAL
    order_from_order_list = OrderPageListLocators.ORDER_FROM_ORDER_LIST
    all_time_orders = OrderPageListLocators.ALL_TIME_ORDERS
    today_orders = OrderPageListLocators.TODAY_ORDERS
    order_in_work = OrderPageListLocators.ORDER_IN_WORK

    @allure.step('Создаем метод, который возвращает текст заголовка страницы "Лента заказов".')
    def get_order_list_title(self):
        return self.get_text_from_element(self.order_list_title)

    @allure.step('Создаем метод, который открывает модальное окно заказа и получает текст в модальном окне.')
    def get_order_modal(self):
         self.click_to_element(self.order)

         return self.get_text_from_element(self.order_modal)

    @allure.step('Создаем метод, который возвращает текст заказа из списка заказов.')
    def get_order_list(self):
        return self.get_text_from_element(self.order_from_order_list)

    @allure.step('Создаем метод, который возвращает текст элемента количества заказаов за все время.')
    def get_all_time_orders(self):
        count_order = int(self.get_text_from_element(self.all_time_orders))

        return count_order

    @allure.step('Создаем метод, который возвращает текст элемента количества заказаов за сегодня.')
    def get_today_orders(self):
        count_order = int(self.get_text_from_element(self.today_orders))

        return count_order

    @allure.step('Создаем метод, который получает текст нового заказа и текст в разделе в "В работе", '
                 'а затем возвращает равенство текста двух элементов.')
    def get_order_in_work(self):
        new_order = self.get_text_from_element(self.order_from_order_list)
        new_order_stripped = new_order.lstrip("#")
        order_in_work_locator = self.order_in_work

        #условное ожидание, когда значнеие локатора new_order_stripped, появится в локаторе order_in_work_locator
        self.to_be_present_in_element(order_in_work_locator, new_order_stripped)

        order_in_work = self.get_text_from_element(order_in_work_locator)

        return new_order_stripped == order_in_work








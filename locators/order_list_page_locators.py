from selenium.webdriver.common.by import By
class OrderPageListLocators:
    ORDER_LIST_TITLE =(By.XPATH, ".//h1[text() = 'Лента заказов']")
    ORDER = (By.XPATH, ".//div[@class = 'OrderFeed_contentBox__3-tWb']/ul/li[1]")
    ORDER_MODAL = (By.XPATH, ".//p[@class = 'text text_type_main-medium mb-8' and text() = 'Cостав']")
    ORDER_FROM_ORDER_LIST = (By.XPATH, ".//div[@class = 'OrderFeed_contentBox__3-tWb']/ul/li[1]/a/div/p[@class = 'text text_type_digits-default']")
    ALL_TIME_ORDERS = (By.XPATH, ".//div/p[text() = 'Выполнено за все время:']/"
                                 "following-sibling::p[@class = 'OrderFeed_number__2MbrQ text text_type_digits-large']")
    TODAY_ORDERS = (By.XPATH, ".//div/p[text() = 'Выполнено за сегодня:']/"
                              "following-sibling::p[@class = 'OrderFeed_number__2MbrQ text text_type_digits-large']")
    ORDER_IN_WORK = (By.XPATH, ".//div[@class = 'OrderFeed_orderStatusBox__1d4q2 mb-15']/"
                               "ul[@class = 'OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']")
    
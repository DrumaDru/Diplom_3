from selenium.webdriver.common.by import By

class PersonalAccountLocators:
    PROFILE_TAB = (By.XPATH, ".//li[@class = 'Account_listItem__35dAP']/a[text() = 'Профиль']")
    ORDERS_HISTORY = (By.XPATH, ".//li[@class = 'Account_listItem__35dAP']/a[text() = 'История заказов']")
    EXIT_TAB = (By.XPATH, ".//button[contains(@class, 'Account_button__14Yp3') and contains(text(), 'Выход')]")
    ORDER_FROM_HISTORY = (By.XPATH, ".//div[@class = 'OrderHistory_orderHistory__qy1VB']/ul/li[1]//p[@class = 'text text_type_digits-default']")
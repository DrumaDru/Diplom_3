from selenium.webdriver.common.by import By

class PasswordRecoveryPageLocators:
    RECOVERY_PASSWORD_BUTTON = (By.XPATH, ".//form/button[text()= 'Восстановить']")
    SAVE_BUTTON = (By.XPATH, ".//div[@class = 'Auth_login__3hAey']//button[text() = 'Сохранить']")
    EMAIL_INPUT = (By.XPATH, ".//input[@class = 'text input__textfield text_type_main-default']")
    HIDE_ICON =(By.XPATH, ".//div[@class ='input__icon input__icon-action']//*")
    PASS_INPUT_TYPE = (By.XPATH, ".//div/input[@class = 'text input__textfield text_type_main-default' and @name = 'Введите новый пароль']")
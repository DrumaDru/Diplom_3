from selenium.webdriver.common.by import By

class StartPageLocators:
    INPUT_EMAIL_LOGIN = (By.XPATH, ".//*[text()='Email']/following-sibling::input")
    INPUT_PASSWORD_LOGIN = (By.XPATH, ".//*[text()='Пароль']/following-sibling::input")
    ENTER_BUTTON_LOGIN = (By.XPATH, ".//button[text()='Войти']")
    RECOVERY_PASSWORD_LINK = (By.XPATH, ".//a[@class = 'Auth_link__1fOlj' and text() = 'Восстановить пароль']")

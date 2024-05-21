import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import Firefox, Chrome
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
import test_data
import requests
from Diplom_3.pages.base_page import BasePage
from Diplom_3.locators.main_page_locators import MainPageLocators
from Diplom_3.locators.start_page_locators import StartPageLocators
from selenium.webdriver.common.action_chains import ActionChains




@pytest.fixture(scope="function", params=["chrome", "firefox"])
def driver(request):
     if request.param == "chrome":
         options = ChromeOptions()
         options.add_argument('--window-size=1920,1080')
         driver = webdriver.Chrome(options=options)
     elif request.param == "firefox":
         options = FirefoxOptions()
         options.add_argument('--window-size=1920,1080')
         driver = webdriver.Firefox(options=options)
     else:
         raise ValueError("Unsupported browser")
    # Открываем веб-страницу
     driver.get("https://stellarburgers.nomoreparties.site/")
     yield driver
    # Закрываем браузер после завершения теста
     driver.quit()


@pytest.fixture(scope="function")
def registration_user_data():
    payload = test_data.payload
    email = test_data.payload["email"]
    requests.post(f"{test_data.curl}/api/auth/register", data=payload)
    return email


# @pytest.fixture(scope="function")
# def log_in(driver, registration_user):
#     base_page = BasePage(driver)
#     email = registration_user
#     password = test_data.payload["password"]
#     enter_to_account = MainPageLocators.ENTER_TO_ACCOUNT_BUTTON
#     input_email_login = StartPageLocators.INPUT_EMAIL_LOGIN
#     input_password_login = StartPageLocators.INPUT_PASSWORD_LOGIN
#     enter_button_login = StartPageLocators.ENTER_BUTTON_LOGIN
#
#     base_page.click_to_element(enter_to_account)
#     base_page.add_text_to_element(input_email_login, email)
#     base_page.add_text_to_element(input_password_login, password)
#     base_page.click_to_element(enter_button_login)

# @pytest.fixture(scope="function")
# def create_order(driver):
#     base_page = BasePage(driver)
#     action_chains = ActionChains(driver)
#     source_element = base_page.find_element_with_wait(MainPageLocators.BUN)
#     target_element = base_page.find_element_with_wait(MainPageLocators.CONSTRUCTOR_ELEMENT)
#     create_order = MainPageLocators.CREATE_ORDER_BUTTON
#     close_button = MainPageLocators.CLOSE_BUTTON
#
#     action_chains.drag_and_drop(source_element, target_element).perform()
#     base_page.click_to_element(create_order)
#     base_page.click_to_element(close_button)







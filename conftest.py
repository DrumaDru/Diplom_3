import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import Firefox, Chrome
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
import test_data
import requests
from Diplom_3.locators.main_page_locators import MainPageLocators
from Diplom_3.locators.start_page_locators import StartPageLocators
from selenium.webdriver.common.action_chains import ActionChains


# @pytest.fixture(scope="function")
# def driver():
#     options = ChromeOptions()
#     options.add_argument('--window-size=1920,1080')
#     driver = webdriver.Chrome(options=options)
#     #Открываем веб-страницу
#     driver.get("https://stellarburgers.nomoreparties.site/")
#     yield driver
#     #выходим из браузера
#     driver.quit()


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
def registration_user():
    payload = test_data.payload
    email = test_data.payload["email"]
    requests.post(f"{test_data.curl}/api/auth/register", data=payload)
    return email


@pytest.fixture(scope="function")
def log_in(driver, registration_user):
    email = registration_user
    WebDriverWait(driver, 30).until(
        expected_conditions.visibility_of_element_located(MainPageLocators.ENTER_TO_ACCOUNT_BUTTON))
    enter_to_account = driver.find_element(*MainPageLocators.ENTER_TO_ACCOUNT_BUTTON)
    enter_to_account.click()
    WebDriverWait(driver, 30).until(
        expected_conditions.visibility_of_element_located(StartPageLocators.INPUT_EMAIL_LOGIN))
    input_email_login = driver.find_element(*StartPageLocators.INPUT_EMAIL_LOGIN)
    input_email_login.send_keys(email)
    input_password_login = driver.find_element(*StartPageLocators.INPUT_PASSWORD_LOGIN)
    password = test_data.payload["password"]
    input_password_login.send_keys(password)
    enter_button_login = driver.find_element(*StartPageLocators.ENTER_BUTTON_LOGIN)
    enter_button_login.click()

@pytest.fixture(scope="function")
def create_order(driver):
    action_chains = ActionChains(driver)
    WebDriverWait(driver, 15).until(
        expected_conditions.visibility_of_element_located(MainPageLocators.BUN))
    source_element = driver.find_element(*MainPageLocators.BUN)
    target_element = driver.find_element(*MainPageLocators.CONSTRUCTOR_ELEMENT)
    action_chains.drag_and_drop(source_element, target_element).perform()
    create_order = driver.find_element(*MainPageLocators.CREATE_ORDER_BUTTON)
    create_order.click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(MainPageLocators.CLOSE_BUTTON))
    close_button = driver.find_element(*MainPageLocators.CLOSE_BUTTON)
    close_button.click()







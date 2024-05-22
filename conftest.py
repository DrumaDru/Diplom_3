import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import Firefox, Chrome
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
import test_data
import requests




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








import pytest
from Diplom_3.pages.start_page import StartPage
from Diplom_3.pages.recovery_pass_page import RecoveryPassPage
import time

class TestPassword:


     def test_recovery_pass_link(self, driver):
          start_page = StartPage(driver)
          result = start_page.recovery_pass_link()

          assert result == "Восстановить"


    def test_recovery_pass_email_input(self, driver, registration_user):
         recovery_pass_page = RecoveryPassPage(driver)
         email = registration_user
         result = recovery_pass_page.recovery_pass_email_input(email)

         assert result == "Сохранить"


    def test_click_hide_icon(self, driver, registration_user):
        recovery_pass_page = RecoveryPassPage(driver)
        email = registration_user
        result = recovery_pass_page.click_hide_icon(email)
        assert result == 'text'


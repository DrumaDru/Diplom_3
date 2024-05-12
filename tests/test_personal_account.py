import pytest
from Diplom_3.pages.personal_account_page import PersonalAccount



class TestPersonalAccount:

    # def test_personal_account(self, driver, log_in):
    #      personal_account = PersonalAccount(driver)
    #      result = personal_account.go_to_personal_account()
    #
    #      assert result == "Профиль"

    # def test_go_to_orders_history(self, driver, log_in):
    #      personal_account = PersonalAccount(driver)
    #      result = personal_account.go_to_orders_history()
    #
    #      assert "Account_link_active" in result

    def test_exit_from_account(self, driver, log_in):
        personal_account = PersonalAccount(driver)
        result = personal_account.exit_from_account()

        assert result == "Войти"


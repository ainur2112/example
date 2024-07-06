import pytest
import allure
from base.base_test import BaseTest
from pages.login_page import LoginPage
@allure.feature("invalid authorization page")
class TestInvalidAutorization(BaseTest):

    """check auth page with invalids creds"""
    @pytest.mark.parametrize('creds', LoginPage.generate_pairs())
    @allure.title("Change profile name")
    @allure.severity("Critical")
    @pytest.mark.regression
    def test_invalid_autorization(self, creds):
        login, password = creds
        self.login_page.open()
        self.login_page.enter_login(login)
        self.login_page.enter_password(password)
        self.login_page.click_submit_button()
        self.login_page.check_visible_alert_notification()


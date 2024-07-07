import pytest
import allure
from base.base_test import BaseTest
from pages.login_page import LoginPage
from config.data import Data
@allure.feature("invalid authorization page")
class TestInvalidAutorization(BaseTest):

    INVALID_LOGINS = Data.INVALID_LOGINS.split(',')
    INVALID_PASSWORDS = Data.INVALID_PASSWORDS.split(',')

    """check auth page with invalids creds"""


    @pytest.mark.parametrize('creds', LoginPage.generate_pairs(INVALID_LOGINS, INVALID_PASSWORDS))
    @allure.title("Change profile name")
    @allure.severity("Critical")
    def test_invalid_autorization(self, creds):
        login, password = creds
        self.login_page.open()
        self.login_page.is_opened()
        self.login_page.enter_login(login)
        self.login_page.enter_password(password)
        self.login_page.click_submit_button()
        self.login_page.check_visible_alert_notification()



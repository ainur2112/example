import allure
import pytest
from base.base_test import BaseTest

@allure.feature("navigate mouse on menu")
class TestMouseNavigateOnMenu(BaseTest):

    """check navigate mouse on menu"""

    @allure.title("Navigete mouse on menu")
    @allure.severity("Low")
    def test_navigate_on_menu(self):
        self.login_page.open()
        self.login_page.is_opened()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.navigate_on_pim()
        self.dashboard_page.navigate_on_my_info()
        self.dashboard_page.navigate_on_leave()
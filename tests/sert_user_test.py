import allure
from base.base_test import BaseTest

@allure.feature("Add user functioanality")
class TestProfileFeature(BaseTest):


    @allure.title("Add user")
    @allure.severity("Critical")
    def test_search_user(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_admin_menu()
        self.admin_page.is_opened()
        self.admin_page.fill_value_username()
        self.admin_page.click_search_button()
        self.admin_page.check_existence_entry()


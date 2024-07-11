import allure
from faker import Faker
from base.base_test import BaseTest

@allure.feature("Profile Functioanality")
class TestProfileFeature(BaseTest):

    """Сделал экземляр класса Faker на русском"""
    fake = Faker('ru_RU')

    @allure.title("Change profile name")
    @allure.severity("Critical")
    def test_changed_profile(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_and_fill_search_menu("My Info")
        self.dashboard_page.click_my_info_link()
        self.personal_page.is_opened()
        firstname = self.personal_page.change_first_name(self.fake.first_name_male())
        middlename = self.personal_page.change_middle_name(self.fake.middle_name_male())
        lastname = self.personal_page.change_last_name(self.fake.last_name_male())
        self.personal_page.save_changes()
        self.personal_page.is_changes_saved(firstname, middlename, lastname)
        self.login_page.make_screenshot("Success")

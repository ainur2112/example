import allure
import pytest
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from locators.locators_login_page import LoginPageLocators

class LoginPage(BasePage):

    PAGE_URL = Links.LOGIN_PAGE

    @allure.step("Enter login")
    def enter_login(self, login):
        login_user = self.clickable_and_return_element(LoginPageLocators.USERNAME_FIELD)
        login_user.send_keys(login)

    @allure.step("Enter password")
    def enter_password(self, password):
        password_user = self.clickable_and_return_element(LoginPageLocators.PASSWORD_FIELD)
        password_user.send_keys(password)

    @allure.step("Click submit button")
    def click_submit_button(self):
        auth_button = self.clickable_and_return_element(LoginPageLocators.SUBMIT_BUTTON)
        auth_button.click()

    def check_visible_alert_notification(self):
        self.wait.until(EC.text_to_be_present_in_element(LoginPageLocators.INVALID_CREDS_TEXT, "Invalid credentials"))


    """Generate pairs for invalid auth page"""
    def generate_pairs(logins, passwords):


        pairs = []
        for login in logins:
            for password in passwords:
                pairs.append(pytest.param((login, password), id=f'{login}, {password}'))
        return pairs
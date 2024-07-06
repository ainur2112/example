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
        self.wait.until(EC.element_to_be_clickable(LoginPageLocators.USERNAME_FIELD)).send_keys(login)

    @allure.step("Enter password")
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(LoginPageLocators.PASSWORD_FIELD)).send_keys(password)

    @allure.step("Click submit button")
    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(LoginPageLocators.SUBMIT_BUTTON)).click()

    def check_visible_alert_notification(self):
        self.wait.until(EC.text_to_be_present_in_element(LoginPageLocators.INVALID_CREDS_TEXT, "Invalid credentials"))


    """Generate pairs for invalid auth page"""
    def generate_pairs():

        """input parameters for the function generate_pairs"""
        logins = ['invalid_login_0', 'invalid_login_1', 'invalid_login_2']
        passwords = ['invalid_password_0', 'invalid_password_1', 'invalid_password_2']

        pairs = []
        for login in logins:
            for password in passwords:
                pairs.append(pytest.param((login, password), id=f'{login}, {password}'))
        return pairs
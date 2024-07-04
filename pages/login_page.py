import allure
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
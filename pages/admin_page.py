import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from locators.locators_admin_page import AdminPageLocators

class AdminPage(BasePage):
    """Страница админа"""

    PAGE_URL = Links.ADMIN_PAGE

    def click_add_button(self):
        self.button.do_click(AdminPageLocators.ADD_BUTTON).click()



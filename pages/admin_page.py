import allure
from base.base_page import BasePage
from config.links import Links
from locators.locators_admin_page import AdminPageLocators

class AdminPage(BasePage):
    """Страница админа"""

    PAGE_URL = Links.ADMIN_PAGE

    def click_add_button(self):
        self.find_element(AdminPageLocators.ADD_BUTTON)
        self.do_click(AdminPageLocators.ADD_BUTTON)



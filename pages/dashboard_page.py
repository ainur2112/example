import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from locators.locators_dashboard_page import DashboardPageLocators

class DashboardPage(BasePage):

    PAGE_URL = Links.DASHBOARD_PAGE

    @allure.step("Click and fill  Search field ")
    def click_and_fill_search_menu(self,name_menu):
        search_field = self.wait.until(EC.element_to_be_clickable(DashboardPageLocators.SEARCH_FIELD))
        search_field.click()
        search_field.send_keys(name_menu)

    def click_admin_menu(self):
        self.wait.until((EC.element_to_be_clickable(DashboardPageLocators.ADMIN_SPAN))).click()


    @allure.step("Click on 'My Info' link")
    def click_my_info_link(self):
        self.button.do_click(DashboardPageLocators.MY_INFO_SPAN)

    @allure.step("Navigate mouse on 'My Info' ")
    def navigate_on_my_info(self):
        self.visible_element(DashboardPageLocators.MY_INFO_SPAN)
        self.button.navigate_mouse_on_element(DashboardPageLocators.MY_INFO_SPAN)

    @allure.step("Navigate mouse on 'PIM' ")
    def navigate_on_pim(self):
        self.visible_element(DashboardPageLocators.PIM_SPAN)
        self.button.navigate_mouse_on_element(DashboardPageLocators.PIM_SPAN)

    @allure.step("Navigate mouse on 'Leave' ")
    def navigate_on_leave(self):
        self.visible_element(DashboardPageLocators.Leave_SPAN)
        self.button.navigate_mouse_on_element(DashboardPageLocators.Leave_SPAN)



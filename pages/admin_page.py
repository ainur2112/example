import allure
from base.base_page import BasePage
from config.links import Links
from locators.locators_admin_page import AdminPageLocators

class AdminPage(BasePage):
    """Страница админа"""

    PAGE_URL = Links.ADMIN_PAGE

    """ Заполнение значением поля "Username """
    @allure.step("Fill value username")
    def fill_value_username(self):
        self.find_element(AdminPageLocators.USER_NAME_INPUT).send_keys("FMLName")

    """ Нажатие на кнопку Seartch """
    @allure.step("Clicl on button Search button")
    def click_search_button(self):
        self.do_click(AdminPageLocators.SEARCH_BUTTON)


    """  Проверка на наличие записи с текстом FMLName """
    @allure.step("Check existence entry with value FMLName")
    def check_existence_entry(self):
        assert self.find_element(AdminPageLocators.CHECK_EXISTENCE_ENTRY).text == "FMLName"

    @allure.step("Scroll to bottom link of page")
    def scroll_to_bottom_limk_of_page(self):
        self.scroll_to_element(AdminPageLocators.BOTTOM_LINK_OF_PAGE)



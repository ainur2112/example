import time
import allure
from selenium.webdriver import Keys

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from locators.locators_personal_page import PersonalPageLocators

class PersonalPage(BasePage):

    PAGE_URL = Links.PERSONAL_PAGE

    def change_first_name(self, first_name: str) -> str:
        with allure.step(f"Changing the value in the first name to'{first_name}'"):
            first_name_field = self.wait_clickable_element(PersonalPageLocators.FIRST_NAME_FIELD)
            self.clear(PersonalPageLocators.FIRST_NAME_FIELD)
            first_name_field.send_keys(first_name)
            return first_name

    def change_middle_name(self, middle_name: str) -> str:
        with allure.step(f"Changing the value in the middle name to'{middle_name}'"):
            first_name_field = self.wait_clickable_element(PersonalPageLocators.MIDDLE_NAME_FIELD)
            self.clear(PersonalPageLocators.MIDDLE_NAME_FIELD)
            first_name_field.send_keys(middle_name)
            return middle_name

    def change_last_name(self, last_name: str) -> str:
        with allure.step(f"Changing the value in the last name to'{last_name}'"):
            first_name_field = self.wait_clickable_element(PersonalPageLocators.LAST_NAME_FIELD)
            self.clear(PersonalPageLocators.LAST_NAME_FIELD)
            first_name_field.send_keys(last_name)
            return last_name

    @allure.step("Save changes")
    def save_changes(self):
        self.wait.until(EC.invisibility_of_element_located(PersonalPageLocators.SPINNER))
        self.wait.until(EC.element_to_be_clickable(PersonalPageLocators.SAVE_BUTTON)).click()

    @allure.step("Changes has been saved  successfully")
    def is_changes_saved(self, new_first_name=str, new_middle_name=str, new_last_name=str):
        self.wait.until(EC.invisibility_of_element_located(PersonalPageLocators.SPINNER))
        self.visibility_of_element(PersonalPageLocators.FIRST_NAME_FIELD)
        self.wait.until(EC.text_to_be_present_in_element_value(PersonalPageLocators.FIRST_NAME_FIELD, new_first_name))
        self.wait.until(EC.text_to_be_present_in_element_value(PersonalPageLocators.MIDDLE_NAME_FIELD, new_middle_name))
        self.wait.until(EC.text_to_be_present_in_element_value(PersonalPageLocators.LAST_NAME_FIELD, new_last_name))




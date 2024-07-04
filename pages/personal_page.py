import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from locators.locators_personal_page import PersonalPageLocators

class PersonalPage(BasePage):

    PAGE_URL = Links.PERSONAL_PAGE

    def change_name(self, new_name):
        with allure.step(f"Change name on '{new_name}'"):
            first_name_field = self.wait.until(EC.element_to_be_clickable(PersonalPageLocators.FIRST_NAME_FIELD))
            self.driver.find_element(*PersonalPageLocators.FIRST_NAME_FIELD).clear()
            first_name_field.send_keys(new_name)
            self.name = new_name

    @allure.step("Save changes")
    def save_changes(self):
        self.wait.until(EC.element_to_be_clickable(PersonalPageLocators.SAVE_BUTTON)).click()

    @allure.step("Changes has been saved successfully")
    def is_changes_saved(self):
        self.wait.until(EC.invisibility_of_element_located(PersonalPageLocators.SPINNER))
        self.wait.until(EC.visibility_of_element_located(PersonalPageLocators.FIRST_NAME_FIELD))
        self.wait.until(EC.text_to_be_present_in_element_value(PersonalPageLocators.FIRST_NAME_FIELD, self.name))


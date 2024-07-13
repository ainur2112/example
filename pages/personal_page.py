import os
import time

import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from locators.locators_personal_page import PersonalPageLocators
from config.data import Data

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
        self.element_is_not_visible(PersonalPageLocators.SPINNER)
        self.do_click(PersonalPageLocators.SAVE_BUTTON)

    @allure.step("Changes has been saved  successfully")
    def is_changes_saved(self, new_first_name=str, new_middle_name=str, new_last_name=str):
        self.element_is_not_visible(PersonalPageLocators.SPINNER)
        self.wait.until(EC.text_to_be_present_in_element_value(PersonalPageLocators.FIRST_NAME_FIELD, new_first_name))
        self.wait.until(EC.text_to_be_present_in_element_value(PersonalPageLocators.MIDDLE_NAME_FIELD, new_middle_name))
        self.wait.until(EC.text_to_be_present_in_element_value(PersonalPageLocators.LAST_NAME_FIELD, new_last_name))

    @allure.step("click on contact details")
    def click_on_contact_details(self):
        self.do_click(PersonalPageLocators.CONTACT_DETAILS)


    """Добавление файла формата pdf"""
    @allure.step("add file pdf")
    def add_file_pdf(self):
        self.do_click(PersonalPageLocators.ADD_BUTTON)
        self.file_input(os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', 'config', 'files_for_test', 'example.pdf')))
        assert self.find_element(PersonalPageLocators.CHECK_ADD_FILE_DIV).text == 'example.pdf'


    """Добавление файла формата doc"""
    @allure.step("add file doc")
    def add_file_doc(self):
        self.file_input(os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', 'config', 'files_for_test', 'example.doc')))
        assert self.find_element(PersonalPageLocators.CHECK_ADD_FILE_DIV).text == 'example.doc'


    """Добавление файла формата jpeg"""
    @allure.step("add file jpeg")
    def add_file_jpeg(self):
        self.file_input(os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', 'config', 'files_for_test', 'example.jpeg')))
        assert self.find_element(PersonalPageLocators.CHECK_ADD_FILE_DIV).text == 'example.jpeg'

    @allure.step("add comment in textarea")
    def add_comment_textarea(self):
        """
        Добавление комментария и проверка его наличия в textarea
        """

        self.find_element(PersonalPageLocators.COMMENT_TEXTAREA).send_keys(Data.SECRET_COMMENT)
        self.wait.until(EC.text_to_be_present_in_element_value(PersonalPageLocators.COMMENT_TEXTAREA, Data.SECRET_COMMENT))

    @allure.step("click on file save button")
    def click_on_file_save_button(self):
        """
         Клик на кнопку,которая сохраняет добавленный файл
        """
        self.do_click(PersonalPageLocators.FILE_SAVE_BUTTON)

    @allure.step("Checking if the success notification appears")
    def check_succes_notification_visible(self):
        assert self.find_element(PersonalPageLocators.SUCCESSFULLY_NOTIFICATION_VALUE).text == 'Success'
        self.element_is_not_visible(PersonalPageLocators.SUCCESSFULLY_NOTIFICATION_VALUE)

    @allure.step("checking that an entry has been added")
    def check_add_entry_with_file(self):
        assert self.find_element(PersonalPageLocators.DIV_WITH_SECRET_COMMENT).text == 'SECRET_COMMENT'

    @allure.step("Delete entry with file ")
    def delete_entry_with_file(self):
        self.do_click(PersonalPageLocators.DELETE_BUTTON)
        self.do_click(PersonalPageLocators.ACCEPT_DELETE_BUTTON)
        self.element_is_not_visible(PersonalPageLocators.DIV_WITH_SECRET_COMMENT)




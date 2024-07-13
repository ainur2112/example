import allure
from base.base_test import BaseTest

@allure.feature("Contact details Functioanality")
class TestAddAttachmentInContactDetails(BaseTest):

    @allure.title("Add contact details name")
    @allure.severity("Critical")
    def test_add_attachment_in_contact_details(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info_link()
        self.personal_page.is_opened()
        self.personal_page.click_on_contact_details()
        self.personal_page.add_file_pdf()
        self.personal_page.add_comment_textarea()
        self.personal_page.click_on_file_save_button()
        self.personal_page.check_succes_notification_visible()
        self.personal_page.check_add_entry_with_file()
        self.personal_page.delete_entry_with_file()
        self.admin_page.scroll_to_bottom_limk_of_page()

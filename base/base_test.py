import pytest

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.personal_page import PersonalPage
from pages.admin_page import AdminPage
from config.data import Data

class BaseTest:
    """Наследуемый класс при запуске тестов"""

    login_page: LoginPage
    dashboard_page: DashboardPage
    personal_page: PersonalPage
    admin_page: AdminPage
    data: Data

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()
        request.cls.login_page = LoginPage(driver)
        request.cls.dashboard_page = DashboardPage(driver)
        request.cls.personal_page = PersonalPage(driver)
        request.cls.admin_page = AdminPage(driver)


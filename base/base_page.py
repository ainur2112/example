import allure
from selenium.common.exceptions import (ElementClickInterceptedException,StaleElementReferenceException)
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.remote.webelement import WebElement
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

class BasePage:

    """Основной класс от которого наследуемся"""


    def __init__(self, driver):
        """Инициализация драйвера"""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    def open(self):
        """Открытии страницы"""
        with allure.step(f"Open {self.PAGE_URL} page"):
            self.driver.get(self.PAGE_URL)

    def is_opened(self):
        """Проверка, открылась ли конкретная страница"""
        with allure.step(f"Page {self.PAGE_URL} is opened"):
            self.wait.until(EC.url_to_be(self.PAGE_URL))

    def make_screenshot(self,screenshot_name):
        """Делает скриншот"""
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )

    def visibility_of_element(self, by_locator: tuple, wait_time=10) -> WebElement:
        """ Ожидает, когда элемент появится в DOM странице
             и возвращает найденный элемент"""
        element = WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(by_locator))
        return element

    def wait_clickable_element(self, by_locator: tuple, wait_time=10) -> WebElement:
        """ Ожидает, когда элемент будет кликабельным
                     и возвращает найденный элемент"""
        with allure.step("Waits for the element to be clickable"):
            element = WebDriverWait(self.driver, wait_time).until(EC.element_to_be_clickable(by_locator))
            return element

    def clear(self, by_locator: tuple, wait_time=10):
        """Функция для удалении данных с поля"""
        with allure.step("Deletes the value in the field"):
            element = WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(by_locator))
            time.sleep(1)
            element.send_keys(Keys.CONTROL + "A")
            element.send_keys(Keys.BACKSPACE)


    def navigate_mouse_on_element(self, by_locator: tuple):
        """
        Навигация мышкой по элементам

        :param by_locator:
            локатор элемента

        """
        with allure.step(f"navigate mouse on element: {by_locator}"):
            element = self.driver.find_element(*by_locator)
            actions = AC(self.driver)
            actions.move_to_element(element)
            actions.perform()

    def do_click(self, by_locator:tuple, wait_time: int = 10):
        """
        Клик на элемент
        :param by_locator:
            элемент

        :param wait_time:
            время ожидания

        """
        with allure.step(f"Click on element: {by_locator}"):
            elem = WebDriverWait(self.driver, wait_time).until(EC.element_to_be_clickable(by_locator))
            try:
                elem.click()
            except (StaleElementReferenceException, ElementClickInterceptedException):
                self.driver.execute_script("arguments[0].click()", elem)

    def action_click_send_keys_and_enter(self, by_locator: tuple, text_str: str, wait_time: int = 4):
        """
        Клик, введение данных в поле и нажатие ENTER

        :param by_locator:
            локатор элемента
        :param text_str:
            значение, которое нужно отправить в элемент
        :param wait_time:
            время ожидания

        """
        with allure.step(f"Click on element: {by_locator}  and enter"):
            element = WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(by_locator))
            actions = AC(self.driver)
            actions.move_to_element(element).click().send_keys(text_str).pause(1).key_down(Keys.ENTER).key_up(Keys.ENTER). \
                perform()
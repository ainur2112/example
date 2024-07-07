import allure
from selenium.common.exceptions import (ElementClickInterceptedException,StaleElementReferenceException)
from selenium.webdriver.common.action_chains import ActionChains as AC
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    def open(self):
        with allure.step(f"Open {self.PAGE_URL} page"):
            self.driver.get(self.PAGE_URL)

    def is_opened(self):
        with allure.step(f"Page {self.PAGE_URL} is opened"):
            self.wait.until(EC.url_to_be(self.PAGE_URL))

    def make_screenshot(self,screenshot_name):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )

    def visible_and_return_return_element(self, by_locator: tuple):
        self.wait.until(EC.visibility_of(self.driver.find_element(*by_locator)))
        element = self.driver.find_element(*by_locator)
        return element

    def clickable_and_return_element(self, by_locator: tuple):
        self.wait.until(EC.element_to_be_clickable(self.driver.find_element(*by_locator)))
        element = self.driver.find_element(*by_locator)
        return element

    def clear(self, by_locator: tuple, wait_time=10):
        """Function for clear field"""
        element = WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located(by_locator))
        time.sleep(1)
        element.send_keys(Keys.CONTROL + "A")
        element.send_keys(Keys.BACKSPACE)


    def navigate_mouse_on_element(self, by_locator: tuple):
        """
        Навигация мышкой по элементам

        :param by_locator:
            локатор элемента

        """

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

        element = WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(by_locator))
        actions = AC(self.driver)
        actions.move_to_element(element).click().send_keys(text_str).pause(1).key_down(Keys.ENTER).key_up(Keys.ENTER). \
            perform()
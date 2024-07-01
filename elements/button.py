from selenium.common.exceptions import (ElementClickInterceptedException,StaleElementReferenceException)
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Button:
    """Класс, описвыающий действия с кнопками на страницах"""

    def __init__(self, driver) -> None:
        self.driver = driver

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


    def double_click(self, by_locator: tuple):
        """
        Двойной клик по элементу

        :param by_locator:
            локатор элемента

        """

        element = self.driver.find_element(*by_locator)
        actions = AC(self.driver)
        actions.double_click(element)
        actions.perform()

    def press_button_escape(self):
        """ Нажатие кнопки ESCAPE """

        actions = AC(self.driver)
        actions.key_down(Keys.ESCAPE).pause(1).key_up(Keys.ESCAPE).perform()
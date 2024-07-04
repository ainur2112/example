import time

from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import  WebDriverWait


class Field:
    """ Класс, описывающий действия с полями на страницах """
    def __init__(self, driver) -> None:
        self.driver = driver

    def do_send_keys(self, by_locator: tuple, input_value: str, wait_time=5):
        """
        Отправка значения в элемент

        :param by_locator:
            локатор элемента
        :param input_value:
            Значение,которое нужно внести
        :param wait_time:
            время ожидания

        """

        WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(by_locator)).send_keys(input_value)

    def do_clear(self, by_locator: tuple):
        """
        Очищение поля

        :param by_locator:
            локатор элемента

        """

        element = self.driver.find_element(*by_locator)
        element.clear()

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

    def action_click_send_keys(self, by_locator: tuple, text_str: str, wait_time: int = 4):
        """
        Клик и введение данных в поле

        :param by_locator:
            локатор элемента

        :param text_str:
             текст, который нужно ввести
        :param wait_time:
            ожидание

        """

        element = WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located(by_locator))
        actions = AC(self.driver)
        actions.move_to_element(element).send_keys(text_str).pause(1).perform()
        time.sleep(wait_time)


    def paste_from_clipboard(self, by_locator: tuple):
        """
        Ввод текста из буффера обмена в поле

        :param by_locator:
            Локатор поля

        """

        self.driver.find_element(*by_locator).send_keys(Keys.CONTROL + 'v')
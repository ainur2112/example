import time

from selenium.common.exceptions import (TimeoutException,
                                        ElementClickInterceptedException,
                                        StaleElementReferenceException)
from selenium.webdriver.common.by import By


class DropDown:
    """ Класс, описывающий действия с dropdown листами на страницах """

    def __init__(self, driver) -> None:
        self.driver = driver


    def fill_dropdown_list(self,
                           list_locator: tuple,
                           search_text: str,
                           result=None,
                           wait_time: int = 1,
                           index: int = 1):

        """
        Заполнение выпадающих списков на странице

        :param list_locator:
            локатор списка
        :param search_text:
            значение, которое вводится в поле

        :param result:
            Результат в выпадающем списке. По-умолчанию None, если локатор элемента отличается от стандартного span,
            то передать другой локатор
        :param wait_time:
            время ожидания
        :param index:
            индекс элемента

        """

        result_elem = ""

        match result:
            case None:
                result_elem = (By.XPATH, f"(//span[contains(.,'{search_text}')])[{index}]")

            case 'li':
                result_elem = (By.XPATH, f"//li[contains(.,'{search_text}')]")

            case _:
                result_elem = result

        locator = self.driver.find_visible(list_locator)

        try:
            locator.click()
            time.sleep(0.5)
            self.driver.do_send_keys(list_locator, input_value=search_text)
        except(ElementClickInterceptedException, StaleElementReferenceException):
            time.sleep(wait_time)
            print("Ждем подгрузки поля")
            self.driver.do_click(list_locator) \
                .scroll_to_elem(result_elem) \
                .do_send_keys(list_locator, input_value=search_text)
        try:
            # time.sleep(wait_time)
            self.driver.find_visible(result_elem) \
                .scroll_to_elem(result_elem)  \
                .do_click(result_elem)
        except TimeoutException:
            print("Значения из списка не прогрузилась")
            self.driver.select_and_delete(list_locator) \
                .action_click_send_keys_and_enter(list_locator, search_text)


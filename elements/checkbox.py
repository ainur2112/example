import time




class Checkbox:
    """ Класс, описывающий действия с чекбоксами на страницах"""

    def __init__(self, driver) -> None:
        self.driver = driver

    def checkbox_on(self, by_locator: tuple, wait_time: int = 1):
        """
        Проверяет включен ли чекбокс. Если выключен, то включает его

        :param by_locator:
            локатор чекбокса
        :param wait_time:
            время ожидания

        """

        time.sleep(wait_time)
        checkbox = self.driver.find_element(*by_locator)
        match checkbox.is_selected():
            case True:
                pass
            case False:
                checkbox.click()

    def checkbox_off(self, by_locator: tuple, wait_time: int = 1):
        """
        Проверяет выключен ли чекбокс. Если выключен, то включает его

        :param by_locator:
            локатор чекбокс
        :param wait_time:
            время ожидания

        """

        time.sleep(wait_time)
        checkbox = self.driver.find_element(*by_locator)
        match checkbox.is_selected():
            case True:
                checkbox.click()
            case False:
                pass

    def checkbox_status(self, by_locator: tuple) -> bool:
        """

        Определяет простановку чекбокса

        :param by_locator:
            Локатор чекбокса

        """

        checkbox = self.driver.find_element(*by_locator)

        if checkbox.is_selected():
            return True
        else:
            return False
from summary_exercise.logic.base_app_page import BaseAppPage
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By


class HomePage(BaseAppPage):
    HISTORY_BUTTON = '//a[@title="History"]'

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._history_button = self._driver.find_element(By.XPATH, self.HISTORY_BUTTON)
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def open_history_page(self):
        self._history_button.click()

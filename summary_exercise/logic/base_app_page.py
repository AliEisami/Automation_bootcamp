from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from summary_exercise.infra.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class BaseAppPage(BasePage):
    YTD_MASTHEAD = '//ytd-masthead[@id="masthead"]'
    SIGNIN_BUTTON = '//div[@id="container"]//a[@aria-label="Sign in"]'
    SEARCH_INPUT = '//input[@id="search"]'

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._ytd_masthead = self._driver.find_element(By.XPATH, self.YTD_MASTHEAD)
            self._signin_button = self._driver.find_element(By.XPATH, self.SIGNIN_BUTTON)
            self._search_input = self._driver.find_element(By.XPATH, self.SEARCH_INPUT)
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def ytd_masthead_is_display(self):
        return self._ytd_masthead.is_displayed()

    def click_signin_button(self):
        self._signin_button.click()

    def search_for_video(self, video_name):
        self._search_input.send_keys(video_name)
        self._search_input.send_keys(Keys.ENTER)

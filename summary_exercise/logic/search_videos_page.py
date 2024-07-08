from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from summary_exercise.infra.base_page import BasePage


class SearchVideos(BasePage):
    VIDEOS = '//div[@id="title-wrapper"]'

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._videos = self._driver.find_elements(By.XPATH, self.VIDEOS)
        except NoSuchElementException as e:
            print("NoSuchElementException:", e)

    def get_search_videos(self):
        print("-------------------------- all good --------------------------")
        print(f"videos: {self._videos}")

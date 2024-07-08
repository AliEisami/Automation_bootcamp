from selenium import webdriver
import undetected_chromedriver as uc
from summary_exercise.infra.config_provider import ConfigProvider


class BrowserWrapper:

    def __init__(self):
        self._driver = None
        self.config = ConfigProvider.load_from_file()
        print("Test Start")

    def get_driver(self, url):
        options = uc.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        if self.config["browser"] == "Chrome":
            self._driver = uc.Chrome(options=options)
        elif self.config["browser"] == "FireFox":
            self._driver = webdriver.Firefox()
        elif self.config["browser"] == "Edge":
            self._driver = webdriver.Edge()
        else:
            print("browser not found")

        self._driver.get(url)
        return self._driver

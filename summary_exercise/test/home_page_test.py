import time
import unittest
from summary_exercise.infra.browser_wrapper import BrowserWrapper
from summary_exercise.infra.config_provider import ConfigProvider
from summary_exercise.logic.base_app_page import BaseAppPage
from summary_exercise.logic.home_page import HomePage


class HomePageTest(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_from_file()
        self.driver = self.browser.get_driver(self.config['url'])
        self.base_app_page = BaseAppPage(self.driver)
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_open_history_page(self):
        self.home_page.open_history_page()
        time.sleep(2)
        self.assertEqual(self.driver.current_url, "https://www.youtube.com/feed/history")

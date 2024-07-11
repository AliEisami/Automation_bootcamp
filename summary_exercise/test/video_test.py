import time
import unittest
from summary_exercise.infra.browser_wrapper import BrowserWrapper
from summary_exercise.infra.config_provider import ConfigProvider
from summary_exercise.logic.base_app_page import BaseAppPage
from summary_exercise.logic.search_videos_page import SearchVideos


class VideoTest(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_from_file()
        self.driver = self.browser.get_driver(self.config['url'])
        self.base_app_page = BaseAppPage(self.driver)
        self.search_videos = SearchVideos(self.driver)


    def tearDown(self):
        self.driver.quit()

    def test_search_successful(self):
        search_text = self.config["search_text"]
        self.base_app_page.search_for_video(search_text)
        time.sleep(2)
        self.assertEqual(self.driver.current_url,
                         f"https://www.youtube.com/results?search_query={search_text.replace(" ", "+")}")

    # def test_open_first_video(self):
    #     self.base_app_page.search_for_video("QA Automation for beginners")
    #     time.sleep(2)
    #     self.search_videos.get_search_videos()


import time
import unittest
from selenium.webdriver.common.by import By
from summary_exercise.infra.browser_wrapper import BrowserWrapper
from summary_exercise.infra.config_provider import ConfigProvider
from summary_exercise.logic.base_app_page import BaseAppPage
from summary_exercise.logic.google_login_page import GoogleLoginPage


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_from_file()
        self.driver = self.browser.get_driver(self.config['url'])
        self.base_app_page = BaseAppPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_login_successful(self):
        self.base_app_page.click_signin_button()
        login_page = GoogleLoginPage(self.driver)
        time.sleep(2)
        login_page.login_flow(self.config['email'], self.config['password'])
        time.sleep(3)
        self.assertEqual(self.driver.current_url, "https://www.youtube.com/")

    def test_login_unsuccessful(self):
        self.base_app_page.click_signin_button()
        login_page = GoogleLoginPage(self.driver)
        login_page.login_flow(self.config['email'], self.config['wrong_password'])
        time.sleep(2)
        error = (self.driver.find_element
                 (By.XPATH, '//span[text()="Wrong password. Try again or click Forgot password to reset it."]'))
        time.sleep(2)
        self.assertTrue(error.is_displayed())

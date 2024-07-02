from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def main():
    driver = webdriver.Chrome()
    driver.get("https://ultimateqa.com/complicated-page")

    # def test_buttons_click():
    #     buttons = driver.find_elements(By.XPATH, '//a[contains(@class, "et_pb_button et_pb_button_")]')
    #     for button in buttons:
    #         button.click()

    def test_buttons_click():
        buttons = driver.find_elements(By.XPATH, '//a[contains(@class, "et_pb_button et_pb_button_")]')
        for index in range(len(buttons)):
            try:
                buttons[index].click()
                time.sleep(1)
            except Exception as e:
                print(f"An error occurred: {e}")

    def test_socialmedia():
        social_media_buttons = driver.find_elements(By.XPATH,'//div[@class="et_pb_row et_pb_row_4"]//div//ul//li[contains(@class,"et_pb_social_media_follow_network_")]')
        for index in range(len(social_media_buttons)):
            try:
                social_media_buttons[index].click()
                time.sleep(2)
            except Exception as e:
                print(f"An error occurred: {e}")
            driver.back()
            if not driver.current_url == "https://ultimateqa.com/complicated-page":
                driver.back()



    test_socialmedia()
    driver.quit()

main()
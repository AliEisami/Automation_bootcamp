from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def main():
    driver = webdriver.Chrome()
    driver.get("https://ultimateqa.com/simple-html-elements-for-automation/")

    def test_contact():
        name_input = driver.find_element(By.ID, "et_pb_contact_name_0")
        name_input.send_keys("Ali")
        email_input = driver.find_element(By.ID, "et_pb_contact_email_0")
        email_input.send_keys("alieisami@gmail.com")
        submit_button = driver.find_element(By.NAME, "et_builder_submit_button")
        submit_button.click()
        driver.implicitly_wait(3)
        contact_message = driver.find_element(By.XPATH, "//div[@class='et-pb-contact-message']//p")
        print(f"test no.1: {contact_message.text}")

    def test_login():
        login_button = driver.find_element(By.XPATH, '//a[contains(text(), "Go to login page")]')
        login_button.click()
        login_email_input = driver.find_element(By.XPATH, '//input[@id="user[email]"]')
        login_email_input.send_keys("ali@test.com")
        login_password_input = driver.find_element(By.XPATH, '//input[@id="user[password]"]')
        login_password_input.send_keys("alitest123")
        login_submit_button = driver.find_element(By.XPATH, '//button[@class="button button-primary g-recaptcha"]')
        login_submit_button.click()
        driver.implicitly_wait(3)
        error_message = driver.find_element(By.XPATH, '//li[@class="form-error__list-item"]')
        print(f"test no.2: {error_message.text}")

    def test_car_checkbox():
        car_checkbox = driver.find_element(By.XPATH, '//input[@name="vehicle"][@value="Car"]')
        if not car_checkbox.is_selected():
            car_checkbox.click()

    test_car_checkbox()
    driver.quit()

main()
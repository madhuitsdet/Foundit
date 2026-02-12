import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class FounditLogin:
    def __init__(self, driver):
        self.driver = driver

    def foundit_login(self):
        # ******************login page**********************************************
        time.sleep(5)
        welcomepage = self.driver.find_element(By.CSS_SELECTOR, "div[class='flex_start h-9 grow cursor-pointer gap-5']").text
        print(welcomepage)
        self.driver.find_element(By.CSS_SELECTOR, "div[class='flex gap-4'] button[type='button']:nth-child(1)").click()
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Login via Password')]").click()
        self.driver.find_element(By.ID, "userName").send_keys("madhuitsdet@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("Madhu@2000")
        try:
            # Use the 'Okay' or 'Accept' button ID/Class from the banner
            cookie_button = self.driver.find_element(By.ID, "gdpr-cookie-accept")  # Example ID
            cookie_button.click()
        except:
            print("Cookie banner not found or already closed")
        self.driver.find_element(By.XPATH, "//button[text()='Login']").click()


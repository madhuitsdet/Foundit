import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class FounditHomepage:
    def __init__(self, driver):
        self.driver = driver

    def foundit_homepage(self):
        # ********************homepage**************************************************
        homepagevalidation = self.driver.find_element(By.CSS_SELECTOR, "div[class='flex_start h-9 grow cursor-pointer gap-5']").text
        print("homepage " + homepagevalidation)
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "span[class='w-20 truncate text-xs']").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "a[href='/seeker/profile']").click()
        profileinfo = self.driver.find_element(By.CSS_SELECTOR, "div[class='flex-1 ']").text
        print(profileinfo)


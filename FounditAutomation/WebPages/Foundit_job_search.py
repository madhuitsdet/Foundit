from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class FounditJobSearch:
    def __init__(self, driver):
        self.driver = driver

    def foundit_jobsearch(self):
        # *******************Job search ************************************************
        skills = "'Automation Testing','Manual Testing','Performance Testing'"
        self.driver.find_element(By.CSS_SELECTOR, "input[id='Desktop-skillsAutoComplete--input']").send_keys(skills)
        self.driver.find_element(By.CSS_SELECTOR, "input[id='Desktop-expAutoComplete--input']").click()
        experiences = self.driver.find_elements(By.CSS_SELECTOR, "div[id='Desktop-expAutoComplete'] [id='searchDropDown'] ul li")
        for year in experiences:
            if year.text == "4 Years":
                print("Total Experience is {}".format(year.text))
                year.click()
                break
        self.driver.find_element(By.CSS_SELECTOR, "svg[class='hidden lg:inline-block']").click()
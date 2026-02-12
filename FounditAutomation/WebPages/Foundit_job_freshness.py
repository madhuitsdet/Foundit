from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class FounditJobFreshness:
    def __init__(self, driver):
        self.driver = driver

    def foundit_job_freshness(self):
        job_freshness = 1
        action = ActionChains(self.driver)
        element = self.driver.find_element(By.XPATH, "//span[contains(text(),'Job Freshness')]")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        action.scroll_to_element(element).perform()
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Last 1 days')]").click()
        time.sleep(2)
        Quick_jobs = self.driver.find_elements(By.XPATH, "//a[contains(text(),'Test') or contains(text(),'Performance') or contains(text(),'QA') or contains(text(),'pytest')]/ancestor::div[@class='jobCardWrapper flex w-full flex-col gap-1']/descendant::button[contains(text(), 'Quick Apply')]")
        count = len(Quick_jobs)
        print("Quick Apply: {}".format(count))
        for job in Quick_jobs:
            if job.text == "Quick Apply":
                print("Job Freshness is {}".format(job.text))
                time.sleep(3)
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", job)
                action.scroll_to_element(job).perform()
                time.sleep(2)
                job.click()
                time.sleep(3)
            else:
                print("No Quick Apply Job")
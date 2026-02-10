import time
import os
import datetime
from itertools import count
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import service
from selenium.webdriver.chrome.options import Options

def test_TestCase_01():
    driver = webdriver.Chrome()
    driver.get("https://www.foundit.in/")

    # options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")  # Required for CI
    # options.add_argument("--window-size=1920,1080")  # Essential for headless
    # options.add_argument("--start-maximized")
    # driver = webdriver.Chrome(options=options)
    # driver.get("https://www.foundit.in/")

    driver.maximize_window()
    driver.implicitly_wait(10)
    # --- HANDLING OVERLAYS ---
    # 1. Close Cookie Banner if it exists
    try:
        # Based on Foundit's usual structure
        driver.find_element(By.XPATH, "//button[contains(text(),'Okay')]").click()
    except:
        pass

#******************login page**********************************************
    time.sleep(5)
    welcomepage = driver.find_element(By.CSS_SELECTOR, "svg[xmlns='http://www.w3.org/2000/svg']").text
    print(welcomepage)
    driver.find_element(By.CSS_SELECTOR, "div[class='flex gap-4'] button[type='button']:nth-child(1)").click()
    driver.find_element(By.XPATH, "//span[contains(text(),'Login via Password')]").click()
    driver.find_element(By.ID, "userName").send_keys("madhuitsdet@gmail.com")
    driver.find_element(By.ID, "password").send_keys("Madhu@2000")
    try:
        # Use the 'Okay' or 'Accept' button ID/Class from the banner
        cookie_button = driver.find_element(By.ID, "gdpr-cookie-accept")  # Example ID
        cookie_button.click()
    except:
        print("Cookie banner not found or already closed")
    driver.find_element(By.XPATH, "//button[text()='Login']").click()

    #********************homepage**************************************************
    homepagevalidation = driver.find_element(By.CSS_SELECTOR, "span[class='text-brand-primary']").text
    print("homepage"+homepagevalidation)
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "span[class='w-20 truncate text-xs']").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "a[href='/seeker/profile']").click()
    profileinfo = driver.find_element(By.CSS_SELECTOR, "div[class='flex-1 ']").text
    print(profileinfo)

    #***********************profile page**********************************************
    # resume_file_path = "C:\\python32-38\\foundit\\FounditAutomation\\data\\Madhu_Vanga_SDET_v6.pdf"
    resume_file_path = os.path.abspath("FounditAutomation/data/Madhu_Vanga_SDET_v6.pdf")
    # driver.find_element(By.XPATH, "(//button[@type='button'][text()='Replace resume'])[2]").click()
    uploadfile = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    uploadfile.send_keys(resume_file_path)
    Uploadstatus = driver.find_element(By.XPATH, "//span[text()='Resume uploaded successfully']").text
    time.sleep(3)
    print(Uploadstatus)
    # assert "Resume uploaded successfully" in Uploadstatus
    #*******************Job search ************************************************

    skills = "'Automation Testing','Manual Testing','Performance Testing'"
    # wait = WebDriverWait(driver, 10)
    driver.find_element(By.CSS_SELECTOR, "input[id='Desktop-skillsAutoComplete--input']").send_keys(skills)
    driver.find_element(By.CSS_SELECTOR, "input[id='Desktop-expAutoComplete--input']").click()
    experiences = driver.find_elements(By.CSS_SELECTOR, "div[id='Desktop-expAutoComplete'] [id='searchDropDown'] ul li")
    for year in experiences:
        if year.text == "4 Years":
            print("Total Experience is {}".format(year.text))
            year.click()
            break
    driver.find_element(By.CSS_SELECTOR, "svg[class='hidden lg:inline-block']").click()

    #**************Job freshness*********************************************************
    job_freshness = 1
    action = ActionChains(driver)
    element = driver.find_element(By.XPATH, "//span[contains(text(),'Job Freshness')]")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    action.scroll_to_element(element).perform()
    driver.find_element(By.XPATH, "//span[contains(text(),'Last 1 days')]").click()
    time.sleep(2)
    Quick_jobs = driver.find_elements(By.XPATH, "//a[contains(text(),'Test') or contains(text(),'Performance') or contains(text(),'QA') or contains(text(),'pytest')]/ancestor::div[@class='jobCardWrapper flex w-full flex-col gap-1']/descendant::button[contains(text(), 'Quick Apply')]")
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










    time.sleep(5)


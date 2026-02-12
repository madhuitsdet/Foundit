import time
import os
import datetime
from itertools import count
from time import sleep

from FounditAutomation.WebPages.Foundit_homepage import FounditHomepage
from FounditAutomation.WebPages.Foundit_job_freshness import FounditJobFreshness
from FounditAutomation.WebPages.Foundit_job_search import FounditJobSearch
from FounditAutomation.WebPages.Foundit_login import FounditLogin
from FounditAutomation.WebPages.Foundit_profilepage import FounditProfilepage
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import service
from selenium.webdriver.chrome.options import Options


def test_TestCase_01(test_browser):
    driver = test_browser
    # --- HANDLING OVERLAYS ---
    # 1. Close Cookie Banner if it exists
    try:
        # Based on Foundit's usual structure
        driver.find_element(By.XPATH, "//button[contains(text(),'Okay')]").click()
    except:
        pass

    #******************login page**********************************************
    foundit_login = FounditLogin(driver)
    foundit_login.foundit_login()

    #********************homepage**************************************************
    foundit_homepage = FounditHomepage(driver)
    foundit_homepage.foundit_homepage()

    #***********************profile page**********************************************
    foundit_profilepage = FounditProfilepage(driver)
    foundit_profilepage.foundit_profilepage()


    #*******************Job search ************************************************
    foundit_jobsearch = FounditJobSearch(driver)
    foundit_jobsearch.foundit_jobsearch()


    #**************Job freshness*********************************************************
    foundit_job_freshness = FounditJobFreshness(driver)
    foundit_job_freshness.foundit_job_freshness()











    time.sleep(5)


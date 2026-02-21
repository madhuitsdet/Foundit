import time
import os
import datetime
from itertools import count
from time import sleep
import pytest
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
import json
import os

# Correct relative path navigation from FounditAutomation/tests/ to /data/
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
jsonpath = os.path.join(project_root, "data", "test_foundit_parameterized.json")

with open(jsonpath) as f:
    test_data = json.load(f)
    list_data = test_data["data"]

@pytest.mark.parametrize("list_data_items", list_data)
def test_TestCase_01(test_browser, list_data_items):
    driver = test_browser
    # --- HANDLING OVERLAYS ---
    # 1. Close Cookie Banner if it exists
    try:
        # Based on Foundit's usual structure okay
        driver.find_element(By.XPATH, "//button[contains(text(),'Okay')]").click()
    except:
        pass

    #******************login page**********************************************
    foundit_login = FounditLogin(driver)
    foundit_login.foundit_login(list_data_items["userName"], list_data_items["password"])

    #********************homepage**************************************************
    foundit_homepage = FounditHomepage(driver)
    foundit_homepage.foundit_homepage()

    #***********************profile page**********************************************
    foundit_profilepage = FounditProfilepage(driver)
    foundit_profilepage.foundit_profilepage(list_data_items["resume_file_path"])


    #*******************Job search ************************************************
    foundit_jobsearch = FounditJobSearch(driver)
    foundit_jobsearch.foundit_jobsearch(list_data_items["skills"])


    #**************Job freshness*********************************************************
    foundit_job_freshness = FounditJobFreshness(driver)
    foundit_job_freshness.foundit_job_freshness(list_data_items["jobFreshness"])







    time.sleep(5)


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
class FounditProfilepage:
    def __init__(self, driver):
        self.driver = driver

    def foundit_profilepage(self):
        # ***********************profile page**********************************************
        # Get the directory where pytest_end_to_end.py is located
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Move up one level to FounditAutomation, then into data
        resume_file_path = os.path.join(current_dir, "..", "data", "Madhu_Vanga_SDET_v6.pdf")

        # # Standardize the path for the OS (fixes slash issues)
        resume_file_path = os.path.normpath(resume_file_path)

        uploadfile = self.driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        uploadfile.send_keys(resume_file_path)
        Uploadstatus = self.driver.find_element(By.XPATH, "//span[text()='Resume uploaded successfully']").text
        time.sleep(3)
        print(Uploadstatus)
        # assert "Resume uploaded successfully" in Uploadstatus
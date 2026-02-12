import pytest
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.edge.options import Options

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="browser selectino")

@pytest.fixture(scope="function")
def test_browser(request):
    browser_name = request.config.getoption("--browser_name")

    if browser_name == "chrome":
        driver = webdriver.Chrome()

    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    elif browser_name == "edge":
        driver = webdriver.Edge


    driver.get("https://www.foundit.in/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


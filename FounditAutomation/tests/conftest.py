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
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="firefoxheadless", help="browser selectino")

@pytest.fixture(scope="function")
def test_browser(request):
    browser_name = request.config.getoption("--browser_name")

    if browser_name == "chrome":
        driver = webdriver.Chrome()

    elif browser_name == "chromedirver":
        chromeservice = ChromeService(r"Drivers/chromedriver.exe")
        driver = webdriver.Chrome(service=chromeservice)


    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    elif browser_name == "firefoxheadless":
        firefoxoptions = FirefoxOptions()
        firefoxoptions.add_argument("--headless")
        driver = webdriver.Firefox(options=firefoxoptions)

    elif browser_name == "edge":
        driver = webdriver.Edge()

    elif browser_name == "edgeheadless":
        edge_options = EdgeOptions()
        edge_options.add_argument("--headless=new")
        edge_options.add_argument("--disable-blink-features=AutomationControlled")
        edge_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        edge_options.add_experimental_option("useAutomationExtension", False)
        edge_options.add_argument("--disable-gpu")
        edge_options.add_argument("--no-sandbox")
        edge_options.add_argument("--disable-dev-shm-usage")
        edge_options.add_argument("--remote-debugging-port=9222")
        edge_options.add_argument("--start-maximized")
        edge_options.add_argument(r"--user-data-dir=C:\temp\EdgeProfile")
        edge_options.add_argument("--window-size=1920,1080")
        edge_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36")
        driver = webdriver.Edge(options=edge_options)

    driver.get("https://www.foundit.in/")
    if "headless" not in browser_name:
        driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


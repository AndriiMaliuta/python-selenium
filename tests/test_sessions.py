import logging
import selectors

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.ie.options import Options as IEOptions
from selenium.webdriver.common import by

# FIREFOX
service = FirefoxService(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
url = "https://en.wikipedia.org/wiki/Example.com"


def test_driver_manager_chrome():
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.quit()


def init_with_options():
    options = FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    driver.get("com.example")
    driver.quit()


def test_firefox_session():
    # service = FirefoxService(executable_path=GeckoDriverManager().install())
    # driver = webdriver.Firefox(service=service)
    driver.quit()


def test_tables_wiki():
    driver.get(url)
    toc = driver.find_element(by.By.ID, "toc")
    toc_heading = driver.find_element(by.By.ID, "mw-toc-heading")
    print(toc)
    logging.info(toc)
    assert toc.text.__contains__("Contents")
    assert toc_heading.text.__eq__("Contents")
    driver.quit()

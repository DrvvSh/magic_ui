import pytest
from selenium import webdriver
from pages.log_in import LogIn
from pages.stats import Stats


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(3)
    return chrome_driver

@pytest.fixture()
def log_in_page(driver):
    return LogIn(driver)

@pytest.fixture()
def stats(driver):
    return Stats(driver)
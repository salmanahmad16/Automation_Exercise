import pytest
from selenium import webdriver


@pytest.fixture
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching Chrome Driver .......")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching FireFox Driver .......")
    else:
        driver = webdriver.Chrome()
    return driver


def pytest_addoption(parser):  # This will get the value from CLI / hook
    parser.addoption('--browser')


@pytest.fixture()
def browser(request):  # This will return the browser value to setup method
    return request.config.getoption('--browser')




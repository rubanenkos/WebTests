import pytest
from selenium import webdriver
from os.path import dirname
from settings.options import ProjectPaths

@pytest.fixture(scope="function")
def browser():
    """Setup browser"""

    direct = dirname(__file__)
    driver = webdriver.Chrome(executable_path=direct + ProjectPaths.CHROME_DRIVER.value)
    driver.maximize_window()
    driver.get(ProjectPaths.LINK.value)

    yield driver
    driver.quit()

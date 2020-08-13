import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from os.path import dirname


class TestMainPage:
    LINK = "https://www.python.org"

    def start_browser(self):
        direct = dirname(dirname(__file__))
        driver = webdriver.Chrome(direct + "/chromedriver")
        driver.maximize_window()
        driver.get(self.LINK)
        return driver

    @pytest.mark.smoke
    def test_search(self):
        driver = self.start_browser()
        try:
            search_bar = driver.find_element_by_name("q")
            search_bar.clear()
            search_word = 'python'
            search_bar.send_keys(search_word)
            search_bar.send_keys(Keys.RETURN)
            url = driver.current_url
            assert self.LINK + '/search/?q=' + search_word in url
        except AssertionError:
            driver.get_screenshot_as_file(driver.session_id+'.png')
            raise
        finally:
            driver.close()

    @pytest.mark.smoke
    def test_title(self):
        driver = self.start_browser()
        try:
            title = driver.title
            print(title)
            assert 'Python' in title
        except AssertionError:
            driver.get_screenshot_as_file(driver.session_id+'.png')
            raise
        finally:
            driver.close()


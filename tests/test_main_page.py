import pytest
from selenium.webdriver.common.keys import Keys
from settings.options import ProjectPaths


class TestMainPage:

    @pytest.mark.smoke
    def test_search(self, browser):
        driver = browser
        try:
            search_bar = driver.find_element_by_name("q")
            search_bar.clear()
            search_word = 'python'
            search_bar.send_keys(search_word)
            search_bar.send_keys(Keys.RETURN)
            url = driver.current_url
            assert ProjectPaths.LINK.value + '/search/?q=' + search_word in url
        except AssertionError:
            driver.get_screenshot_as_file(driver.session_id+'.png')
            raise

    @pytest.mark.smoke
    def test_title(self, browser):
        driver = browser
        try:
            title = driver.title
            print(title)
            assert 'Python' in title
        except AssertionError:
            driver.get_screenshot_as_file(driver.session_id+'.png')
            raise

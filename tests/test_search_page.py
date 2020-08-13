import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from os.path import dirname

class TestSearchPage:

    @pytest.mark.smoke
    def test_search_1(self):

        direct = dirname(dirname(__file__))
        # print(direct)
        # main_directory = dirname(dirname(dirname(__file__)))
        # print(main_directory)
        path = direct + "/chromedriver"
        print(path)
        driver = webdriver.Chrome(path)
        # driver = webdriver.Chrome("chromedriver")
        # driver = webdriver.Chrome(main_directory + "/WebTests/chromedriver")
        driver.maximize_window()

        # driver = webdriver.Chrome('./chromedriver')
        session_id = driver.session_id
        link = "https://www.python.org"
        driver.get(link)
        print(driver.title)
        try:
            search_bar = driver.find_element_by_name("q")
            search_bar.clear()
            search_word = 'python'
            search_bar.send_keys(search_word)
            search_bar.send_keys(Keys.RETURN)
            url= driver.current_url
            assert link + '/search/?q=' + search_word in url
        except AssertionError:
            driver.get_screenshot_as_file(session_id+'.png')
            raise
        finally:
            driver.close()

    @pytest.mark.smoke
    def test_search_2(self):
        driver = webdriver.Chrome('chromedriver')
        session_id = driver.session_id
        driver.get("https://www.python.org")
        try:
            title = driver.title
            print(title)
            assert 'python' in title
        except AssertionError:
            driver.get_screenshot_as_file(session_id+'.png')
            raise
        finally:
            driver.close()


import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities 
from selenium.webdriver.firefox.options import Options

class WelcomePage:
    ''' A Page Object to model the welcome page of Python '''

    title = "Wikipedia"
    url = "http://www.wikipedia.org"

    def __init__(self, driver):
        self.driver = driver
        self.query_field = WelcomePage.QueryField(driver)

    def go(self):
        print("going to : ", WelcomePage.url)
        self.driver.get(WelcomePage.url)
        return self

    def get_title(self):
        title = self.driver.title
        print("title : ", title)
        return title

    def search(self, query):
        print("search : ", query)
        self.query_field.clear().search(query)
        return self

    def has_results(self):
        return "No results found." not in self.driver.page_source

    class QueryField:
        ''' A Page Element to model the query field of the welcome page '''

        def __init__(self, driver):
            self.driver = driver

        def __get_elem(self):
            if not hasattr(self, 'elem'):
                self.elem = self.driver.find_element(By.CSS_SELECTOR, "[name='q']")
            return self.elem

        def clear(self):
            self.__get_elem().clear()
            return self

        def search(self, query):
            input = self.__get_elem()
            input.send_keys("pycon")
            input.send_keys(Keys.RETURN)
            return self

class PythonOrgSearch(unittest.TestCase):
    ''' A test class '''

    def setUp(self):
        ''' Executed before each test '''
        self.driver = webdriver.Firefox()

    def tearDown(self):
        ''' Executed after each test '''
        self.driver.close()

    def test_search_in_python_org(self):
        ''' A test example :
            1. Opens the python page
            2. Check the page title
            3. Enter a query in the search input
            4. Check results are found '''
        
        page = WelcomePage(self.driver).go()
        assert page.get_title() == WelcomePage.title

if __name__ == "__main__":
    unittest.main()


from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class duckduckgoSearchPage:
    URL = 'https://duckduckgo.com/'

    SEARCH_INPUT = (By.ID,"search_form_input_homepage")
    def __init__(self,browser):
        self.browser = browser

    def load(self):
        # TODO
        self.browser.get(self.URL)

    def search(self,phrase):
        # TODO
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)
        
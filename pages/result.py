from selenium.webdriver.common.by import By

class duckduckgoResultPage:
    RESULT_LINKS = (By.CSS_SELECTOR, 'a.result__a')
    SEARCH_INUPT = (By.ID,'search_form_input')

    def __init__(self,browser):
        self.browser = browser
    
    def result_link_titles(self):
        # TODO
        links = self.browser.find_elements(*self.RESULT_LINKS)
        titles = [links.text for link in links]
        return titles

    def search_input_value(self):
        # TODO
        search_input = self.browser.find_element(*self.SEARCH_INUPT)
        value = search_input.get_attribute('value')
        return value
    
    def title(self):
        # TODO
        return self.browser.title
# import pytest
# import selenium.webdriver

# @pytest.fixture
# def browser():

#     b = selenium.webdriver.Chrome()
#     b.implicitly_wait(10)
#     yield b
#     b.quit()

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def browser():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

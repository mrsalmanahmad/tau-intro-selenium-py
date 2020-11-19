# import pytest
# import selenium.webdriver

# @pytest.fixture
# def browser():

#     b = selenium.webdriver.Chrome()
#     b.implicitly_wait(10)
#     yield b
#     b.quit()

import pytest
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import json

@pytest.fixture
def config(scrpe='session'):
    # Read file
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Assert values are acceptable
    assert config['browser'] in ['Firefox','Chrome','Headless Chrome']
    assert isinstance(config['implicit_wait'],int)
    assert config['implicit_wait'] > 0

    # Return confif so it can be used
    return config

@pytest.fixture
def browser(config):

    if config['browser'] == 'Firefox':
        #b = selenium.webdriver.Firefox()
        b = webdriver.Chrome(ChromeDriverManager().install())
    elif config['browser'] == 'Chorme':
        b = selenium.webdriver.Chrome()
        #b = webdriver.Chrome(ChromeDriverManager().install())
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        #b = selenium.webdriver.Chrome(options=opts)
        b = webdriver.Chrome(ChromeDriverManager().install())
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    #driver = webdriver.Chrome(ChromeDriverManager().install())
    b.implicitly_wait(config['implicit_wait'])
    yield b
    b.quit()

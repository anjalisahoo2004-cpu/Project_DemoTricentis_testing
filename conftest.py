'''
import pytest
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

@pytest.fixture
def setup_and_teardown():
    driver = webdriver.Chrome(options=opts)
    driver.get("https://demowebshop.tricentis.com/")
    yield driver
    driver.quit()
'''

##Cross browser testing

import pytest
from selenium import webdriver

@pytest.fixture(params=['chrome','edge','firefox'])
def setup_and_teardown(request):

    parameter=request.param

    if parameter=='chrome':
        driver=webdriver.Chrome()

    if parameter=='firefox':
        driver=webdriver.Firefox()

    if parameter=='edge':
        driver=webdriver.Edge()

    driver.get("https://demowebshop.tricentis.com/")
    yield driver
    driver.quit()
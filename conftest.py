import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose browser: language")


@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    x = request.config.getoption("language")
    
    options.add_experimental_option('prefs', {'intl.accept_languages': x})
    browser = webdriver.Chrome(options=options)
    yield browser
    
    browser.quit()
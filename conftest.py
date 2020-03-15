import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

import logging
import allure


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome', help='Choose browser: chrome or firefox')
    parser.addoption('--link', action='store', default='http://localhost:5000', help='Enter link')


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope='function')
def browser(request):
    browser = request.config.getoption('browser')

    if browser == 'chrome':
        print('\nstart chrome browser for test ')
        options = Options()
        browser = webdriver.Chrome(options=options)

    elif browser == 'firefox':
        print('\nstart firefox browser for test ')
        fp = webdriver.FirefoxProfile()
        browser = webdriver.Firefox(firefox_profile=fp)

    else:
        print('Browser {} is not implemented yet'.format(browser))
        raise pytest.UsageError('--browser should be chrome or firefox')
    browser.implicitly_wait(10)
    browser.set_window_size(1200, 1000)
    yield browser
    
    # Do teardown (this code will be executed after each test):
    if request.node.rep_call.failed:
        # Make the screenshot if test failed:
        try:
            browser.execute_script("document.body.bgColor = 'white';")
            allure.attach(browser.get_screenshot_as_png())
        except:
            # just ignore
            pass
    
    print('\nquit browser ')
    browser.quit()


@pytest.fixture(scope='function')
def link(request):
    return request.config.getoption('link')
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: ru, en, etc.")
    parser.addoption('--link', action='store', default=None,
                     help="Set the test link")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('language', ["en", "ru"])
def test_guest_should_see_login_link(browser, request, language):
    link = request.config.getoption("link")
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# для корректного отображения кириллицы в параметризаторах
def pytest_make_parametrize_id(config, val): return repr(val)


def pytest_addoption(parser):
    parser.addoption('--browser_name',
                     action='store',
                     default='safari',
                     help='Choose browser: chrome of firefox')
    parser.addoption('--language',
                     action='store',
                     default='en',
                     help='Choose language: ru, en, ... etc.')


def interceptor(request):
    del request.headers['Accept-Language']
    request.headers['Accept-Language'] = 'en'


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption("browser_name")  # получаем параметр командной строки browser_name
    user_language = request.config.getoption("language")

    if browser_name == "chrome":
        print("\nstart chrome browser for test...")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        print("\nstart firefox browser for test...")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)

    elif browser_name == "safari":
        print("\nstart safari browser for test...")
        browser = webdriver.Safari()
        browser.request_interceptor = interceptor
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser...")
    browser.quit()

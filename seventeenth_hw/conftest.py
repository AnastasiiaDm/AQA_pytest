import pytest
from seventeenth_hw.utilities.config_reader import get_application_url, get_browser_id
from seventeenth_hw.utilities.browser_factory import browser_factory

from seventeenth_hw.page_objects.main_page_pack.main_page import MainPage

@pytest.fixture()
def create_browser():
    browser = browser_factory(get_browser_id())
    browser.maximize_window()
    browser.get(get_application_url())
    yield browser
    browser.quit()

# def pytest_addoption(parser):
#     parser.addoption('--browser_id', action='store', default=1, help='Set browser id')
#
# @pytest.fixture()
# def create_browser(pytestconfig):
#     browser = browser_factory(int(pytestconfig.getoption('--browser_id')))
#     browser.maximize_window()
#     browser.get(get_application_url())
#     yield browser
#     browser.quit()


@pytest.fixture()
def open_main_page(create_browser):
    return MainPage(create_browser)


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "smoke: for smoke tests"
    )
    config.addinivalue_line(
        "markers", "regression: for regression tests"
    )

import pytest

from seventeenth_hw.page_objects.cart_page_pack.cart_page import CartPage
from seventeenth_hw.page_objects.login_page_pack.login_page import LoginPage
from seventeenth_hw.page_objects.manager_application_form.manager_application_form import ManagerApplicationForm
from seventeenth_hw.utilities.config_reader import get_application_url, get_browser_id, get_search_id_key
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


@pytest.fixture()
def open_cart_page_with_item(create_browser):
    MainPage(create_browser).set_search_key(get_search_id_key()).click_search_submit().click_add_to_cart_button(). \
        click_cart_page_button()
    return CartPage(create_browser)

@pytest.fixture()
def open_empty_cart_page(create_browser):
    MainPage(create_browser).click_cart_button()
    return CartPage(create_browser)

@pytest.fixture()
def open_login_page(create_browser):
    MainPage(create_browser).click_login_button()
    return LoginPage(create_browser)

@pytest.fixture()
def open_manager_application_form(create_browser):
    MainPage(create_browser).click_search_submit().click_manager_application_button()
    return ManagerApplicationForm(create_browser)


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "smoke: for smoke tests"
    )
    config.addinivalue_line(
        "markers", "regression: for regression tests"
    )

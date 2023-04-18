import json
from urllib import request
from contextlib import suppress

import allure
import pytest

from constants import ROOT_DIR
from seventeenth_hw.mongo_db_repo.alternate_signs_collection import AlternateSigns
from seventeenth_hw.page_objects.login_page_pack.login_page import LoginPage
from seventeenth_hw.page_objects.manager_application_form.manager_application_form import ManagerApplicationForm
from seventeenth_hw.utilities.browser_factory import browser_factory

from seventeenth_hw.page_objects.main_page_pack.main_page import MainPage
from seventeenth_hw.utilities.configuration import Configuration


@pytest.fixture(scope='session', autouse=True)
def env():
    with open(f'{ROOT_DIR}/seventeenth_hw/configurations/config.json', 'r') as file:
        response = file.read()
    config = json.loads(response)
    return Configuration(**config)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def create_browser(env, request):
    browser = browser_factory(int(env.browser_id))
    browser.maximize_window()
    browser.get(env.app_url)
    yield browser
    if request.node.rep_call.failed:
        with suppress(Exception):
            allure.attach(browser.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
    browser.quit()


def pytest_addoption(parser):
    parser.addoption('--browser_id', action='store', default=1, help='Set browser id')
    parser.addoption('--env', action='store', help='Env')


@pytest.fixture()
def open_main_page(create_browser):
    return MainPage(create_browser)


@pytest.fixture()
def open_cart_page_with_item(open_main_page, env):
    return open_main_page.set_search_key(env.search_id_key).click_search_submit().click_add_to_cart_button(). \
        click_cart_page_button()


@pytest.fixture()
def open_empty_cart_page(open_main_page):
    return open_main_page.click_cart_button()


@pytest.fixture()
def open_login_page(create_browser):
    MainPage(create_browser).click_login_button()
    return LoginPage(create_browser)


@pytest.fixture()
def open_manager_application_form(create_browser):
    MainPage(create_browser).click_search_submit().click_manager_application_button()
    return ManagerApplicationForm(create_browser)


@pytest.fixture()
def get_alternate_signs_col():
    return AlternateSigns.get_col()


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "smoke: for smoke tests"
    )
    config.addinivalue_line(
        "markers", "regression: for regression tests"
    )

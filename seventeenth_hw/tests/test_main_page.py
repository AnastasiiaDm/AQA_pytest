"""
Find web site for your framework
Implement config_file and config reader
Implement driver factory
Implement BasePage
Implement at least 5 PageObjects with a minimum of 10 elements and methods using the ChainOfResponcibility pattern
Implement conftest.py with different fixtures
Write TCs for your pages (At least 5 TCs per page).
Mark smoke test cases and regression Tcs
"""
import pytest

from seventeenth_hw.utilities.config_reader import get_search_key, get_invalid_search_key


@pytest.mark.smoke
def test_search_items_by_search_field(open_main_page):
    main_page = open_main_page
    search_page = main_page.set_search_key(get_search_key()).click_search_submit()
    assert search_page.is_search_result_counter_displayed(), 'Search result counter is not displayed'
    assert search_page.is_search_warning_invisible(), 'Search warning is displayed'


@pytest.mark.regression
def test_search_no_items_by_search_field(open_main_page):
    main_page = open_main_page
    search_page = main_page.click_search_submit()
    assert search_page.is_warning_displayed(), 'Search page warning is not displayed'
    assert search_page.is_search_result_counter_invisible(), 'Search result counter is displayed'


@pytest.mark.regression
def test_search_invalid_items_by_search_field(open_main_page):
    main_page = open_main_page
    search_page = main_page.set_search_key(get_invalid_search_key()).click_search_submit()
    assert search_page.is_warning_displayed(), 'Search page warning is not displayed'
    assert search_page.is_search_result_counter_invisible(), 'Search result counter is displayed'

@pytest.mark.smoke
def test_open_empty_cart(open_main_page):
    main_page = open_main_page
    search_page = main_page.click_cart_button()
    assert search_page.is_warning_displayed(), "Empty cart warning is not displayed"

# main_page.set_email(get_user_creds()[0])

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
    search_page = main_page.set_search_key(get_search_key()).click_search_submit_for_main()
    assert search_page.is_search_result_counter_displayed(), 'Search result counter is not displayed'
    assert search_page.is_search_warning_invisible(), 'Search warning is displayed'


@pytest.mark.regression
def test_search_no_items_by_search_field(open_main_page):
    main_page = open_main_page
    search_page = main_page.click_search_submit_for_main()
    assert search_page.is_warning_displayed(), 'Search page warning is not displayed'
    assert search_page.is_search_result_counter_invisible(), 'Search result counter is displayed'


@pytest.mark.regression
def test_search_invalid_items_by_search_field(open_main_page):
    main_page = open_main_page
    search_page = main_page.set_search_key(get_invalid_search_key()).click_search_submit_for_main()
    assert search_page.is_warning_displayed(), 'Search page warning is not displayed'
    assert search_page.is_search_result_counter_invisible(), 'Search result counter is displayed'


@pytest.mark.smoke
def test_open_empty_cart(open_main_page):
    main_page = open_main_page
    search_page = main_page.click_cart_button_for_main()
    assert search_page.is_warning_displayed(), "Empty cart warning is not displayed"


@pytest.mark.smoke
def test_login_page(open_main_page):
    main_page = open_main_page
    login_page = main_page.click_login_button()
    assert login_page.is_submit_login_button_visible(), "Login button is not displayed"


@pytest.mark.smoke
def test_go_to_iphone_item_page(open_main_page):
    main_page = open_main_page
    iphone_items = main_page.click_iphone_items_by_js()
    assert iphone_items.is_iphone_items_url_matches(), "Url do not match"


@pytest.mark.smoke
def test_go_to_contact_page(open_main_page):
    main_page = open_main_page
    contact_page = main_page.click_header_contact_button()
    assert contact_page.is_contact_url_matches(), "Url do not match"


@pytest.mark.smoke
def test_is_promo_block_exist(open_main_page):
    main_page = open_main_page
    assert main_page.is_promo_block_exist(), "Promo block is not disabled"

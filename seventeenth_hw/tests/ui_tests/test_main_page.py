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


@pytest.mark.smoke
def test_search_items_by_search_field(open_main_page, env):
    main_page = open_main_page
    search_page = main_page.set_search_key(env.search_key).click_search_submit_for_main()
    assert search_page.is_search_result_counter_displayed(), 'Search result counter is not displayed'
    assert main_page.wait_until_warning_invisible(), 'Warning is displayed'


@pytest.mark.regression
def test_search_no_items_by_search_field(open_main_page):
    main_page = open_main_page
    search_page = main_page.click_search_submit_for_main()
    assert search_page.wait_until_warning_visible(), 'Search page warning is not displayed'
    assert search_page.is_search_result_counter_invisible(), 'Search result counter is displayed'


@pytest.mark.regression
def test_search_invalid_items_by_search_field(open_main_page, env):
    main_page = open_main_page
    search_page = main_page.set_search_key(env.invalid_key).click_search_submit_for_main()
    assert search_page.wait_until_warning_visible(), 'Search page warning is not displayed'
    assert search_page.is_search_result_counter_invisible(), 'Search result counter is displayed'


@pytest.mark.smoke
def test_go_to_iphone_item_page(open_main_page, env):
    main_page = open_main_page
    iphone_items = main_page.click_iphone_item()
    assert iphone_items.is_page_url_matches(env.iphone_items_url), f"Url do not match {env.iphone_items_url}"


@pytest.mark.smoke
def test_go_to_contact_page(open_main_page, env):
    main_page = open_main_page
    contact_page = main_page.click_header_contact_button()
    assert contact_page.is_page_url_matches(env.contact_url), f"Url do not match {env.contact_url}"


@pytest.mark.smoke
def test_is_promo_block_exist(open_main_page):
    main_page = open_main_page
    assert main_page.is_promo_block_exist(), "Promo block is not disabled"

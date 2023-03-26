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

from seventeenth_hw.utilities.config_reader import get_search_key, get_invalid_search_key, \
    get_manager_application_form_name_key, get_manager_application_form_phone_key, get_manager_application_form_text_key


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
    assert search_page.is_search_warning_displayed(), 'Search page warning is not displayed'
    assert search_page.is_search_result_counter_invisible(), 'Search result counter is displayed'


@pytest.mark.regression
def test_search_invalid_items_by_search_field(open_main_page):
    main_page = open_main_page
    search_page = main_page.set_search_key(get_invalid_search_key()).click_search_submit()
    assert search_page.is_search_warning_displayed(), 'Search page warning is not displayed'
    assert search_page.is_search_result_counter_invisible(), 'Search result counter is displayed'


@pytest.mark.regression
def test_go_to_main_page_from_search_result(open_main_page):
    main_page = open_main_page
    main_page_url = main_page.set_search_key(get_search_key()).click_search_submit().click_site_header_logo()
    assert main_page_url.is_main_page_url_matches(), "Url doesnt match"


@pytest.mark.smoke
def test_open_manager_application_form(open_main_page):
    main_page = open_main_page
    manager_application_form = main_page.click_search_submit().click_manager_application_button()
    assert manager_application_form.is_form_visible(), \
        "Manager application form is not displayed"


# @pytest.mark.regression
# def test_exist_manager_application_form_phone_onfocus(open_main_page):
#     main_page = open_main_page
#     manager_application_form = main_page.click_search_submit().click_manager_application_button()
#     assert manager_application_form.is_phone_onfocus_exist(), "Manager application form onfocus is not displayed"
#
#
# @pytest.mark.smoke
# def test_close_manager_application_form(open_main_page):
#     main_page = open_main_page
#     manager_application_form = main_page.click_search_submit().click_manager_application_button()
#     assert manager_application_form.is_manager_application_form_popup_visible()
#     manager_application_form.click_manager_application_form_exit_button()
#     assert manager_application_form.is_manager_application_form_popup_invisible(), \
#         "Manager application form is displayed"
#
#
# @pytest.mark.regression
# def test_submit_empty_manager_application_form(open_main_page):
#     main_page = open_main_page
#     submit = main_page.click_search_submit().click_manager_application_button(). \
#         click_manager_application_form_submit_button()
#     assert submit.is_manager_application_form_popup_visible(), "Manager application form onfocus is not displayed"
#
#
# @pytest.mark.smoke
# def test_send_message_by_manager_application_form(open_main_page):
#     main_page = open_main_page
#     fill_form = main_page.click_search_submit().click_manager_application_button(). \
#         send_message_by_manager_application_form(get_manager_application_form_name_key(),
#                                                  get_manager_application_form_phone_key(),
#                                                  get_manager_application_form_text_key())
#     #here might be assert fill_form.is_manager_application_form_popup_invisible() but I decided not to disturb operators
#     assert fill_form.is_manager_application_form_popup_visible(), "Manager application form is not displayed"

# main_page.set_email(get_user_creds()[0])

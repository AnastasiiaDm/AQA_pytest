import pytest

from seventeenth_hw.utilities.config_reader import get_user_creds


@pytest.mark.smoke
def test_is_google_sign_up_button_exist(open_main_page):
    main_page = open_main_page
    login_page = main_page.click_login_button()
    assert login_page.is_google_sign_up_button_exist(), "Sign up by google button is not displayed"


@pytest.mark.smoke
def test_authorize(open_main_page):
    main_page = open_main_page
    login = main_page.click_login_button().authorize(get_user_creds()[0], get_user_creds()[1])
    assert login.is_header_logout_button_exist(), "User not authorized"


@pytest.mark.smoke
def test_open_forgot_password_page(open_main_page):
    main_page = open_main_page
    forgot_password = main_page.click_login_button().click_forgot_password_button()
    assert forgot_password.is_recover_password_submit_visible(), "Forgot password page is not opened"


@pytest.mark.smoke
def test_open_login_page_from_forgot_password_page(open_main_page):
    main_page = open_main_page
    login_page = main_page.click_login_button().click_forgot_password_button().click_go_to_login_page_button()
    assert login_page.is_submit_login_button_visible(), "Login page is not opened"


@pytest.mark.smoke
def test_invalid_sign_up_alert_visible(open_main_page):
    main_page = open_main_page
    login_page = main_page.click_login_button().click_submit_sign_up_button()
    assert login_page.is_invalid_sign_up_alert_visible(), "No alert is visible"

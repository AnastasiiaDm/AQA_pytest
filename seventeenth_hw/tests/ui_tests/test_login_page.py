import pytest


@pytest.mark.smoke
def test_login_page(open_login_page):
    login_page = open_login_page
    assert login_page.is_submit_login_button_visible(), "Login button is not displayed"


@pytest.mark.smoke
def test_is_google_sign_up_button_exist(open_login_page):
    login_page = open_login_page
    assert login_page.is_google_sign_up_button_exist(), "Sign up by google button is not displayed"


@pytest.mark.smoke
def test_authorize(open_login_page, env):
    login_page = open_login_page
    authorize = login_page.authorize(env.email, env.password)
    assert authorize.is_header_logout_button_exist(), "User not authorized"


@pytest.mark.smoke
def test_open_forgot_password_page(open_login_page):
    login_page = open_login_page
    forgot_password = login_page.click_forgot_password_button()
    assert forgot_password.is_recover_password_submit_visible(), "Forgot password page is not opened"


@pytest.mark.smoke
def test_open_login_page_from_forgot_password_page(open_login_page):
    login_page = open_login_page
    return_login_page = login_page.click_forgot_password_button().click_go_to_login_page_button()
    assert return_login_page.is_submit_login_button_visible(), "Login page is not opened"


@pytest.mark.smoke
def test_invalid_sign_up_alert_visible(open_login_page):
    login_page = open_login_page
    alert = login_page.click_submit_sign_up_button()
    assert alert.is_invalid_sign_up_alert_visible(), "No alert is visible"

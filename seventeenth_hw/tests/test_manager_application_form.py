import pytest

from seventeenth_hw.utilities.config_reader import get_manager_application_form_name_key, \
    get_manager_application_form_phone_key, get_manager_application_form_text_key


@pytest.mark.regression
def test_exist_phone_onfocus(open_main_page):
    main_page = open_main_page
    form = main_page.click_search_submit().click_manager_application_button()
    assert form.is_phone_onfocus_exist(), "Manager application form onfocus is not displayed"


@pytest.mark.smoke
def test_close_form(open_main_page):
    main_page = open_main_page
    form = main_page.click_search_submit().click_manager_application_button()
    assert form.is_form_visible()
    form.click_exit_button()
    assert form.is_form_invisible(), "Manager application form is displayed"


@pytest.mark.regression
def test_submit_empty_fields(open_main_page):
    main_page = open_main_page
    submit = main_page.click_search_submit().click_manager_application_button().click_submit_button()
    assert submit.is_form_visible(), "Manager application form is not displayed"
    assert submit.are_required_fields_unfilled(), "Required fields ane not displayed"


@pytest.mark.smoke
def test_send_message(open_main_page):
    main_page = open_main_page
    fill_form = main_page.click_search_submit().click_manager_application_button().send_message(
        get_manager_application_form_name_key(),
        get_manager_application_form_phone_key(),
        get_manager_application_form_text_key())
    # here might be assert fill_form.is_manager_application_form_popup_invisible() but I decided not to disturb operators
    assert fill_form.is_form_visible(), "Manager application form is not displayed"


@pytest.mark.regression
@pytest.mark.xfail
def test_exist_name_text_uk(open_main_page):
    main_page = open_main_page
    actual_text = main_page.click_search_submit().click_manager_application_button().get_name_text()
    assert actual_text == "Ім'я:", "Manager application form name text is invalid or not in Ukrainian"


@pytest.mark.regression
@pytest.mark.xfail
def test_exist_phone_text_uk(open_main_page):
    main_page = open_main_page
    actual_text = main_page.click_search_submit().click_manager_application_button().get_phone_text()
    assert actual_text == "Номер телефону:", "Manager application form name text is invalid or not in Ukrainian"


@pytest.mark.regression
@pytest.mark.xfail
def test_exist_comment_text_uk(open_main_page):
    main_page = open_main_page
    actual_text = main_page.click_search_submit().click_manager_application_button().get_comment_text()
    assert actual_text == "Напишіть товар, який ви шукайте:", "Manager application form name text is invalid or not in Ukrainian"

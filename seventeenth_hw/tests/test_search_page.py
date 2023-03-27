import pytest

from seventeenth_hw.utilities.config_reader import get_search_key, get_search_id_key


@pytest.mark.regression
def test_go_to_main_page_from_search_result(open_main_page):
    main_page = open_main_page
    main_page_url = main_page.click_search_submit().click_site_header_logo()
    assert main_page_url.is_main_page_url_matches(), "Url doesnt match"


@pytest.mark.smoke
def test_open_manager_application_form(open_main_page):
    main_page = open_main_page
    manager_application_form = main_page.click_search_submit().click_manager_application_button()
    assert manager_application_form.is_form_visible(), "Manager application form is not displayed"


@pytest.mark.smoke
def test_is_search_result_text_appropriate(open_main_page):
    main_page = open_main_page
    search = main_page.set_search_key(get_search_key()).click_search_submit().get_search_result_text()
    assert search == f'"{get_search_key()}"', f"Search result key not equal '{get_search_key()}'"


@pytest.mark.smoke
def test_exist_item_list(open_main_page):
    main_page = open_main_page
    search = main_page.set_search_key(get_search_key()).click_search_submit()
    assert search.get_item_list_located(), "Item list is not displayed"


@pytest.mark.smoke
def test_exist_recent_news(open_main_page):
    main_page = open_main_page
    search = main_page.click_search_submit()
    assert search.is_recent_articles_active(), "Recent news are not displayed"


@pytest.mark.smoke
def test_click_popular_news(open_main_page):
    main_page = open_main_page
    search = main_page.click_search_submit().click_popular_news_button()
    assert search.is_popular_articles_active(), "Popular news are not displayed"


@pytest.mark.regression
def test_click_popular_news(open_main_page):
    main_page = open_main_page
    search = main_page.click_search_submit().click_popular_news_button().click_recent_news_button()
    assert search.is_recent_articles_active(), "Recent news are not displayed"


@pytest.mark.regression
def test_is_compare_value_0(open_main_page):
    main_page = open_main_page
    search = main_page.set_search_key(get_search_id_key()).click_search_submit()
    assert search.is_compare_value_0() == '0', "Compare value not equal 0"


@pytest.mark.smoke
def test_add_to_cart(open_main_page):
    main_page = open_main_page
    search = main_page.set_search_key(get_search_id_key()).click_search_submit().click_add_to_cart_button()
    assert search.is_cart_popup_displayed, "Cart popup is not displayed"


@pytest.mark.smoke
def test_open_cart_page_with_order(open_main_page):
    main_page = open_main_page
    search = main_page.set_search_key(get_search_id_key()).click_search_submit().click_add_to_cart_button().\
        click_cart_page_button()
    assert search.is_exist_order_block, "Order block is not displayed"

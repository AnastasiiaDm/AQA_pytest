import pytest

from seventeenth_hw.utilities.config_reader import get_search_key, get_invalid_search_key, get_search_id_key, \
    get_invalid_discount_key


@pytest.mark.regressoin
def test_is_exist_empty_cart_video(open_main_page):
    main_page = open_main_page
    cart_page = main_page.click_cart_button()
    assert cart_page.is_exist_empty_cart_video(), "No video is displayed in empty cart page"


@pytest.mark.regressoin
def test_is_exist_empty_cart_text_uk(open_main_page):
    main_page = open_main_page
    cart_page = main_page.click_cart_button().get_empty_cart_text()
    assert cart_page == "Ваш кошик порожній. Що тепер буде з Всесвіту?\n" \
                        "Додайте товар, заповніть порожнечу в душі котика 🤗", "Empty cart text is not displayed"


@pytest.mark.regressoin
def test_to_main_page_from_empty_cart_page(open_main_page):
    main_page = open_main_page
    cart_page = main_page.click_cart_button().click_home_button()
    assert cart_page.is_main_page_url_matches(), "Url doesnt match"


@pytest.mark.smoke
def test_open_cart_page_with_order(open_main_page):
    main_page = open_main_page
    order = main_page.set_search_key(get_search_id_key()).click_search_submit().click_add_to_cart_button(). \
        click_cart_page_button().get_order_id_text()
    assert order == f'Артикул: {get_search_id_key()}', "Order id doesn't match"


@pytest.mark.smoke
def test_add_invalid_discount(open_main_page):
    main_page = open_main_page
    order = main_page.set_search_key(get_search_id_key()).click_search_submit().click_add_to_cart_button(). \
        click_cart_page_button().set_discount_key(get_invalid_discount_key()).click_discount_submit_button()
    assert order.is_open_invalid_discount_popup(), "Invalid discount popup is not displayed"


@pytest.mark.smoke
def test_close_invalid_discount_popup(open_main_page):
    main_page = open_main_page
    order = main_page.set_search_key(get_search_id_key()).click_search_submit().click_add_to_cart_button(). \
        click_cart_page_button().set_discount_key(get_invalid_discount_key()).click_discount_submit_button(). \
        click_popup_close_button()
    assert order.is_close_invalid_discount_popup(), "Invalid discount popup is displayed"


@pytest.mark.smoke
def test_continue_shopping(open_main_page):
    main_page = open_main_page
    order = main_page.set_search_key(get_search_id_key()).click_search_submit().click_add_to_cart_button(). \
        click_cart_page_button().click_continue_shopping_button()
    assert order.is_main_page_url_matches(), "Url doesnt match"

import pytest


@pytest.mark.regressoin
def test_is_exist_empty_cart_video(open_empty_cart_page):
    cart_page = open_empty_cart_page
    assert cart_page.is_exist_empty_cart_video_exist(), "No video is displayed in empty cart page"


@pytest.mark.regressoin
def test_is_exist_empty_cart_text_uk(open_empty_cart_page):
    cart_page = open_empty_cart_page
    cart_text = cart_page.wait_until_warning_visible().text
    assert cart_text == "Ваш кошик порожній. Що тепер буде з Всесвіту?\n" \
                        "Додайте товар, заповніть порожнечу в душі котика 🤗", "Empty cart text is not displayed"


@pytest.mark.regressoin
def test_to_main_page_from_empty_cart_page(open_empty_cart_page, env):
    cart_page = open_empty_cart_page
    home_page = cart_page.click_home_button()
    assert home_page.is_page_url_matches(env.app_url), f"Url doesnt match {env.app_url}"


@pytest.mark.smoke
def test_open_cart_page_with_order(open_cart_page_with_item, env):
    cart_page = open_cart_page_with_item
    order = cart_page.get_order_id_text()
    assert order == f'Артикул: {env.search_id_key}', "Order id doesn't match"


@pytest.mark.smoke
def test_add_invalid_discount(open_cart_page_with_item, env):
    cart_page = open_cart_page_with_item
    discount = cart_page.set_discount_key(env.invalid_key).click_discount_submit_button()
    assert discount.is_invalid_discount_popup_opened(), "Invalid discount popup is not displayed"


@pytest.mark.smoke
def test_close_invalid_discount_popup(open_cart_page_with_item, env):
    cart_page = open_cart_page_with_item
    discount = cart_page.set_discount_key(env.invalid_key).click_discount_submit_button(). \
        click_popup_close_button()
    assert discount.is_invalid_discount_popup_closed(), "Invalid discount popup is displayed"


@pytest.mark.smoke
def test_continue_shopping(open_cart_page_with_item, env):
    cart_page = open_cart_page_with_item
    order = cart_page.click_continue_shopping_button()
    assert order.is_page_url_matches(env.app_url), f"Url doesnt match {env.app_url}"

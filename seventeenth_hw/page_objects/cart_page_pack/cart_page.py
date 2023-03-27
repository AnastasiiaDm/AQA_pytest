from selenium.webdriver.common.by import By

from seventeenth_hw.page_objects.cart_page_pack.cart_page_locators import CartPageLocators
from seventeenth_hw.page_objects.main_page_pack.main_page_locators import MainPageLocators
from seventeenth_hw.utilities.config_reader import get_application_url
from seventeenth_hw.utilities.web_ui.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.__cart_locator = CartPageLocators()
        self.__main_locator = MainPageLocators()

    def is_exist_empty_cart_video(self):
        return self._wait_until_element_visible(self.__cart_locator.empty_cart_video)

    def get_empty_cart_text(self):
        return self._get_text(self.__main_locator.alert_warning)

    def click_home_button(self):
        self._click(self.__cart_locator.home_button)
        return self

    def is_main_page_url_matches(self):
        return self._wait_until_url_matches(get_application_url())

    def is_exist_order_block(self):
        return self._wait_until_element_located(self.__cart_locator.order_block)

    def get_order_id_text(self):
        return self._get_text(self.__cart_locator.order_id_text)

    def set_discount_key(self, key: str):
        self._send_keys(locator=self.__cart_locator.discount_input, value=key)
        return self

    def click_discount_submit_button(self):
        self._click(self.__cart_locator.discount_submit_button)
        return self

    def is_open_invalid_discount_popup(self):
        return self._wait_until_element_located(self.__cart_locator.invalid_discount_popup_active)

    def click_popup_close_button(self):
        self._click(self.__cart_locator.popup_close_button)
        return self

    def is_close_invalid_discount_popup(self):
        return self._wait_until_element_located(self.__cart_locator.invalid_discount_popup_active)

    def click_continue_shopping_button(self):
        self._click(self.__cart_locator.continue_shopping_button)
        return self

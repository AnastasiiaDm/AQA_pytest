from seventeenth_hw.page_objects.cart_page_pack.cart_page import CartPage
from seventeenth_hw.page_objects.login_page_pack.login_page import LoginPage
from seventeenth_hw.page_objects.main_page_pack.main_page_locators import MainPageLocators
from seventeenth_hw.page_objects.search_page_pack.search_page import SearchPage
from seventeenth_hw.utilities.config_reader import get_iphone_items_url, get_contact_url, get_application_url
from seventeenth_hw.utilities.web_ui.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.__main_page_locator = MainPageLocators()

    def set_search_key(self, key: str):
        self._send_keys(locator=self.__main_page_locator.search_input, value=key)
        return self

    def click_search_submit(self):
        self._click(self.__main_page_locator.search_submit_button)
        return SearchPage(self.browser)

    def click_search_submit_for_main(self):
        self._click(self.__main_page_locator.search_submit_button)
        return self

    def is_search_result_counter_displayed(self):
        element = self._wait_until_element_visible(self.__main_page_locator.search_result_counter)
        return element.is_displayed()

    def is_search_result_counter_invisible(self):
        return self._wait_until_element_invisible(self.__main_page_locator.search_result_counter)

    def is_warning_displayed(self):
        element = self._wait_until_element_visible(self.__main_page_locator.alert_warning)
        return element.is_displayed()

    def click_cart_button(self):
        self._click(self.__main_page_locator.cart_button)
        return CartPage(self.browser)

    # def click_cart_button_for_main(self):
    #     self._click(self.__main_page_locator.cart_button)
    #     return self

    def click_login_button(self):
        self._click(self.__main_page_locator.login_button)
        return LoginPage(self.browser)

    def is_iphone_items_url_matches(self):
        return self._wait_until_url_matches(get_iphone_items_url())

    def click_iphone_item(self):
        self._click_by_js(self.__main_page_locator.iphone_items_button)
        return self

    def is_promo_block_exist(self):
        return self._wait_until_element_visible(self.__main_page_locator.promo_block)

    def click_header_contact_button(self):
        self._click(self.__main_page_locator.header_contact_button)
        return self

    def is_contact_url_matches(self):
        return self._wait_until_url_matches(get_contact_url())

    def is_main_page_url_matches(self):
        return self._wait_until_url_matches(get_application_url())

    def is_header_logout_button_exist(self):
        element = self._wait_until_element_visible(self.__main_page_locator.header_logout_button)
        return element.is_displayed()


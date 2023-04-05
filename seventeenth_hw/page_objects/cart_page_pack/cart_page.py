from seventeenth_hw.page_objects.cart_page_pack.cart_page_locators import CartPageLocators
from seventeenth_hw.utilities.web_ui.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.__cart_locator = CartPageLocators()

    def is_exist_empty_cart_video_exist(self):
        element = self._wait_until_element_visible(self.__cart_locator.empty_cart_video)
        return element.is_displayed()

    def is_cart_popup_displayed(self):
        element = self._wait_until_element_visible(self.__cart_locator.cart_popup)
        return element.is_displayed()

    def click_home_button(self):
        from seventeenth_hw.page_objects.main_page_pack.main_page import MainPage
        self._click(self.__cart_locator.home_button)
        return MainPage(self.browser)

    def is_order_block_exist(self):
        element = self._wait_until_element_located(self.__cart_locator.order_block)
        return element.is_displayed()

    def get_order_id_text(self):
        return self._get_text(self.__cart_locator.order_id_text)

    def set_discount_key(self, value: str):
        self._send_keys(locator=self.__cart_locator.discount_input, value=value)
        return self

    def click_discount_submit_button(self):
        self._click(self.__cart_locator.discount_submit_button)
        return self

    def is_invalid_discount_popup_opened(self):
        element = self._wait_until_element_located(self.__cart_locator.invalid_discount_popup_active)
        return element.is_displayed()

    def click_popup_close_button(self):
        self._click(self.__cart_locator.popup_close_button)
        return self

    def is_invalid_discount_popup_closed(self):
        element = self._wait_until_element_located(self.__cart_locator.invalid_discount_popup_active)
        return element.is_displayed()

    def click_continue_shopping_button(self):
        from seventeenth_hw.page_objects.main_page_pack.main_page import MainPage
        self._click(self.__cart_locator.continue_shopping_button)
        return MainPage(self.browser)

from selenium.webdriver.common.by import By

from seventeenth_hw.page_objects.cart_page_pack.cart_page import CartPage
from seventeenth_hw.page_objects.search_page_pack.search_page import SearchPage
from seventeenth_hw.utilities.web_ui.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    __search_input = (By.XPATH, "//*[@id='search_query_top']")
    __search_submit_button = (By.XPATH, "//*[@name='submit_search']")
    __cart_button = (By.XPATH, "//*[@id='cart']")

    def set_search_key(self, key: str):
        self._send_keys(locator=self.__search_input, value=key)
        return self

    def click_search_submit(self):
        self._click(self.__search_submit_button)
        return SearchPage(self.browser)

    def click_cart_button(self):
        self._click(self.__cart_button)
        return CartPage(self.browser)





from seventeenth_hw.page_objects.cart_page_pack.cart_page import CartPage
from seventeenth_hw.page_objects.main_page_pack.main_page_locators import MainPageLocators
from seventeenth_hw.page_objects.manager_application_form.manager_application_form import ManagerApplicationForm
from seventeenth_hw.page_objects.search_page_pack.search_page_locators import SearchLocators
from seventeenth_hw.utilities.web_ui.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.__main_page_locator = MainPageLocators()
        self.__search_locator = SearchLocators()

    def click_site_header_logo(self):
        self._click(self.__main_page_locator.header_logo)
        return self

    def click_manager_application_button(self):
        self._click(self.__search_locator.manager_application_button)
        return ManagerApplicationForm(self.browser)

    def get_search_result_text(self):
        return self._get_text(self.__search_locator.search_result_key)

    def get_item_list_located(self):
        return self._wait_until_all_elements_located(self.__search_locator.item_list)

    def click_item(self):
        self._click(self.__search_locator.item_list)
        return self

    def is_recent_articles_active(self):
        element = self._wait_until_element_visible(self.__search_locator.recent_articles_active)
        return element.is_displayed()

    def is_popular_articles_active(self):
        element = self._wait_until_element_visible(self.__search_locator.popular_articles_active)
        return element.is_displayed()

    def click_recent_news_button(self):
        self._click(self.__search_locator.recent_news_button)
        return self

    def click_popular_news_button(self):
        self._click(self.__search_locator.popular_news_button)
        return self

    def is_compare_value_equals_0(self):
        return self._get_text(self.__search_locator.compare_value)

    def click_add_to_cart_button(self):
        self._click(self.__search_locator.add_to_cart_button)
        return self

    def click_cart_page_button(self):
        self._click(self.__search_locator.cart_page_button)
        return CartPage(self.browser)

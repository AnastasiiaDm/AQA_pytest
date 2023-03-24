from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By

from seventeenth_hw.utilities.config_reader import get_application_url
# from seventeenth_hw.page_objects.main_page import MainPage
from seventeenth_hw.utilities.web_ui.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    __search_result_counter = (By.XPATH, "//*[@class='heading-counter']")
    __search_warning = (By.XPATH, "//*[@class='alert alert-warning']")
    __site_header_logo = (By.XPATH, "//*[@id='header_logo']")
    __manager_application_button = (By.XPATH, "//*[@class='button btn modalBtn']")
    __manager_application_form_popup = (By.XPATH, "//*[@class='search-form_block']")
    # __manager_application_form_name_field = ()
    __manager_application_form_phone_field = (By.XPATH, "//*[@name='mask_user_num_search']")
    # __manager_application_form_phone_index = (By.XPATH, "//*[@value='+38']")
    __manager_application_form_phone_index = "value='+38'"

    def is_search_result_counter_displayed(self):
        element = self._wait_until_element_visible(self.__search_result_counter)
        return element.is_displayed()

    def is_search_warning_displayed(self):
        element = self._wait_until_element_visible(self.__search_warning)
        return element.is_displayed()

    def is_search_warning_invisible(self):
        return self._wait_until_element_invisible(self.__search_warning)

    def is_search_result_counter_invisible(self):
        return self._wait_until_element_invisible(self.__search_result_counter)

    def click_site_header_logo(self):
        self._click(self.__site_header_logo)
        return self

    def is_main_page_url_matches(self):
        return self._wait_until_url_matches(get_application_url())

    def click_manager_application_button(self):
        self._click(self.__manager_application_button)
        return self

    def is_manager_application_form_popup_invisible(self):
        return self._wait_until_element_visible(self.__manager_application_form_popup)

    def is_phone_index_exist(self):
        return self._find_attribute_in_locator(self.__manager_application_form_phone_field,
                                               self.__manager_application_form_phone_index)

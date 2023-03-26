from seventeenth_hw.page_objects.main_locators import MainLocators
from seventeenth_hw.page_objects.manager_application_form.manager_application_form import ManagerApplicationForm
from seventeenth_hw.page_objects.manager_application_form.manager_application_form_locators import \
    ManagerApplicationFormLocators
from seventeenth_hw.page_objects.search_page_pack.search_page_locators import SearchLocators
from seventeenth_hw.utilities.config_reader import get_application_url
from seventeenth_hw.utilities.web_ui.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.__main_locator = MainLocators()
        self.__search_locator = SearchLocators()
        self.__manager_form_locator = ManagerApplicationFormLocators()

    def is_search_result_counter_displayed(self):
        element = self._wait_until_element_visible(self.__search_locator.search_result_counter)
        return element.is_displayed()

    def is_search_warning_displayed(self):
        element = self._wait_until_element_visible(self.__main_locator.alert_warning)
        return element.is_displayed()

    def is_search_warning_invisible(self):
        return self._wait_until_element_invisible(self.__main_locator.alert_warning)

    def is_search_result_counter_invisible(self):
        return self._wait_until_element_invisible(self.__search_locator.search_result_counter)

    def click_site_header_logo(self):
        self._click(self.__main_locator.header_logo)
        return self

    def is_main_page_url_matches(self):
        return self._wait_until_url_matches(get_application_url())

    def click_manager_application_button(self):
        self._click(self.__search_locator.manager_application_button)
        return ManagerApplicationForm(self.browser)


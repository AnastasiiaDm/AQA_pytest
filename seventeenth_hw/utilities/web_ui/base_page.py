from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seventeenth_hw.utilities.web_ui.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.__wait = WebDriverWait(self.browser, 10, 1)
        self.__base_page_locator = BasePageLocators()

    def _wait_until_element_located(self, locator):
        return self.__wait.until(EC.presence_of_element_located(locator))

    def _wait_until_all_elements_located(self, locator):
        return self.__wait.until(EC.presence_of_all_elements_located(locator))

    def _wait_until_element_clickable(self, locator):
        return self.__wait.until(EC.element_to_be_clickable(locator))

    def _wait_until_element_visible(self, locator):
        return self.__wait.until(EC.visibility_of_element_located(locator))

    def _wait_until_element_invisible(self, locator):
        return self.__wait.until(EC.invisibility_of_element_located(locator))

    def _send_keys(self, locator, value, is_clear=True):
        element = self._wait_until_element_located(locator)
        if is_clear:
            element.clear()
        element.send_keys(value)

    def _click(self, locator):
        self._wait_until_element_clickable(locator).click()

    def _wait_until_url_matches(self, url):
        return self.__wait.until(EC.url_to_be(url))

    def _find_attribute_in_locator(self, locator, attribute):
        return self.__wait.until(EC.element_attribute_to_include(locator, attribute))

    def _get_text(self, locator):
        element = self._wait_until_element_located(locator)
        return element.text

    def _click_by_js(self, locator):
        return self.browser.execute_script('arguments[0].click()', self._wait_until_element_located(locator))

    def wait_until_warning_visible(self):
        return self._wait_until_element_located(self.__base_page_locator.alert_warning)

    def wait_until_warning_invisible(self):
        return self._wait_until_element_invisible(self.__base_page_locator.alert_warning)

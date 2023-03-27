from seventeenth_hw.page_objects.login_page_pack.login_page_locators import LoginPageLocators
from seventeenth_hw.page_objects.main_page_pack.main_page_locators import MainPageLocators
from seventeenth_hw.utilities.web_ui.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.__login_locator = LoginPageLocators()

    def is_submit_login_button_visible(self):
        return self._wait_until_element_visible(self.__login_locator.submit_login_button)

    def is_google_sign_up_button_exist(self):
        return self._wait_until_element_located(self.__login_locator.google_sign_up)

    def set_login_email(self, key: str):
        self._send_keys(locator=self.__login_locator.login_email_input, value=key)
        return self

    def set_password_email(self, key: str):
        self._send_keys(locator=self.__login_locator.password_input, value=key)
        return self

    def click_submit_login_button(self):
        self._click(self.__login_locator.submit_login_button)
        return self

    def authorize(self, email: str, password: str):
        self.set_login_email(email)
        self.set_password_email(password)
        self.click_submit_login_button()
        return self

    def click_forgot_password_button(self):
        self._click(self.__login_locator.forgot_password_button)
        return self

    def click_submit_sign_up_button(self):
        self._click(self.__login_locator.submit_sign_up_button)
        return self

    def is_invalid_sign_up_alert_visible(self):
        return self._wait_until_element_visible(self.__login_locator.invalid_sign_up_alert)

    def is_recover_password_submit_visible(self):
        return self._wait_until_element_visible(self.__login_locator.recover_password_submit)

    def click_go_to_login_page_button(self):
        self._click(self.__login_locator.go_to_login_page_button)
        return self

    def is_header_logout_button_exist(self):
        return self._wait_until_element_visible(self.__login_locator.header_logout_button)


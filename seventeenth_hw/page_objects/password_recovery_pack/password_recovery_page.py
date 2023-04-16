from seventeenth_hw.page_objects.password_recovery_pack.password_recovery_page_locators import \
    PasswordRecoveryPageLocators
from seventeenth_hw.utilities.web_ui.base_page import BasePage

from seventeenth_hw.utilities.web_ui.decorators import allure_step


@allure_step
class PasswordRecoveryPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.__password_recovery_locator = PasswordRecoveryPageLocators()

    def is_recover_password_submit_visible(self):
        element = self._wait_until_element_visible(self.__password_recovery_locator.recover_password_submit)
        return element.is_displayed()

    def click_go_to_login_page_button(self):
        self._click(self.__password_recovery_locator.go_to_login_page_button)
        from seventeenth_hw.page_objects.login_page_pack.login_page import LoginPage
        return LoginPage(self.browser)

from seventeenth_hw.page_objects.manager_application_form.manager_application_form_locators import \
    ManagerApplicationFormLocators
from seventeenth_hw.utilities.web_ui.base_page import BasePage


class ManagerApplicationForm(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.__manager_form_locator = ManagerApplicationFormLocators()

    __phone_onfocus_attribute = "onfocus"

    def is_form_visible(self):
        return self._wait_until_element_visible(self.__manager_form_locator.popup)

    def is_phone_onfocus_exist(self):
        return self._find_attribute_in_locator(self.__manager_form_locator.phone_input, self.__phone_onfocus_attribute)

    def click_exit_button(self):
        return self._click(self.__manager_form_locator.exit_button)

    def is_form_invisible(self):
        return self._wait_until_element_invisible(self.__manager_form_locator.popup)

    def set_name_key(self, key: str):
        self._send_keys(locator=self.__manager_form_locator.name_input, value=key)
        return self

    def set_phone_key(self, key: str):
        self._send_keys(locator=self.__manager_form_locator.phone_input, value=key)
        return self

    def set_comment_key(self, key: str):
        self._send_keys(locator=self.__manager_form_locator.comment_input, value=key)
        return self

    def click_submit_button(self):
        self._click(self.__manager_form_locator.submit_button)
        return self

    def send_message(self, name, phone, text):
        self.set_name_key(name)
        self.set_phone_key(phone)
        self.set_comment_key(text)
        # here might be one more method "click_manager_application_form_submit_button()" but I decided not to disturb operators
        return self

    def is_name_invalid(self):
        return self._wait_until_element_located(self.__manager_form_locator.name_invalid)

    def is_phone_invalid(self):
        return self._wait_until_element_located(self.__manager_form_locator.phone_invalid)

    def is_comment_invalid(self):
        return self._wait_until_element_located(self.__manager_form_locator.comment_invalid)

    def are_required_fields_unfilled(self):
        self.is_name_invalid()
        self.is_phone_invalid()
        self.is_comment_invalid()
        return self

    def get_name_text(self):
        return self._get_text(self.__manager_form_locator.name_text)

    def get_phone_text(self):
        return self._get_text(self.__manager_form_locator.phone_text)

    def get_comment_text(self):
        return self._get_text(self.__manager_form_locator.comment_text)

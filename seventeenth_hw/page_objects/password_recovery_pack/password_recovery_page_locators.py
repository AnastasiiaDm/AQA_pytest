from selenium.webdriver.common.by import By
from seventeenth_hw.utilities.web_ui.locator import Locator


class PasswordRecoveryPageLocators:
    def __init__(self):
        self.__recover_password_submit = Locator(By.XPATH, "//*[@class='btn btn-outline button button-medium btn-sm']")
        self.__go_to_login_page_button = Locator(By.XPATH, "//*[@class='pull-left']")

    @property
    def recover_password_submit(self):
        return self.__recover_password_submit.get_locator()

    @property
    def go_to_login_page_button(self):
        return self.__go_to_login_page_button.get_locator()

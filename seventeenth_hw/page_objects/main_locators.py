from selenium.webdriver.common.by import By
from seventeenth_hw.utilities.web_ui.locator import Locator


class MainLocators:
    def __init__(self):
        self.__alert_warning = Locator(By.XPATH, "//*[@class='alert alert-warning']")
        self.__header_logo = Locator(By.XPATH, "//*[@id='header_logo']")

    @property
    def alert_warning(self):
        return self.__alert_warning.get_locator()

    @property
    def header_logo(self):
        return self.__header_logo.get_locator()
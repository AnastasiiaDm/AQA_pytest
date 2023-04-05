from selenium.webdriver.common.by import By
from seventeenth_hw.utilities.web_ui.locator import Locator


class BasePageLocators:
    def __init__(self):
        self.__alert_warning = Locator(By.XPATH, "//*[@class='alert alert-warning']")

    @property
    def alert_warning(self):
        return self.__alert_warning.get_locator()
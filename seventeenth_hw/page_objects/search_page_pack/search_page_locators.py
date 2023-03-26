from selenium.webdriver.common.by import By
from seventeenth_hw.utilities.web_ui.locator import Locator


class SearchLocators:
    def __init__(self):
        self.__search_result_counter = Locator(By.XPATH, "//*[@class='heading-counter']")
        self.__manager_application_button = Locator(By.XPATH, "//*[@class='button btn modalBtn']")

    @property
    def search_result_counter(self):
        return self.__search_result_counter.get_locator()

    @property
    def manager_application_button(self):
        return self.__manager_application_button.get_locator()

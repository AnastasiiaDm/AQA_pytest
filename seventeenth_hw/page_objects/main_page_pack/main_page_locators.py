from selenium.webdriver.common.by import By
from seventeenth_hw.utilities.web_ui.locator import Locator


class MainPageLocators:
    def __init__(self):
        self.__search_input = Locator(By.XPATH, "//*[@id='search_query_top']")
        self.__search_submit_button = Locator(By.XPATH, "//*[@name='submit_search']")
        self.__search_result_counter = Locator(By.XPATH, "//*[@class='heading-counter']")
        self.__cart_button = Locator(By.XPATH, "//*[@id='cart']")

    @property
    def search_input(self):
        return self.__search_input.get_locator()

    @property
    def search_submit_button(self):
        return self.__search_submit_button.get_locator()

    @property
    def search_result_counter(self):
        return self.__search_result_counter.get_locator()

    @property
    def cart_button(self):
        return self.__cart_button.get_locator()

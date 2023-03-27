from selenium.webdriver.common.by import By
from seventeenth_hw.utilities.web_ui.locator import Locator


class MainPageLocators:
    def __init__(self):
        self.__search_input = Locator(By.XPATH, "//*[@id='search_query_top']")
        self.__search_submit_button = Locator(By.XPATH, "//*[@name='submit_search']")
        self.__search_result_counter = Locator(By.XPATH, "//*[@class='heading-counter']")
        self.__cart_button = Locator(By.XPATH, "//*[@class='title-cart pull-right']")
        self.__login_button = Locator(By.XPATH, "//*[@class='login']")

        self.__alert_warning = Locator(By.XPATH, "//*[@class='alert alert-warning']")
        self.__header_logo = Locator(By.XPATH, "//*[@id='header_logo']")
        self.__iphone_items_button = Locator(By.XPATH,
                                           "//*[@class='submenu-level-0_18 sub fullwidth clearfix']//*[@title='iPhone']")
        self.__apple_store_button = Locator(By.XPATH, "//*[@title='Apple Store']")
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

    @property
    def login_button(self):
        return self.__login_button.get_locator()

    @property
    def alert_warning(self):
        return self.__alert_warning.get_locator()

    @property
    def header_logo(self):
        return self.__header_logo.get_locator()

    @property
    def iphone_items_button(self):
        return self.__iphone_items_button.get_locator()

    @property
    def apple_store_button(self):
        return self.__apple_store_button.get_locator()

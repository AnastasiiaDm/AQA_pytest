from selenium.webdriver.common.by import By
from seventeenth_hw.utilities.web_ui.locator import Locator


class MainPageLocators:
    def __init__(self):
        self.__search_input = Locator(By.XPATH, "//*[@id='search_query_top']")
        self.__search_submit_button = Locator(By.XPATH, "//*[@name='submit_search']")
        self.__search_result_counter = Locator(By.XPATH, "//*[@class='heading-counter']")
        self.__cart_button = Locator(By.XPATH, "//*[@class='title-cart pull-right']")
        self.__login_button = Locator(By.XPATH, "//*[@class='login']")

        self.__header_logo = Locator(By.XPATH, "//*[@id='header_logo']")
        self.__iphone_items_button = Locator(By.XPATH,
                                             "//*[@class='submenu-level-0_18 sub fullwidth clearfix']//*[@title='iPhone']")
        self.__promo_block = Locator(By.XPATH, "//*[@class='row promo-block-at-home']")
        self.__header_contact_button = Locator(By.XPATH,
                                               "//*[@class='sf-menu clearfix menu-content']//*[contains(@href, 'contact-us')]")
        self.__header_logout_button = Locator(By.XPATH, "//*[@class='header_user_info pull-right']//*[@class='logout']")

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
    def header_logo(self):
        return self.__header_logo.get_locator()

    @property
    def iphone_items_button(self):
        return self.__iphone_items_button.get_locator()

    @property
    def header_contact_button(self):
        return self.__header_contact_button.get_locator()

    @property
    def promo_block(self):
        return self.__promo_block.get_locator()

    @property
    def header_logout_button(self):
        return self.__header_logout_button.get_locator()

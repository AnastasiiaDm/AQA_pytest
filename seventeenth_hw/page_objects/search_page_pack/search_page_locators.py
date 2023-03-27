from selenium.webdriver.common.by import By
from seventeenth_hw.utilities.web_ui.locator import Locator


class SearchLocators:
    def __init__(self):
        self.__search_result_key = Locator(By.XPATH, "//*[@class='page-heading product-listing']/*[@class='lighter']")
        self.__item_list = Locator(By.XPATH, "//*[@class='product_list grid row category-ajax']/child::*")
        self.__manager_application_button = Locator(By.XPATH, "//*[@class='button btn modalBtn']")
        self.__recent_news_button = Locator(By.XPATH, "//*[contains(@href, 'recent_news')]")
        self.__popular_news_button = Locator(By.XPATH, "//*[contains(@href, 'pop_news')]")
        self.__recent_articles_block_active = Locator(By.XPATH,
                                                      "//*[@id='smartblog_recent_news']/self::*[contains(@class, 'active')]")
        self.__popular_articles_block_active = Locator(By.XPATH,
                                                       "//*[@id='smartblog_pop_news']/self::*[contains(@class, 'active')]")
        self.__compare_value = Locator(By.XPATH,
                                       "//*[@class='sortPagiBar clearfix row']//*[@class='total-compare-val']")
        self.__add_to_cart_button = Locator(By.XPATH, "//*[contains(@class, 'ajax_add_to_cart_button')]")
        self.__cart_popup = Locator(By.XPATH, "//*[@id='layer_cart']/self::*[contains(@style, 'display: block')]")
        self.__cart_page_button = Locator(By.XPATH, "//*[@class='btn btn-warning button pull-right']/child::span")

    @property
    def search_result_key(self):
        return self.__search_result_key.get_locator()

    @property
    def item_list(self):
        return self.__item_list.get_locator()

    @property
    def manager_application_button(self):
        return self.__manager_application_button.get_locator()

    @property
    def recent_news_button(self):
        return self.__recent_news_button.get_locator()

    @property
    def popular_news_button(self):
        return self.__popular_news_button.get_locator()

    @property
    def recent_articles_active(self):
        return self.__recent_articles_block_active.get_locator()

    @property
    def popular_articles_active(self):
        return self.__popular_articles_block_active.get_locator()

    @property
    def compare_value(self):
        return self.__compare_value.get_locator()

    @property
    def add_to_cart_button(self):
        return self.__add_to_cart_button.get_locator()

    @property
    def cart_popup(self):
        return self.__cart_popup.get_locator()

    @property
    def cart_page_button(self):
        return self.__cart_page_button.get_locator()

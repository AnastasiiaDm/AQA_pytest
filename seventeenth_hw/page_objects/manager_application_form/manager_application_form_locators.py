from selenium.webdriver.common.by import By
from seventeenth_hw.utilities.web_ui.locator import Locator


class ManagerApplicationFormLocators:
    def __init__(self):
        self.__form_popup = Locator(By.XPATH, "//*[@class='search-form_block']")
        self.__name_input = Locator(By.XPATH, "//*[@id='user_name_search']")
        self.__phone_input = Locator(By.XPATH, "//*[@name='mask_user_num_search']")
        self.__comment_input = Locator(By.XPATH, "//*[@id='text_comment_search']")
        self.__submit_button = Locator(By.XPATH, "//*[@id='btn-search_submit']")
        self.__exit_button = Locator(By.XPATH, "//*[@id='modalSearch']/descendant::*[@class='close-krestick']")
        self.__name_invalid = Locator(By.XPATH, "//*[@id='user_name_search']/self::*[@class='valid-input notvalid']")
        self.__phone_invalid = Locator(By.XPATH,
                                       "//*[@name='mask_user_num_search']/self::*[@class='mask_user_num_search notvalid']")
        self.__comment_invalid = Locator(By.XPATH,
                                         "//*[@id='text_comment_search']/self::*[@class='valid-input notvalid']")
        # 2 Bohdan: please, don't judge the following locators from the start. The realisation of index here is tied to
        # it's element and would't be affected if elements order would be changed
        self.__name_text = Locator(By.XPATH, "//*[@id='user_name_search']/preceding-sibling::label[1]")
        self.__phone_text = Locator(By.XPATH, "//*[@id='user_num_search']/preceding-sibling::label[1]")
        self.__comment_text = Locator(By.XPATH, "//*[@id='text_comment_search']/preceding-sibling::label[1]")

    @property
    def popup(self):
        return self.__form_popup.get_locator()

    @property
    def name_input(self):
        return self.__name_input.get_locator()

    @property
    def phone_input(self):
        return self.__phone_input.get_locator()

    @property
    def comment_input(self):
        return self.__comment_input.get_locator()

    @property
    def submit_button(self):
        return self.__submit_button.get_locator()

    @property
    def exit_button(self):
        return self.__exit_button.get_locator()

    @property
    def name_invalid(self):
        return self.__name_invalid.get_locator()

    @property
    def phone_invalid(self):
        return self.__phone_invalid.get_locator()

    @property
    def comment_invalid(self):
        return self.__comment_invalid.get_locator()

    @property
    def name_text(self):
        return self.__name_text.get_locator()

    @property
    def phone_text(self):
        return self.__phone_text.get_locator()

    @property
    def comment_text(self):
        return self.__comment_text.get_locator()

from selenium.webdriver.common.by import By
from seventeenth_hw.utilities.web_ui.locator import Locator


class CartPageLocators:
    def __init__(self):
        self.__empty_cart_video = Locator(By.XPATH, "//*[@class='video-bg-tor']")
        self.__home_button = Locator(By.XPATH, "//*[@class='to-home button add_to_cart btn']")
        self.__order_block = Locator(By.XPATH, "//*[@id='order-detail-content']")
        self.__order_id_text = Locator(By.XPATH, "//*[@class='product_reference row']")
        self.__discount_input = Locator(By.XPATH, "//*[@id='discount_name']")

        self.__discount_submit_button = Locator(By.XPATH, "//*[@id='submitAddDiscount']")
        self.__invalid_discount_popup_active = Locator(By.XPATH,
                                                       "//*[@id='opc_modal'][contains(@style, 'display: block')]")
        self.__popup_close_button = Locator(By.XPATH, "//*[@class='close']")
        self.__invalid_discount_popup_inactive = Locator(By.XPATH,
                                                         "//*[@id='opc_modal'][contains(@style, 'display: none')]")
        self.__continue_shopping_button = Locator(By.XPATH, "//*[@class='continue']")

    @property
    def empty_cart_video(self):
        return self.__empty_cart_video.get_locator()

    @property
    def home_button(self):
        return self.__home_button.get_locator()

    @property
    def order_block(self):
        return self.__order_block.get_locator()

    @property
    def order_id_text(self):
        return self.__order_id_text.get_locator()

    @property
    def discount_input(self):
        return self.__discount_input.get_locator()

    @property
    def discount_submit_button(self):
        return self.__discount_submit_button.get_locator()

    @property
    def invalid_discount_popup_active(self):
        return self.__invalid_discount_popup_active.get_locator()

    @property
    def popup_close_button(self):
        return self.__popup_close_button.get_locator()

    @property
    def invalid_discount_popup_inactive(self):
        return self.__invalid_discount_popup_inactive.get_locator()

    @property
    def continue_shopping_button(self):
        return self.__continue_shopping_button.get_locator()

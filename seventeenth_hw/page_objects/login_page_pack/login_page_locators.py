from selenium.webdriver.common.by import By
from seventeenth_hw.utilities.web_ui.locator import Locator


class LoginPageLocators:
    def __init__(self):
        self.__submit_login_button = Locator(By.XPATH, "//*[@id='SubmitLogin']")
        self.__login_email_input = Locator(By.XPATH, "//*[@id='email']")
        self.__password_input = Locator(By.XPATH, "//*[@id='passwd']")
        self.__google_sign_up_button = Locator(By.XPATH, "//*[@id='gp-link']")
        self.__forgot_password_button = Locator(By.XPATH, "//*[@class='lost_password form-group']/a")

        self.__submit_sign_up_button = Locator(By.XPATH, "//*[@id='SubmitCreate']")
        self.__invalid_sign_up_alert = Locator(By.XPATH, "//*[@id='create_account_error']")

    @property
    def submit_login_button(self):
        return self.__submit_login_button.get_locator()

    @property
    def login_email_input(self):
        return self.__login_email_input.get_locator()

    @property
    def password_input(self):
        return self.__password_input.get_locator()

    @property
    def google_sign_up(self):
        return self.__google_sign_up_button.get_locator()

    @property
    def forgot_password_button(self):
        return self.__forgot_password_button.get_locator()

    @property
    def submit_sign_up_button(self):
        return self.__submit_sign_up_button.get_locator()

    @property
    def invalid_sign_up_alert(self):
        return self.__invalid_sign_up_alert.get_locator()

from selenium.webdriver import Chrome, Firefox
from seventeenth_hw.utilities.config_reader import get_application_url
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service

__CHROME = 1
__FIREFOX = 2


def browser_factory(browser_id: int):
    if int(browser_id) == __CHROME:
        return Chrome(service=Service(ChromeDriverManager().install()))
    if int(browser_id) == __FIREFOX:
        return Firefox(service=Service(GeckoDriverManager().install()))
    else:
        return Chrome(service=Service(ChromeDriverManager().install()))

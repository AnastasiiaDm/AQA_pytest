from selenium.webdriver import Chrome, Firefox
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from argparse import ArgumentParser

__CHROME = 1
__FIREFOX = 2


def browser_factory(browser_id: int):
    if int(browser_id) == __CHROME:
        return Chrome(service=Service(ChromeDriverManager().install()))
    if int(browser_id) == __FIREFOX:
        return Firefox(service=Service(GeckoDriverManager().install()))
    else:
        return Chrome(service=Service(ChromeDriverManager().install()))

#
# class Chrome:
#     def __init__(self):
#         Chrome(service=Service(ChromeDriverManager().install()))
#
# class Firefox:
#     def __init__(self):
#         Firefox(service=Service(GeckoDriverManager().install()))

# parser = ArgumentParser(description='Parser')
# parser.add_argument('--browser', help='Browser name', default='chrome')
# args = parser.parse_args()
#
# if args.browser.lower() == 'chrome':
#     Chrome()
# elif args.browser.lower() == 'firefox':
#     Firefox()
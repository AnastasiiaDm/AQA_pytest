"""
Find web page.
Write 30 XPATH locators for this page using XPath Axes and Wildcards. Some of them should have more than 3 steps.
For 10 XPATH locators write 10 CSS locators which find the same element
"""
from selenium.webdriver import Chrome


def test_web_elements():
    browser = Chrome('chromedriver.exe')
    browser.maximize_window()
    browser.get('https://dou.ua/')

    logo_locator = "//*[@class='logo']//a"
    footer_right_part_locator = "//*[@id='txtGlobalSearch']/../ancestor::div[@class='right-part']"
    unfollowed_lang_locator = "//*[@class='footer-lang-switch']/a[@rel='nofollow']"
    copyright_locator = "//*[@class='footer-lang-switch']/parent::div[@class]"
    support_locator = "//*[contains(text(), 'support')]"
    footer_gamedev_locator = "//*[contains(@class, '__gamedev')]"
    black_ball_2_locator = "//*[@class='b-index-links']/following::li[@num='2']/."
    sponsor_macpaw_locator = "//*[@class='b-block b-sponsors']/child::div/child::div/*[contains(@href, 'macpaw')]"
    sponsor_evoplay_locator = "//*[contains(@href, 'evo') and @target='_blank']"
    max_header_locator = "//*[@id='max-header-adv-id']"

    facebook_meta_name_locator = "//*[@name='facebook-domain-verification']"
    header_locator = "//*[@class='b-head']"
    popular_articles_locator = "//*[@class='b-articles-switch']/descendant::option/ancestor::li/a"
    tech_articles_title_locator = "//*[@class='title __separated']/preceding::div[@class='b-block']/div[@class='title __separated']"
    hot_vacancies_list = "//*[@class='title __hot']/following::ul[@class='vacancies-list']/li"
    adv_event_list = "//*[@class='b-adv-events']/child::div"
    second_line_of_footer_slider_locator = "//*[@class='b-footer-slider m-hide']/div/following-sibling::div"
    users_count_locator = "//*[contains(@href, 'facebook')]/preceding-sibling::span/a"
    header_relocate_button = "//*[contains(@href, 'relo')]/attribute::title"
    forum_locator = "//*[@class='b-head']//child::node()/*[contains(@href, 'forum')]"

    send_article_locator = "//a[@class='all-materials __add']"
    ukrainian_lang_locator = "//*[text()='Українська']"
    find_programmers_in_Jinni_locator = "//*[@class='m-hide']/a[@target='_blank']"
    main_locator = "//*[@class='m-hide']/self::li"
    close_header_locator = ".//*[@id='max-header-close-id']"
    max_header_img_locator = ".//*[@id='max-header-adv-id']/descendant::img"
    b_index_block_locator = "//*[@class='b-index-links']/descendant-or-self::ul"
    all_materials_locator = "//*[@class='links']/descendant-or-self::div/descendant-or-self::a[@class='all-materials']"
    news_title_locator = "//*[@class='b-articles b-articles_tech b-articles__compact']/ancestor-or-self::div[@class='b-block b-block_news']/div[@class='title']"
    first_job_locator = "//*[@class='b-index-links']/descendant::*[contains(@href, 'first-job')]"

    root_locator_xpath = "html"
    root_locator_css = ":root"

    slider_articles_locator_xpath = "//*[@id='slideArticles']"
    slider_articles_locator_css = "#slideArticles"

    b_header_locator_xpath = "//*[@class='b-head']"
    b_header_locator_css = ".b-head"

    blog_block_locator_xpath = "//*[@class='b-index-columnisty b-block']"
    blog_block_locator_css = ".b-index-columnisty.b-block"

    blog_block_title_locator_xpath = "//*[@class='b-index-columnisty b-block']/*[@class='title __separated']"
    blog_block_title_locator_css = ".b-index-columnisty .title"

    search_input_locator_xpath = "//*[@class='search']/input"
    search_input_locator_css = ".search input"

    login_registration_locator_xpath = "//a[@id='login-link']"
    login_registration_locator_css = "a#login-link"

    header_gamedev_locator_xpath = "//*[@title='GameDev']"
    header_gamedev_locator_css = "[title='GameDev']"

    sponsor_luxoft_locator_xpath = "//a[contains(@href,'https://www.luxoft.com')]"
    sponsor_luxoft_locator_css = "a[href^='https://www.luxoft.com']"

    last_header_locator_xpath = "//li[@class='m-last']"
    last_header_locator_css = "li.m-last"

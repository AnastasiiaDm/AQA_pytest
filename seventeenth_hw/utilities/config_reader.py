import configparser

abs_path = '/Users/nasik/PycharmProjects/AQA_pytest/seventeenth_hw/configurations/configuration.ini'
config = configparser.RawConfigParser()
config.read(abs_path)


def get_application_url():
    return config.get('add_data', 'app_url')


def get_user_creds():
    return (config.get('user_data', 'email'),
            config.get('user_data', 'password'))


def get_browser_id():
    return config.get('browser_data', 'browser_id')


def get_search_key():
    return config.get('search_data', 'search_key')


def get_invalid_search_key():
    return config.get('search_data', 'invalid_key')

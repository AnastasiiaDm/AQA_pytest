import configparser
from constants import ROOT_DIR

abs_path = f'{ROOT_DIR}/seventeenth_hw/configurations/configuration.ini'
config = configparser.RawConfigParser()
config.read(abs_path)

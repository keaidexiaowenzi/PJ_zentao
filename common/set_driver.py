from selenium import webdriver
from common.config_value import ConfigUtils


def set_driver():
    conf = ConfigUtils()
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    url= conf.get_zentao_url
    driver.get(url)
    return driver


if __name__ == '__main__':
    set_driver()

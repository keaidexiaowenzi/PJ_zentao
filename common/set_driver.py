from selenium import webdriver
from self import self

from common.config_value import ConfigUtils
from selenium.webdriver.chrome.options import Options

class Set_Driver(object):
    # def __init__(self,driver_name=ConfigUtils.get_driver_name):
    #     self.driver_name = driver_name
    #
    #
    # def get_driver(self):
    #     if self.driver_name.lower()== "chrome" :
    #         return  self.set_Chrome_driver()
    #     elif self.driver_name.lower() == "firefox":
    #         return self.set_Firefox_driver()


    def set_Chrome_driver():
        chrome_options=Options()
        # 谷歌文档提到需要加上这个规避bug
        chrome_options.add_argument('--disable-gpu')
        # 设置默认编码为utf-8
        chrome_options.add_argument('lang=zh_CN.UTF-8')
        # 取消chrome受自动化软件控制提示
        chrome_options.add_experimental_option('useAutomationExtension',False)
        #取消chrome受自动化软件控制提示
        chrome_options.add_experimental_option("excludeSwitches",['enable-automation'])
        conf = ConfigUtils()
        driver = webdriver.Chrome(options=chrome_options)
        driver.implicitly_wait(10)
        driver.maximize_window()
        url= conf.get_zentao_url
        driver.get(url)
        return driver

    def set_Firefox_driver(self):
        conf = ConfigUtils()
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.maximize_window()
        url= conf.get_zentao_url
        driver.get(url)
        return driver





if __name__ == '__main__':
    # set_Driver.set_Firefox_driver(self)
    Set_Driver.set_Chrome_driver()

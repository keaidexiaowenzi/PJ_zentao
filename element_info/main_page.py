import os
import time

from common.base_page import BasePage
from common import set_driver
from common.config_value import ConfigUtils
from function import login


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        # 把loginpage定义的driver对象转移到mainpage来
        # self.driver = login.driver
        # 属性-》页面上的控件
        self.product_menu = {'element_name': '产品菜单',
                             'locator_type': 'xpath',
                             'locator_value': '//nav/ul/li[2]/a[@href="/zentao3/www/product-index-no.html"]',
                             'timeout': 5}
        self.username_showspan = {'element_name': '登录用户名称',
                                  'locator_type': 'xpath',
                                  'locator_value': '//li/a/span[1][@class="user-name"]',
                                  'timeout': 3}
        self.user_Modular = {'element_name': '用户模块展示',
                             'locator_type': 'xpath',
                             'locator_value': '//li/a/span[1][@class="user-name"]',
                             'timeout': 3}
        self.logout_button = {'element_name': '退出登录按钮',
                              'locator_type': 'xpath',
                              'locator_value': '//li[13]/a[@href="/zentao3/www/user-logout.html"]',
                              'timeout': 3}

    # 方法-》控件的操作
    # 进入产品页面
    def goto_product(self):
        # self.product_menu.click()
        # logger.info("进入产品页面成功")
        self.click(self.product_menu)

    # 获取用户名
    def get_username(self):
        # value = self.username_showspan.text
        # logger.info("获取用户名成功")
        # return value
        text = self.get(self.username_showspan)
        return text

    # 显示用户菜单栏
    def click_userModular(self):
        self.click(self.user_Modular)

    # 点击退出登录按钮
    def click_logout(self):
        self.click(self.logout_button)



if __name__ == "__main__":
    conf = ConfigUtils()
    driver = set_driver.set_driver()
    login.test_login(conf.get_zentao_url, conf.get_username, conf.get_password, driver)
    # time.sleep(5)
    mainpage = MainPage(driver)
    # 用例2：获取主页当前登录人姓名
    username = mainpage.get_username()
    print(username)
    time.sleep(3)
    # 用例3： 进入产品页面
    mainpage.goto_product()
    # 用例4：展示主页用户菜单
    mainpage.click_userModular()
    # 用例5：退出登录
    mainpage.click_logout()

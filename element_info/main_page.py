import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from element_info.login_page import LoginPage
from commen.log_utils import logger
from commen.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

        # 把loginpage定义的driver对象转移到mainpage来
        # self.driver = login.driver
        # 属性-》页面上的控件
        self.product_menu = {'element_name': '产品菜单',
                             'locator_type': 'xpath',
                             'locator_value': '//nav/ul/li[2]/a[@href="/zentao/product-index-no.html"]',
                             'timeout': 5}
        self.username_showspan = {'element_name': '登录用户名称',
                                  'locator_type': 'xpath',
                                  'locator_value': '//span[@class="user-name"]',
                                  'timeout': 3}
        self.user_Modular = {'element_name': '用户模块展示',
                             'locator_type': 'xpath',
                             'locator_value': '//li/a/span[1][@class="user-name"]',
                             'timeout': 3}
        self.logout_button = {'element_name': '退出登录按钮',
                              'locator_type': 'xpath',
                              'locator_value': '//li/ul/li[13]/a[@href="/zentao/user-logout.html"]',
                              'timeout': 3}
        # self.product_menu = self.driver.find_element(By.XPATH,'//nav/ul/li[2]/a[@href="/zentao/product-index-no.html"]')
        # self.username_showspan = self.driver.find_element(By.XPATH, '//span[@class="user-name"]')
        # self.user_Modular = self.driver.find_element(By.XPATH, '//li/a/span[1][@class="user-name"]')
        # self.logout_button = self.driver.find_element(By.XPATH, '//li/ul/li[13]/a[@href="/zentao/user-logout.html"]')

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
        self.get(self.username_showspan)

    # 显示用户菜单栏
    def click_userModular(self):
        self.click(self.user_Modular)

    # 点击退出登录按钮
    def click_logout(self):
        self.click(self.logout_button)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open_url('http://wangyawen.w3.luyouxia.net/zentao/user-login.html')
    login_page.input_username('wangyawen')
    login_page.input_password('wyw123456.')
    login_page.click_login()
    time.sleep(20)

    mainpage = MainPage(driver)
    mainpage.refresh()
    mainpage.get_username()
    mainpage.goto_product()
    mainpage.click_userModular()
    mainpage.click_logout()

    # time.sleep(3)
    # username = mainpage.get_username()
    # print(username)
    # time.sleep(3)
    # mainpage.goto_product()
    # time.sleep(3)
    # mainpage.click_userModular()
    # time.sleep(3)
    # mainpage.click_logout()

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from element_info.login_page import LoginPage
from commen.log_utils import logger


class MainPage(object):

    def __init__(self):
        login = LoginPage()
        login.input_username('wangyawen')
        login.input_password('wyw123456.')
        login.click_login()
        # 把loginpage定义的driver对象转移到mainpage来
        self.driver = login.driver
        # 属性-》页面上的控件
        time.sleep(3)
        self.product_menu = self.driver.find_element(By.XPATH,'//nav/ul/li[2]/a[@href="/zentao/product-index-no.html"]')
        self.username_showspan = self.driver.find_element(By.XPATH, '//span[@class="user-name"]')
        self.user_Modular = self.driver.find_element(By.XPATH, '//li/a/span[1][@class="user-name"]')
        self.logout_button = self.driver.find_element(By.XPATH, '//li/ul/li[13]/a[@href="/zentao/user-logout.html"]')

    # 方法-》控件的操作
    # 进入产品页面
    def goto_product(self):
        time.sleep(3)
        self.product_menu.click()
        logger.info("进入产品页面成功")

    # 获取用户名
    def get_username(self):
        value = self.username_showspan.text
        logger.info("获取用户名成功")

        return value

    # 显示用户菜单栏
    def click_userModular(self):
        self.user_Modular.click()

    # 点击退出登录按钮
    def click_logout(self):
        self.logout_button.click()


if __name__ == "__main__":
    mainpage = MainPage()
    time.sleep(3)
    username = mainpage.get_username()
    print(username)
    time.sleep(3)
    mainpage.goto_product()
    time.sleep(3)
    mainpage.click_userModular()
    time.sleep(3)
    mainpage.click_logout()

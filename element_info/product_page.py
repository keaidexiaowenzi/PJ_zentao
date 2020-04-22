import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from element_info.login_page import LoginPage
from commen.log_utils import logger
from commen.base_page import BasePage
from element_info.main_page import MainPage


class ProductPage(BasePage):

    def __init__(self, driver):
        # 继承父类
        super().__init__(driver)
        # 属性-》页面上的控件
        self.addproduct_Button= {'element_name': '添加产品控件',
                             'locator_type': 'xpath',
                             'locator_value': '//div[2]/div/a[@href="/zentao3/www/product-create.html"]',
                             'timeout': 5}
        self.requirement_menu = {'element_name': '需求菜单',
                                  'locator_type': 'xpath',
                                  'locator_value': '//ul/li[1]/a[@href="/zentao3/www/product-browse-1.html"]',
                                  'timeout': 3}
        self.plan_menu = {'element_name': '计划菜单',
                             'locator_type': 'xpath',
                             'locator_value': '//nav/ul/li[3]/a[@href="/zentao3/www/productplan-browse-1.html"]',
                             'timeout': 3}
        self.productmain_Modular= {'elem ent_name': '产品主页模块',
                              'locator_type': 'xpath',
                              'locator_value': '//div[1]/ul/li[2]/a[2]/i[@class="icon-arrow-right text-primary""]',
                              'timeout': 3}
    # 方法-》控件的操作
    # 进入添加产品页面
    def goto_addproduct(self):
        self.click(self.addproduct_Button)

    # 进入需求页面
    def goto_requirement(self):
        self.click(self.requirement_menu)

    # 进入计划页面
    def goto_plan(self):
        self.click(self.plan_menu)

    # 产品主页模块展示
    def click_productmain(self):
        self.click(self.productmain_Modular)


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

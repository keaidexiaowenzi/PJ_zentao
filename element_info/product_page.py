from common.base_page import BasePage
from common.config_value import ConfigUtils
from common import set_driver
from element_info import main_page
from function import login
import time

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
        self.productmain_Modular= {'element_name': '产品主页模块',
                              'locator_type': 'xpath',
                              'locator_value': '//div[1]/div[1]/div/button[@class="btn"]',
                              'timeout': 3}
        self.allproduct_button= {'element_name': '所有产品按钮',
                              'locator_type': 'xpath',
                              'locator_value': '//div[1]/div/ul/li[2]/a[@href="/zentao3/www/product-all.html"]',
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

    # 进入所有产品页面
    def click_allproduct(self):
        self.click(self.allproduct_button)

if __name__ == "__main__":
    conf = ConfigUtils()
    driver = set_driver.set_driver()
    login.test_login(conf.get_zentao_url, conf.get_username, conf.get_password, driver)
    # time.sleep(5)
    mainpage= main_page.MainPage(driver)
    mainpage.goto_product()
    # 产品主页
    productpage=ProductPage(driver)
    # 用例6：进入添加产品页面
    productpage.goto_addproduct()
    time.sleep(2)
    # 用例7：进入需求页面
    productpage.goto_requirement()
    time.sleep(2)
    # 用例8：进入计划页面
    productpage.goto_plan()
    time.sleep(3)
    # 用例9: 产品主页模块展示
    productpage.click_productmain()
    time.sleep(3)
    # 用例10：进入所有产品页面
    productpage.click_allproduct()
    time.sleep(3)
    # 退出登录
    login.test_logout(driver)

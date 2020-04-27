from common.elements_data_excel import get_page_info
from common.log_utils import logger
from common.base_page import  BasePage
from common import set_driver
import time
from common.config_value import ConfigUtils
from function import login
from selenium.webdriver.common.by import By
from common.elements_data_yml import ElementYamlData

# 读取excel为数据源
# elements = get_page_info('LoginPage')
# 读取yaml文件为数据源
element_infos = ElementYamlData('LoginPage')
elements=element_infos.read_yaml()

class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

        # 方式三：
        self.username_inputbox = elements['username_inputbox']
        self.password_inputbox = elements['password_inputbox']
        self.login_button = elements['login_button']

        # 方式二：
        # self.username_inputbox={'element_name':'用户名输入框',
        #                         'locator_type':'xpath',
        #                         'locator_value':'//input[@name="account"]',
        #                         'timeout':3}
        # self.password_inputbox={'element_name':'密码输入框',
        #                         'locator_type':'xpath',
        #                         'locator_value':'//input[@name="password"]',
        #                         'timeout':3}
        # self.login_button={'element_name':'登录按钮',
        #                         'locator_type':'xpath',
        #                         'locator_value':'//button[@id="submit"]',
        #                         'timeout':10}
        # 方式一：
        # self.driver = webdriver.Chrome()
        # self.driver.implicitly_wait(10)
        # self.driver.maximize_window()
        # self.driver.get('http://wangyawen.w3.luyouxia.net/zentao/user-login.html')
        # # 属性-》页面上的控件
        # time.sleep(3)
        # self.username_inputbox = self.driver.find_element(By.XPATH, '//input[@name="account"]')
        # self.password_inputbox = self.driver.find_element(By.XPATH, '//input[@name="password"]')
        # self.login_button = self.driver.find_element(By.XPATH, '//button[@id="submit"]')
        # self.keeplogin_checkbox = self.driver.find_element(By.XPATH, '//input[@id="keepLoginon"]')

    # 方法-》控件的操作
    # 输入用户名
    def input_username(self, username):
        # self.username_inputbox.send_keys(username)
        # logger.info('用户名输入框输入：'+ str(username))
        self.input(self.username_inputbox,username)
    # 输入密码
    def input_password(self, password):
        # self.password_inputbox.send_keys(password)
        # logger.info('密码输入框输入：'+str(password))
        self.input(self.password_inputbox,password)
    # 点击登录按钮
    def click_login(self):
        # self.login_button.click()
        # logger.info("点击登录按钮成功")
        self.click(self.login_button)

if __name__ == "__main__":
    # 用例1：登录成功用例
    conf = ConfigUtils()
    driver = set_driver.set_driver()
    login.test_login(conf.get_zentao_url,conf.get_username,conf.get_password,driver)
    time.sleep(3)

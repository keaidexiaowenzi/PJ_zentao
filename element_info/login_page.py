import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from commen.log_utils import logger
from commen.base_page import  BasePage
# current_path=os.path.dirname(__file__)
# driver_path=os.path.join(current_path,'../webdriver/chromerdriver')

class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.username_inputbox={'element_name':'用户名输入框',
                                'locator_type':'xpath',
                                'locator_value':'//input[@name="account"]',
                                'timeout':3}
        self.password_inputbox={'element_name':'密码输入框',
                                'locator_type':'xpath',
                                'locator_value':'//input[@name="password"]',
                                'timeout':3}
        self.login_button={'element_name':'登录按钮',
                                'locator_type':'xpath',
                                'locator_value':'//button[@id="submit"]',
                                'timeout':10}

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
    driver=webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open_url('http://106.53.50.202:8999/zentao3/www/user-login-L3plbnRhbzYvd3d3Lw==.html')
    login_page.input_username('admin')
    login_page.input_password('a12345678')
    login_page.click_login()

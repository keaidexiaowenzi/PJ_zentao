import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from commen.log_utils import logger

# current_path=os.path.dirname(__file__)
# driver_path=os.path.join(current_path,'../webdriver/chromerdriver')

class LoginPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('http://wangyawen.w3.luyouxia.net/zentao/user-login.html')
        # 属性-》页面上的控件
        time.sleep(3)
        self.username_inputbox = self.driver.find_element(By.XPATH, '//input[@name="account"]')
        self.password_inputbox = self.driver.find_element(By.XPATH, '//input[@name="password"]')
        self.login_button = self.driver.find_element(By.XPATH, '//button[@id="submit"]')
        self.keeplogin_checkbox = self.driver.find_element(By.XPATH, '//input[@id="keepLoginon"]')

    # 方法-》控件的操作
    # 输入用户名
    def input_username(self, username):
        self.username_inputbox.send_keys(username)
        logger.info('用户名输入框输入：'+ str(username))

    # 输入密码
    def input_password(self, password):
        self.password_inputbox.send_keys(password)
        logger.info('密码输入框输入：'+str(password))

    # 点击登录按钮
    def click_login(self):
        self.login_button.click()
        logger.info("点击登录按钮成功")


if __name__ == "__main__":
    login = LoginPage()
    login.input_username('wangyawen')
    login.input_password('wyw123456.')
    login.click_login()

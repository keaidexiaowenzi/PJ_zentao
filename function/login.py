import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from element_info.login_page import LoginPage
from commen.log_utils import logger
from commen.base_page import BasePage
from element_info.main_page import MainPage

# 登录成功案例
def test_login_Success(username,password):
    driver=webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open_url('http://106.53.50.202:8999/zentao3/www/user-login-L3plbnRhbzYvd3d3Lw==.html')
    login_page.input_username(username)
    login_page.input_password(password)
    login_page.click_login()


def test_main():
    test_login_Success('admin','a12345678')
    mainpage = MainPage(driver)
    mainpage.refresh()
    mainpage.get_username()
    mainpage.goto_product()
    mainpage.click_userModular()
    mainpage.click_logout()
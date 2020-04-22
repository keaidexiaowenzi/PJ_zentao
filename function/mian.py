import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from element_info.login_page import LoginPage
from commen.log_utils import logger
from commen.base_page import BasePage
from element_info.main_page import MainPage

def main():

    mainpage = MainPage(driver)
    mainpage.refresh()
    mainpage.get_username()
    mainpage.goto_product()
    mainpage.click_userModular()
    mainpage.click_logout()
import os
import time

import mouse as mouse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from common.log_utils import logger
from selenium.webdriver.common.keys import Keys

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    # 浏览器操作封装->二次封装
    def open_url(self, url):
        self.driver.get(url)
        logger.info('打开url地址%s' % url)

    def set_browser_max(self):
        self.driver.maximize_window()
        logger.info('设置浏览器最大化')

    def refresh(self):
        self.driver.refresh()
        logger.info('浏览器刷新')

    def get_title(self):
        value = self.driver.title
        logger.info('获取标题：%s' % value)
        return value

    # 元素操作封装
    # 查找元素
    def find_element(self, element_info):
        locator_type_name = element_info['locator_type']
        locator_value_info = element_info['locator_value']
        locator_timeout = element_info['timeout']
        if locator_type_name == 'id':
            locator_type = By.ID
        elif locator_type_name == 'class':
            locator_type = By.CLASS_NAME
        elif locator_type_name == 'xpath':
            locator_type = By.XPATH
        elif locator_type_name == 'link_text':
            locator_type = By.LINK_TEXT
        elif locator_type_name == 'css':
            locator_type = By.CSS_SELECTOR
        elif locator_type_name == 'name':
            locator_type = By.NAME

        element = WebDriverWait(self.driver, int(locator_timeout)) \
            .until(lambda x: x.find_element(locator_type, locator_value_info))
        # element_info怎么来的
        logger.info('[%s]元素识别成功' % element_info['element_name'])
        return element

    # 点击操作
    def click(self, element_info):
        element = self.find_element(element_info)
        element.click()
        logger.info('对[%s]元素进行点击操作' % element_info['element_name'])

    # 输入操作
    def input(self, element_info, content):
        element = self.find_element(element_info)
        element.send_keys(content)
        logger.info('[%s]元素输入内容：%s' % (element_info['element_name'], content))

    # 获取文本
    def get(self, element_info):
        element = self.find_element(element_info)
        value = element.text
        logger.info('获取[%s]元素内容为：%s' % (element_info['element_name'], value))
        return value

    # 提交表单，submit() : 要求对象必须是表单
    def submit_to(self, element_info):
        element = self.find_element(element_info)
        element.submit()
        logger.info('提交[%s]表单' % element_info['element_name'])

    # frame处理
    # 进入frame框
    def goto_frame(self, element_info):
        self.driver.switch_to.frame(element_info)
        # self.driver.switch_to.default_content()
        logger.info('定位至[%s]frame框' % element_info['element_name'])

    # 退出frame框
    def outo_frame(self):
        self.driver.switch_to.default_content()
        logger.info('退出frame框')

    # alert处理
    # alert处理,返回alert/confirm/prompt中的文字内容
    def alert_text(self):
        value = self.driver.switch_to_alert().text()
        logger.info('获取alert元素内容为：%s' % value)
        return value

    # alert处理,accept: 点击确认按钮
    def alert_accept(self):
        self.driver.switch_to_alert().accept()
        logger.info('点击确认按钮')

    # alert处理,dismiss : 点击取消按钮如果有取消按钮的话
    def alert_dismiss(self):
        self.driver.switch_to_alert().dismiss()
        logger.info('点击取消按钮')

    # alert处理,sendKeys : 向prompt中输入文字
    def alert_sendKeys(self, content):
        self.driver.switch_to_alert().senkeys(content)
        logger.info('在alert元素中输入内容为：%s' % content)

# 鼠标事件
    # 鼠标右击元素
    def contextclick(self, element_info):
        element = self.find_element(element_info)
        ActionChains.context_click(element).perform()
        logger.info('鼠标右击[%s]元素' % element_info['element_name'])

    # 鼠标双击元素
    def doubleclick(self, element_info):
        element = self.find_element(element_info)
        ActionChains.double_click(element).perform()
        logger.info('鼠标双击[%s]元素' % element_info['element_name'])

    # 鼠标移动到一个元素上
    def move_to_element(self, element_info):
        element = self.find_element(element_info)
        ActionChains.move_to_element(element).perform()
        logger.info('鼠标移动到[%s]元素之上' % element_info['element_name'])

    # 鼠标左击元素
    def clickAndhold(self, element_info):
        element = self.find_element(element_info)
        ActionChains.click_and_hold(element).release().perform()
        logger.info('鼠标左击[%s]元素' % element_info['element_name'])

# 键盘事件
# key_down 模拟键盘摁下某个按键 key_up 松开某个按键，与sendkey连用完成一些操作，每次down必须up一次否则将出现异常
    # 全选数据
    def SelectAll(self):
        ActionChains.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL).perform()
        logger.info('全选当前数据')
    # 复制数据
    def copy(self):
        ActionChains.key_down(Keys.CONTROL).send_keys('C').key_up(Keys.CONTROL).perform()
        logger.info('复制当前选中数据')
    # 粘贴数据
    def stick(self):
        ActionChains.key_down(Keys.CONTROL).send_keys('V').key_up(Keys.CONTROL).perform()
        logger.info('粘贴当前复制数据')
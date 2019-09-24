import time
from io import BytesIO

from PIL import Image
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from chaojiying import Chaojiying

ACCOUNT = '18520895887'
PASSWORD = 'suxinwei1314a!'
# 超级鹰用户名、密码、软件ID、验证码类型
CHAOJIYING_USERNAME = 'suxinwei'
CHAOJIYING_PASSWORD = 'suxinwei1314a!'
CHAOJIYING_SOFT_ID = 'python_test'
CHAOJIYING_KIND = 9102


class CrackTouClick():
    def __init__(self):
        self.url = 'https://login.flyme.cn'
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.account = ACCOUNT
        self.password = PASSWORD
        self.chaojiying = Chaojiying(CHAOJIYING_USERNAME, CHAOJIYING_PASSWORD, CHAOJIYING_SOFT_ID)

    def __del__(self):
        self.browser.close()

    def open(self):
        """
        打开网页输入用户名密码
        :return: None
        """
        self.browser.get(self.url)
        account = self.wait.until(EC.presence_of_element_located((By.ID, 'account')))
        password = self.wait.until(EC.presence_of_element_located((By.ID, 'password')))
        account.send_keys(self.account)
        password.send_keys(self.password)

    def get_geetest_button(self):
        """
        获取初始验证按钮
        :return: 按钮对象
        """
        button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_radar_tip')))
        return button

    def get_screenshot(self):
        """
        获取网页截图
        :return: 截图对象
        """
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        return screenshot

    def get_position(self):
        """
        获取验证码位置
        :return: 验证码位置元组
        """
        img = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_tip_content')))
        time.sleep(2)
        location = img.location
        size = img.size
        top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size[
            'width']
        return (top, bottom, left, right)

    def get_geetest_image(self, name='captcha.png'):
        """
        获取验证码图片
        :param name:
        :return: 图片对象
        """
        top, bottom, left, right = self.get_position()
        print('验证码位置', top, bottom, left, right)
        screenshot = self.get_screenshot()
        captcha = screenshot.crop((left, top, right, bottom))
        return captcha

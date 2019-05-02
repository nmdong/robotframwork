
#!/usr/bin/python

# ********************************************************************
# This library mainly focused on Equinox Client with help of
# selenium remote webdriver.
# Author Dong Nguyen <nmdong@tma.com.vn>
# Date 30 Dec 2018
# *******************************************************************

# Python default packages used in this lib.

import unittest
import time,datetime,inspect
import logging
import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from selenium.webdriver import ActionChains
from random import randint

class Chrome(unittest.TestCase):
    '''
        This class will help to automate chrome for mac OS  use appium driver
    '''

    def __init__(self):
        logging.info('Start auto browser: chrome')
        self.chrome_driver = None
        self.obj_chrome = None
        self.address = "/AXApplication[@AXTitle='Google Chrome']/AXWindow[@AXTitle='New Tab - Google Chrome' and @AXSubrole='AXStandardWindow']/AXGroup[@AXTitle='New Tab - Google Chrome']/AXGroup[0]/AXTextField[@AXTitle='Address and search bar']"

    def launch_browser(self, client_ip=None, client_port=None, url=None):
        logging.info('Start function launch chrome browser for mac')
        self.obj_chrome = driver.Driver(client_ip=client_ip, client_port=client_port, browser='chrome', app_name='Google Chrome')
        self.chrome_driver = self.obj_chrome.get_driver()
        self.assertTrue(self.chrome_driver, 'Get chrome driver failed')
        wait = WebDriverWait(self.chrome_driver, 20)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.address)))
        self.chrome_driver.find_element_by_xpath(self.address).send_keys(url)
        ActionChains(self.chrome_driver).send_keys(Keys.ENTER).perform()
        logging.info('launch_browser successfully')
        return True

    def exit_app(self):
        print 'Quitting the WebDriver session'
        menubar = ['Chrome','Quit Google Chrome']
        self.obj_chrome.select_menu_item(self.chrome_driver, menubar)
        self.chrome_driver.quit()

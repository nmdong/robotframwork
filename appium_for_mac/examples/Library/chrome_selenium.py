
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
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from selenium.webdriver import ActionChains
from random import randint

class Chrome_Selenium(unittest.TestCase):
    '''
        This class will help to automate chrome for mac OS  use appium driver
    '''

    def __init__(self, client_ip=None, client_port=None):
        logging.info('Start auto browser: chrome')
        self.chrome_driver = None
        self.client_ip = client_ip
        self.client_port = client_port

    def launch_browser_use_selenium(self, url=None):
        '''
            * Function name: lauch_browser
            * Description: This function is used to launch web address
            * Parameters:
                + url: this is address web
                + title_web: title web
            * Author: Dong Nguyen
            * Date: Feb, 2019
            * Ex: lauch_browser  http://appium.io/
            * Modify by:
            * Date
        '''
        profile1 = webdriver.ChromeOptions()
        profile1.accept_untrusted_cert = True
        profile1.add_argument("--lang=en")
        profile1.add_argument("start-maximized")
        self.profile = profile1
        logging.info('Web Address:   %s' % url)
        d = self.profile.to_capabilities()
        d['loggingPrefs'] = {'browser': 'ALL'}
        self.chrome_driver = webdriver.Remote('http://' + self.client_ip + ':' + self.client_port + '/wd/hub', desired_capabilities=d)
        self.chrome_driver.get(url)
        self.chrome_driver.set_page_load_timeout(30)
        self.chrome_driver.switch_to.default_content()
        self.main_window = self.chrome_driver.current_window_handle
        logging.info('%s' % self.main_window)
        time.sleep(5)
        title_current = self.chrome_driver.title
        logging.info('Title: %s' % title_current)
        return self.chrome_driver

    def exit_app(self):
        print 'Quitting the WebDriver session'
        self.chrome_driver.quit()

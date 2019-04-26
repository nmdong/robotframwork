
#!/usr/bin/python

# ********************************************************************
# This library mainly focused on Equinox Client with help of
# selenium remote webdriver.
# Author Dong Nguyen <nmdong@tma.com.vn>
# Date 30 Dec 2018
# *******************************************************************

# Python default packages used in this lib.

import unittest
import sys
import os
import time,datetime,inspect
import subprocess
import logging

from appium import webdriver

class Driver(unittest.TestCase):
    '''
        This class will help to get driver
    '''

    def __init__(self, client_ip=None, client_port=None, browser='chrome', app_name=None):
        self.driver = None
        self.client_ip = client_ip
        self.client_port = client_port
        self.browser_client = browser
        self.app_name = app_name

    def get_driver(self):
        desired_capabilities = {
            'platformName': 'mac',
            'deviceName': 'ThoPham',
            'browserName': self.browser_client,
            'commandDelay': 50,
            'loopDelay': 1000,
            'implicitTimeout': 3000,
            'mouseMoveSpeed': 50,
            "screenShotOnError": 1,
            "--url-base": "wd/hub"
        }
        command_url = 'http://'+self.client_ip+':'+self.client_port+'/wd/hub'
        self.driver = webdriver.Remote(command_executor=command_url, desired_capabilities=desired_capabilities)
        self.driver.add_cookie({'name': 'mouse_speed', 'value': 200})
        logging.info('Opening the %s' %self.app_name)
        self.driver.get(self.app_name)
        if self.driver.window_handles:
            logging.info('Open window: %s' %(self.driver.window_handles))
            return self.driver
        self.fail('Cannot open application')
        return False

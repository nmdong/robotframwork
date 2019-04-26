
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
import driver

from appium import webdriver

class Calculator(unittest.TestCase):
    '''
        This class will help to automate calculator for mac OS
    '''

    def __init__(self):
        logging.info('Start auto Calculator app')
        self.windowPath = "/AXApplication[@AXTitle='Calculator']/AXWindow[0]"
        self.basicGroupPath = self.windowPath + "/AXGroup[1]"
        self.calculator_driver = None

    def numToAXPath(self, num):
        if num == 0:
            return self.basicGroupPath + "/AXButton[@AXDescription='zero']"
        elif num == 1:
            return self.basicGroupPath + "/AXButton[@AXDescription='one']"
        elif num == 2:
            return self.basicGroupPath + "/AXButton[@AXDescription='two']"
        elif num == 3:
            return self.basicGroupPath + "/AXButton[@AXDescription='three']"
        elif num == 4:
            return self.basicGroupPath + "/AXButton[@AXDescription='four']"
        elif num == 5:
            return self.basicGroupPath + "/AXButton[@AXDescription='five']"
        elif num == 6:
            return self.basicGroupPath + "/AXButton[@AXDescription='six']"
        elif num == 7:
            return self.basicGroupPath + "/AXButton[@AXDescription='seven']"
        elif num == 8:
            return self.basicGroupPath + "/AXButton[@AXDescription='eight']"
        elif num == 9:
            return self.basicGroupPath + "/AXButton[@AXDescription='nine']"
        else:
            return ""

    def lauch_app(self, client_ip=None, client_port=None):
        logging.info('Start function launch app calculator for mac')
        obj_calculator = driver.Driver(client_ip=client_ip, client_port=client_port, app_name='Calculator')
        self.calculator_driver = obj_calculator.get_driver()
        self.assertTrue(self.calculator_driver, 'Get calculator driver failed')
        logging.info('lauch_app successfully')
        return True

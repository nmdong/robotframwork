
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


from selenium.webdriver import ActionChains
from random import randint

class Calculator(unittest.TestCase):
    '''
        This class will help to automate calculator for mac OS
    '''

    def __init__(self):
        logging.info('Start auto Calculator app')
        self.windowPath = "/AXApplication[@AXTitle='Calculator']/AXWindow[0]"
        self.basicGroupPath = self.windowPath + "/AXGroup[1]"
        self.resultGroupPath = self.windowPath + "/AXGroup[0]"
        self.calculator_driver = None
        self.obj_calculator = None

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
        self.obj_calculator = driver.Driver(client_ip=client_ip, client_port=client_port, app_name='Calculator')
        self.calculator_driver = self.obj_calculator.get_driver()
        self.assertTrue(self.calculator_driver, 'Get calculator driver failed')
        logging.info('lauch_app successfully')
        return True

    def clickElement(self, element=None, useNativeEvents=0):
        if useNativeEvents > 0:
            # move and click the mouse like a user
            actions = ActionChains(self.calculator_driver)
            actions.click(element)
            actions.perform()
        else:
            # use the traditional accessibility action
            element.click()

    def do_some_calculations_with_clicks(self):
        print 'Clearing the calculator'
        button_clear = self.calculator_driver.find_element_by_xpath(self.basicGroupPath + "/AXButton[@AXDescription='clear']")
        self.clickElement(button_clear)

        rand1 = randint(0, 1000)
        rand2 = randint(0, 1000)

        print 'Entering the first number'
        for num in str(rand1):
            n = self.numToAXPath(int(num))
            print str(num) + ' --> ' + str(n)
            self.clickElement(self.calculator_driver.find_element_by_xpath(n))
            time.sleep(1)

        button_plus = self.calculator_driver.find_element_by_xpath(self.basicGroupPath + "/AXButton[@AXDescription='add']")
        print 'Clicking the "+" button'
        self.clickElement(button_plus)

        print 'Entering the second number'
        for num in str(rand2):
            n = self.numToAXPath(int(num))
            print str(num) + ' --> ' + str(n)
            self.clickElement(self.calculator_driver.find_element_by_xpath(n))
            time.sleep(2)

        button_equals = self.calculator_driver.find_element_by_xpath(self.basicGroupPath + "/AXButton[@AXDescription='equals']")
        print 'Clicking the "=" button'
        self.clickElement(button_equals)

        text_result = self.calculator_driver.find_element_by_xpath(self.resultGroupPath + "/AXStaticText[@AXDescription='main display']")
        print 'Reading result from screen'
        ActionChains(self.calculator_driver).move_to_element(text_result).perform()
        answer = text_result.text

        if int(answer) == (rand1 + rand2):
            print 'Correct Result: ' + answer
        else:
            print 'Incorect Result: ' + answer

    def do_some_calculations_with_keystrokes(self):
        print 'Clearing the calculator'
        button_clear = self.calculator_driver.find_element_by_xpath(self.basicGroupPath + "/AXButton[@AXDescription='clear']")
        self.clickElement(button_clear)

        rand1 = randint(0, 1000)
        rand2 = randint(0, 1000)

        print 'Typing the first number'
        ActionChains(self.calculator_driver).send_keys(str(rand1)).perform()

        print 'Typing the "+" button'
        ActionChains(self.calculator_driver).send_keys("+").perform()

        print 'Typing the second number'
        ActionChains(self.calculator_driver).send_keys(str(rand2)).perform()

        print 'Typing the "=" button'
        ActionChains(self.calculator_driver).send_keys("=").perform()

        print 'Reading result from screen'
        text_result = self.calculator_driver.find_element_by_xpath(self.resultGroupPath + "/AXStaticText[@AXDescription='main display']")
        ActionChains(self.calculator_driver).move_to_element(text_result).perform()
        answer = text_result.text

        if int(answer) == (rand1 + rand2):
            print 'Correct Result: ' + answer
        else:
            print 'Incorect Result: ' + answer

    def exit_app(self):
        print 'Quitting the WebDriver session'
        menubar = ['Calculator', 'Quit Calculator']
        self.obj_calculator.select_menu_item(self.calculator_driver, menubar)
        self.calculator_driver.quit()
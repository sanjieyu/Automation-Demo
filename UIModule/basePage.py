

# Author:Yi Sun(Tim) 2023-03-31

'''Page Object:Base Page'''

from selenium import webdriver
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
# from appium.webdriver.common.mobileby import MobileBy

class Factory(object):
    def __init__(self,driver):
        self.driver = driver

    # Factory Method
    def createDriver(self,driver):
        if driver == 'web':
            return WebUI(self.driver)
        elif driver == 'app':
            return AppUI(self.driver)

class WebDriver(object):
    def __init__(self,driver):
        self.driver = driver

    def findElement(self,*loc):
        '''Sigle Element locate'''
        try:
           # return self.driver.find_element(*loc)
           return WebDriverWait(self.driver,20).until(lambda x:x.find_element(*loc))
        except NoSuchElementException as e:
            print('Error Details{0}'.format(e.args[0]))

# class Login():
#     def __init__(self):
#         self.fp = None
#         self.username = None
#         self.password = None
#
#     def openfile(self):
#         try:
#             fileName = input('pls input a file; ')
#             self.fp = open("%s.txt" % fileName, 'r')
#             self.fp = open('../Test_Data/admin.txt', 'r')
#         except FileNotFoundError as rr:
#             print("file not found")
#
#     def readfile(self):
#         if self.fp:
#             lines = self.fp.readlines()
#             for i in lines:
#                 self.username = lines[0]
#                 self.password = lines[1]
#             print(self.username, self.password)
#             return self.username, self.password


class WebUI(WebDriver):
    def __str__(self):
        return 'WebUI'

class AppUI(WebDriver):
    def __str__(self):
        return 'AppUI'


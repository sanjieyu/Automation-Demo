# Author:Yi Sun(Tim) 2020-4-03

'''Test CRM Page'''

import unittest
from selenium import webdriver
from time import *
from UIModule.crm_page import *
from CommonModule.read_config import *

class CRMTest(unittest.TestCase,CRM_Page):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.config_read = ReadConfig()
        cls.url = cls.config_read.get_url()
        cls.admin_username = cls.config_read.admin_username()
        cls.admin_password = cls.config_read.admin_password()
        cls.login = Admin_Portal(cls.driver)
        cls.driver.get(cls.url)
        cls.login.login(cls.admin_username,cls.admin_password)
        cls.driver.implicitly_wait(5)
        cls.gocrm = CRM_Page(cls.driver)
        cls.gocrm.go_crm()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # @unittest.skip
    def test_CRM_001(self):
        '''Verify the title of CRM Page'''
        self.driver.implicitly_wait(5)
        self.assertEqual('RELATIONSHIP MANAGEMENT',self.check_title)

    def test_CRM_002(self):
        '''Verify the default Sections in CRM Page'''
        self.driver.implicitly_wait(5)
        self.assertEqual(('Dashboard','Company','Contact','Task'),self.check_defaultvalue)

if __name__ == '__main__':
    unittest.main(verbosity=2)

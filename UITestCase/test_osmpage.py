# Author:Yi Sun(Tim) 2023-5-22

'''Test CRM Page'''

import unittest
from selenium import webdriver
from time import *
from UIModule.osm_page import *
from CommonModule.read_config import *

class OSMTest(unittest.TestCase,OSM_Page):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.config_read = ReadConfig()
        cls.url = cls.config_read.get_url()
        cls.username = cls.config_read.admin_username()
        cls.password = cls.config_read.admin_password()
        cls.login = Admin_Portal(cls.driver)
        cls.driver.get(cls.url)
        cls.login.login(cls.username,cls.password)
        cls.driver.implicitly_wait(5)
        cls.goosm = OSM_Page(cls.driver)
        cls.goosm.go_osm()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_OSM_001(self):
        '''Verify the url of OSM Page'''
        self.driver.implicitly_wait(5)
        self.assertEqual(self.check_url,'https://portal.staging.itrazoadi.com/#/app/inventory-management')

    def test_OSM_002(self):
        '''Verify the title of OSM Page'''
        self.driver.implicitly_wait(5)
        self.assertEqual(self.check_title,'STOCK & ORDER MANAGEMENT')

    def test_OSM_003(self):
        '''Verify the default Sections in OSM Page'''
        self.driver.implicitly_wait(5)
        self.assertEqual(self.check_defaultvalue,('Dashboard','Procurement','Inventory','Quality Management'))

if __name__ == '__main__':
    unittest.main(verbosity=2)
# Author:Yi Sun(Tim) 2023-05-22

'''Test Sales Page'''

import unittest
from selenium import webdriver
from time import *
from UIModule.osm_sales import *
from CommonModule.read_config import *

class Test_Sales(unittest.TestCase,Sales_Page):
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
        # cls.goosm = OSM_Page(cls.driver)
        # cls.goosm.go_osm()
        cls.gosales = Sales_Page(cls.driver)
        cls.gosales.go_production()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_sales_001(self):
        '''Verify the default section in sales page'''
        self.driver.implicitly_wait(5)
        self.assertEqual(self.check_salessection,('Open (0)','Closed (0)','Cancelled (0)','Production Work Order (PWO) (0)'))

    def test_sales_002(self):
        '''Verify the default values in open section of sales page'''
        self.driver.implicitly_wait(5)
        self.assertEqual(self.check_opendefault,('  New Purchase Order','Create PWO'))

    def test_sales_003(self):
        '''Verify the search box in open section of sales page'''
        self.driver.implicitly_wait(5)
        self.assertEqual(self.check_opensearchbox,True)

    def test_sales_004(self):
        '''Verify the From date filter in open section of sales page'''
        self.driver.implicitly_wait(5)
        self.assertEqual(self.check_fromopen,True)

    def test_sales_005(self):
        '''Verify the To date filter in open section of sales page'''
        self.driver.implicitly_wait(5)
        self.assertEqual(self.check_toopen,True)

    def test_sales_006(self):
        '''Verify the columns in Open section of Sales page'''
        self.driver.implicitly_wait(5)
        self.assertEqual(self.check_opentable,('ORDER NO.','STATUS','CUSTOMER','PURPOSE','PAYMENT','PACKAGING','PRODUCTS','EXPECTED DELIVERY'))

    def test_sales_007(self):
        '''Verify the default values in closed section of sales page'''
        self.driver.implicitly_wait(5)
        self.go_closed
        self.driver.implicitly_wait(5)
        self.assertEqual(self.check_closeddefault,('  New Purchase Order'))

    def test_sales_008(self):
        '''Verify the search box in closed section of sales page'''
        self.driver.implicitly_wait(5)
        self.go_closed
        self.driver.implicitly_wait(5)
        self.assertEqual(self.check_closedsearchbox,True)

    def test_sales_009(self):
        '''Verify the From date filter in closed section of sales page'''
        self.driver.implicitly_wait(5)
        self.go_closed
        self.driver.implicitly_wait(5)
        self.assertEqual(self.check_fromclosed,True)

    def test_sales_010(self):
        '''Verify the To date filter in closed section of sales page'''
        self.driver.implicitly_wait(5)
        self.go_closed
        self.driver.implicitly_wait(5)
        self.assertEqual(self.check_toclosed,True)

    def test_sales_011(self):
        '''Verify the columns in closed section of Sales page'''
        self.driver.implicitly_wait(5)
        self.go_closed
        self.driver.implicitly_wait(5)
        self.assertEqual(self.check_closedtable,('ORDER NO.','STATUS','CUSTOMER','PURPOSE','PAYMENT','PACKAGING','PRODUCTS','EXPECTED DELIVERY'))


    def test_sales_012(self):
        '''Verify the default values in cancelled section of sales page'''
        self.driver.implicitly_wait(5)
        self.go_cancelled
        self.driver.implicitly_wait(5)
        self.assertEqual(self.check_canceldefault,('  New Purchase Order'))

    def test_sales_013(self):
        '''Verify the search box in cancelled section of sales page'''
        self.driver.implicitly_wait(5)
        self.go_cancelled
        self.driver.implicitly_wait(5)
        self.assertEqual(self.check_cancelsearchbox,True)

    def test_sales_014(self):
        '''Verify the From date filter in cancelled section of sales page'''
        self.driver.implicitly_wait(5)
        self.go_cancelled
        self.driver.implicitly_wait(5)
        self.assertEqual(self.check_fromcancel,True)

    def test_sales_015(self):
        '''Verify the To date filter in cancelled section of sales page'''
        self.driver.implicitly_wait(5)
        self.go_cancelled
        self.driver.implicitly_wait(5)
        self.assertEqual(self.check_tocancel,True)

    def test_sales_016(self):
        '''Verify the search box in pwo section of sales page'''
        self.driver.implicitly_wait(5)
        self.go_pwo
        self.driver.implicitly_wait(5)
        self.assertEqual(self.check_pwosearchbox,True)

    def test_sales_017(self):
        '''Verify the From date filter in pwo section of sales page'''
        self.driver.implicitly_wait(5)
        self.go_pwo
        self.driver.implicitly_wait(5)
        self.assertEqual(self.check_frompwo,True)

    def test_sales_018(self):
        '''Verify the To date filter in pwo section of sales page'''
        self.driver.implicitly_wait(5)
        self.go_pwo
        self.driver.implicitly_wait(5)
        self.assertEqual(self.check_topwo,True)

if __name__ == '__main__':
    unittest.main(verbosity=2)

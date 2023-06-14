# Author:Yi Sun(Tim) 2023-04-04

'''Test Company Page'''
import time
import unittest
from selenium import webdriver
from time import *
from UIModule.crm_company import *
from CommonModule.read_config import *

class CRM_Company_Test(unittest.TestCase,Company_page):
    @classmethod
    def setUpClass(cls) -> None:
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
        cls.gocompany = Company_page(cls.driver)
        cls.gocompany.go_company()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_company_001(self):
        '''Verify the default sescription for each element in Company Page'''
        self.driver.implicitly_wait(5)
        self.assertEqual(self.check_description,('All','Leads','  Add Company'))

    def test_company_002(self):
        '''Verify each column of the company list table'''
        self.driver.implicitly_wait(5)
        self.assertEqual(self.check_column,('BUSINESS RELATIONSHIP','COMPANY NAME','INDUSTRY','EMAIL','PHONE NUMBER','CREATED ON','STATUS','ACTIONS'))

    def test_company_003(self):
        '''Verify current url for company page'''
        self.driver.implicitly_wait(5)
        self.assertEqual(self.check_companyurl,('https://portal.staging.itrazoadi.com/#/app/relationship-management'))
    #
    # @unittest.skip
    def test_company_004(self):
        '''Verify the filter of Busniess Relationship'''
        self.driver.implicitly_wait(5)
        self.assertEqual(self.sort_relationship,('Customer','Supplier','Lead','Unassigned'))

    # @unittest.skip
    def test_company_005(self):
        '''Verify the filter of Status'''
        self.driver.refresh()
        self.go_company()
        sleep(2)
        # self.driver.implicitly_wait(10)
        self.assertEqual(self.sort_status,('Active'))

    def test_company_006(self):
        '''Verify the title of add company page'''
        self.driver.implicitly_wait(5)
        self.assertEqual(self.add_companyptitle,('Create Company'))

    def test_company_007(self):
        '''Verify the three section in the first page of add company'''
        self.driver.refresh()
        self.go_company()
        self.assertEqual(self.add_companyp1section,('Company','Primary Contact','Address'))

    def test_company_008(self):
        '''Verify the default elements in the first page of add company'''
        self.driver.refresh()
        self.go_company()
        self.assertEqual(self.add_companyp1,('* Fields marked with (*) are required.','Business Relationship','Company Name*','Country','ABN','Business Email*','Business Phone No.','Industry*','URL','Status','Comments'))

    def test_company_009(self):
        '''Verify the warning msg if doesn't input company name and industry in the first page of add company'''
        self.driver.refresh()
        self.go_company()
        self.assertEqual(self.add_p1_required,('Please enter the Company Name.','Please enter the Industry.'))

    def test_company_010(self):
        '''Verify the three section in 2nd page of add company'''
        self.driver.refresh()
        self.go_company()
        self.assertEqual(self.add_companyp2section,('Company','Primary Contact','Address'))

    def test_company_011(self):
        '''Verify the default elements for exist contact in the 2nd page of add company'''
        self.driver.refresh()
        self.go_company()
        self.assertEqual(self.add_companyp2_exsit,('* Fields marked with (*) are required.','Add existing','New','Contact*','Skip'))
    #
    def test_company_012(self):
        '''Verify the default elements for new contact in the 2nd page of add company'''
        self.driver.refresh()
        self.go_company()
        self.assertEqual(self.add_companyp2_new,('Title','First name*','Last Name*','Job Title*','Email*','Mobile No*','Skip'))
    #
    # @unittest.skip
    def test_company_013(self):
        '''Verify the warning msg if missing the mandatory values for new contact in the 2nd page of add company'''
        self.driver.refresh()
        self.go_company()
        self.assertEqual(self.add_p2_newrequired,('Please enter the First Name.','Please enter the Last Name.','Please enter the Job Title.','Please enter an Email.','Please enter the Phone Number.'))

    # # @unittest.skip
    def test_company_014(self):
        '''Verify the warning msg if missing the mandatory values for exist contact in the 2nd page of add company'''
        self.driver.refresh()
        self.go_company()
        self.assertEqual(self.add_p2_existrequired,('Please select a Contact.'))

    # @unittest.skip
    def test_company_015(self):
        '''Verify the Back function in the 2nd page of add company'''
        self.driver.refresh()
        self.go_company()
        self.assertEqual(self.add_p2_back,('Company Name*'))

    def test_company_016(self):
        '''Verify the Skip function in the 2nd page of add company'''
        self.driver.refresh()
        self.go_company()
        self.assertEqual(self.add_p2_skip,('Delivery Address'))

    def test_company_017(self):
        '''Verify the three section in the 3rd page of add company'''
        self.driver.refresh()
        self.go_company()
        self.assertEqual(self.add_companyp3section,('Company','Primary Contact','Address'))

    def test_company_018(self):
        '''Verify the default elements for delivery in the 3rd page of add company'''
        self.driver.refresh()
        self.go_company()
        self.assertEqual(self.add_companyp3_delivery,('* Fields marked with (*) are required.','Delivery Address','Unit/Suite','Street*','Country*','State*','Suburb/City*','Postcode*'))

    def test_company_019(self):
        '''Verify the default elements for billing in the 3rd page of add company'''
        self.driver.refresh()
        self.go_company()
        self.assertEqual(self.add_companyp3_billing,('Billing Address','Same as Delivery Address','Unit/Suite','Street','Country','State','Suburb/City','Postcode','+ Add','Back','Create'))

    def test_company_020(self):
        '''Verify the warning msg if missing the mandatory values for new contact in the 3rd page of add company'''
        self.driver.refresh()
        self.go_company()
        self.assertEqual(self.add_p3_required,('Please enter the Street.','Please select a State.','Please select a Suburb.','Please enter the Postcode.'))

    def test_company_021(self):
        '''Verify the Back function in the 3rd page of add company'''
        self.driver.refresh()
        self.go_company()
        self.assertEqual(self.add_p3_back,('Skip'))

    def test_company_022(self):
        '''Verify if it has search box in Company Page'''
        self.driver.refresh()
        self.go_company()
        self.assertEqual(self.check_searchbox,True)

    def test_company_023(self):
        '''Verify if it has From date filter in Company Page'''
        self.driver.refresh()
        self.go_company()
        self.assertEqual(self.check_fromdatebox,True)

    def test_company_024(self):
        '''Verify if it has To date filter in Company Page'''
        self.driver.refresh()
        self.go_company()
        self.assertEqual(self.check_todatebox,True)

    def test_company_025(self):
        '''Verify each column of the company list table for Lead'''
        self.driver.refresh()
        self.go_company()
        self.assertEqual(self.check_column_lead,('COMPANY NAME','INDUSTRY','STAGE','COUNTRY','LAST CONTACTED','STATUS','ACTIONS'))

if __name__ == '__main__':
    unittest.main(verbosity=2)
# Author:Yi Sun(Tim) 2023-04-3

'''CRM Page'''

from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
from UIModule.login_admin import *


class CRM_Page(Admin_Portal):
    '''loc for default values in this page'''
    crm_title_loc = (By.ID,'messages_billing_address')
    menu_loc = (By.CLASS_NAME,'button')
    CRM_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[1]/div/div[2]/div[3]/a/div/span[1]/img')
    dashboard_loc = (By.CSS_SELECTOR,'button.sc-drKuOJ:nth-child(1)')
    company_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[1]/button[2]')
    contact_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[1]/button[3]')
    task_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[1]/button[4]')

    def go_crm(self):
        '''go to crm page'''
        sleep(5)
        self.driver.find_element(*self.menu_loc).click()
        self.driver.find_element(*self.CRM_loc).click()

    @property
    def check_title(self):
        '''check the title for CRM page'''
        crm_title = self.driver.find_element(*self.crm_title_loc).text
        # print(crm_title)
        return crm_title

    @property
    def check_defaultvalue(self):
        '''check the default values in CRM page'''
        dashboard = self.driver.find_element(*self.dashboard_loc).text
        company = self.driver.find_element(*self.company_loc).text
        contact = self.driver.find_element(*self.contact_loc).text
        task = self.driver.find_element(*self.task_loc).text
        # print(dashboard, company, contact, task)
        return dashboard, company, contact, task

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://portal.staging.abcd.com/")
    driver.implicitly_wait(10)

    login = CRM_Page(driver)
    login.typeUserName('yi_Sun')
    login.typePassword('abcd')
    # login.typeUserName('timnew')
    # login.typePassword('Tims1')
    login.clickLogin
    login.go_crm()
    # login.check_title
    login.check_defaultvalue







# Author:Yi Sun(Tim) 2023-05-22

'''OSM Page'''

import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from UIModule.login_admin import *

class OSM_Page(Admin_Portal):
    '''loc for default values in this page'''
    osmtitle_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[1]/div[1]/div[1]')
    osmdashboard_loc = (By.ID,'messages_billing_address')
    procurement_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[1]/button[2]')
    inventory_loc = (By.CSS_SELECTOR,'button.sc-drKuOJ:nth-child(5)')
    quality_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[1]/button[4]')

    def go_osm(self):
        sleep(5)
        self.driver.find_element(*self.menu_loc).click()
        self.driver.find_element(*self.OSM_loc).click()

    @property
    def check_title(self):
        '''check the title for OSM page'''
        osm_title = self.driver.find_element(*self.osmtitle_loc).text
        return osm_title

    @property
    def check_url(self):
        '''check the url for OSM page'''
        osm_url = self.driver.current_url
        return osm_url

    @property
    def check_defaultvalue(self):
        '''check the default values in OSM page'''
        dashboard = self.driver.find_element(*self.osmdashboard_loc).text
        procurement = self.driver.find_element(*self.procurement_loc).text
        inventory = self.driver.find_element(*self.inventory_loc).text
        quality = self.driver.find_element(*self.quality_loc).text
        return dashboard,procurement,inventory,quality

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://portal.staging.abcd.com/")
    driver.implicitly_wait(10)

    login = OSM_Page(driver)
    login.typeUserName('yi_sun')
    login.typePassword('abcd')
    login.clickLogin
    login.go_osm()
    login.check_url()
    login.check_title
    login.check_defaultvalue








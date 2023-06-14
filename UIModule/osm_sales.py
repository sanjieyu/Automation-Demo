# Author:Yi Sun(Tim) 2023-05-22

'''OSM Sales Page'''

from time import sleep
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from UIModule.osm_page import *
from selenium.webdriver.support import expected_conditions as EC

class Sales_Page(OSM_Page):
    '''loc for default section in Production page'''
    open_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[1]/div/button[1]')
    closed_loc = (By.CSS_SELECTOR,'button.sc-drKuOJ:nth-child(3)')
    cancelled_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[1]/div/button[3]')
    pwo_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[1]/div/button[4]')

    '''loc for default values in open section'''
    searchopen_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div[1]/div[1]/div/div[1]/div/div/input')
    fromopen_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div[1]/input')
    toopen_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div[3]/input')
    editcolumnboxopen_loc = (By.XPATH,'//*[@id="rc_select_13"]')
    neworderbutton_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div[1]/div[2]/button')
    creatpwobutton_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div[2]/button')

    '''loc for each table title in open section'''
    orderno_open_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[3]/div/div/div/div/div/div[1]/table/thead/tr/th[2]/span/div/span[1]')
    status_open_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[3]/div/div/div/div/div/div[1]/table/thead/tr/th[3]/div/span[1]')
    customer_open_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[3]/div/div/div/div/div/div[1]/table/thead/tr/th[4]/div/span[1]')
    purpose_open_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[3]/div/div/div/div/div/div[1]/table/thead/tr/th[5]')
    payment_open_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[3]/div/div/div/div/div/div[1]/table/thead/tr/th[6]')
    packing_open_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[3]/div/div/div/div/div/div[1]/table/thead/tr/th[7]/div/span[1]')
    products_open_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[3]/div/div/div/div/div/div[1]/table/thead/tr/th[8]')
    expectdelivery_open_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[3]/div/div/div/div/div/div[1]/table/thead/tr/th[9]/div/span[1]')

    '''loc for default values in closed section'''
    searchclosed_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div[1]/div/div[1]/div/div/input')
    fromclosed_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/input')
    toclosed_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div/div[3]/input')
    editcolumnboxclosed_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div/div/div')
    neworderbuttonclosed_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/button')

    '''loc for each table title in closed section'''
    orderno_closed_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[3]/div/div/div/div/div/div[1]/table/thead/tr/th[1]/div/span[1]')
    status_closed_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[3]/div/div/div/div/div/div[1]/table/thead/tr/th[2]/div/span[1]')
    customer_closed_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[3]/div/div/div/div/div/div[1]/table/thead/tr/th[3]/div/span[1]')
    purpose_closed_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[3]/div/div/div/div/div/div[1]/table/thead/tr/th[4]')
    payment_closed_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[3]/div/div/div/div/div/div[1]/table/thead/tr/th[5]')
    packing_closed_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[3]/div/div/div/div/div/div[1]/table/thead/tr/th[6]/div/span[1]')
    products_closed_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[3]/div/div/div/div/div/div[1]/table/thead/tr/th[7]')
    delivery_closed_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[3]/div/div/div/div/div/div[1]/table/thead/tr/th[8]/div/span[1]')

    '''loc for default values in cancelled section'''
    searchcancel_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div[1]/div/div[1]/div/div/input')
    fromcancel_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div/div[1]/input')
    tocancel_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div/div/div[3]/input')
    editcolumncancel_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div/label')
    editcolumnboxcancel_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div/div/div')
    neworderbuttoncancel_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/button')

    '''loc for default values in pwo section'''
    searchpwo_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div/input')
    frompwo_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[1]/input')
    topwo_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[3]/input')

    def go_production(self):
        '''go to Production page'''
        sleep(5)
        self.driver.find_element(*self.menu_loc).click()
        self.driver.find_element(*self.OSM_loc).click()
        self.driver.find_element(*self.production_loc).click()

    @property
    def check_salessection(self):
        '''check the default section in sales page'''
        open_sales = self.driver.find_element(*self.open_loc).text
        closed_sales = self.driver.find_element(*self.closed_loc).text
        cancelled_sales = self.driver.find_element(*self.cancelled_loc).text
        pwo_sales = self.driver.find_element(*self.pwo_loc).text
        return open_sales,closed_sales,cancelled_sales,pwo_sales

    @property
    def check_opendefault(self):
        '''check the default values in open section'''
        neworderbutton = self.driver.find_element(*self.neworderbutton_loc).text
        createpwobutton = self.driver.find_element(*self.creatpwobutton_loc).text
        return neworderbutton,createpwobutton

    @property
    def check_opensearchbox(self):
        '''Check if it has search box in open section'''
        opensearchbox_des = self.driver.find_element(*self.searchopen_loc)
        if opensearchbox_des.is_displayed():
            return True
        else:
            return False

    @property
    def check_fromopen(self):
        '''Check if it has From date filter in open section'''
        fromopen_des = self.driver.find_element(*self.fromopen_loc)
        if fromopen_des.is_displayed():
            return True
        else:
            return False

    @property
    def check_toopen(self):
        '''Check if it has To date filter in open section'''
        toopen_des = self.driver.find_element(*self.toopen_loc)
        if toopen_des.is_displayed():
            return True
        else:
            return False

    @property
    def check_opentable(self):
        '''Check the columns in Open section of Sales page'''
        orderno_open = self.driver.find_element(*self.orderno_open_loc).text
        status_open = self.driver.find_element(*self.status_open_loc).text
        customer_open = self.driver.find_element(*self.customer_open_loc).text
        purpose_open = self.driver.find_element(*self.purpose_open_loc).text
        payment_open = self.driver.find_element(*self.payment_open_loc).text
        packing_open = self.driver.find_element(*self.packing_open_loc).text
        products_open = self.driver.find_element(*self.products_open_loc).text
        expectdelivery_open = self.driver.find_element(*self.expectdelivery_open_loc).text
        return orderno_open,status_open,customer_open,purpose_open,payment_open,packing_open,products_open,expectdelivery_open

    @property
    def go_closed(self):
        '''switch to closed section'''
        self.driver.implicitly_wait(5)
        closed_section = self.driver.find_element(*self.closed_loc)
        self.driver.execute_script("arguments[0].click();",closed_section)
        closed_section.send_keys(Keys.ENTER)

    @property
    def check_closeddefault(self):
        '''check the default values in closed section'''
        neworderbuttonclosed = self.driver.find_element(*self.neworderbuttonclosed_loc).text
        return neworderbuttonclosed

    @property
    def check_closedsearchbox(self):
        '''Check if it has search box in closed section'''
        closedsearchbox_des = self.driver.find_element(*self.searchclosed_loc)
        if closedsearchbox_des.is_displayed():
            return True
        else:
            return False

    @property
    def check_fromclosed(self):
        '''Check if it has From date filter in closed section'''
        fromclosed_des = self.driver.find_element(*self.fromclosed_loc)
        if fromclosed_des.is_displayed():
            return True
        else:
            return False

    @property
    def check_toclosed(self):
        '''Check if it has To date filter in closed section'''
        toclosed_des = self.driver.find_element(*self.toclosed_loc)
        if toclosed_des.is_displayed():
            return True
        else:
            return False

    @property
    def check_closedtable(self):
        '''Check the columns in Closed section of Sales page'''
        orderno_closed = self.driver.find_element(*self.orderno_closed_loc).text
        status_closed = self.driver.find_element(*self.status_closed_loc).text
        customer_closed = self.driver.find_element(*self.customer_closed_loc).text
        purpose_closed = self.driver.find_element(*self.purpose_closed_loc).text
        payment_closed = self.driver.find_element(*self.payment_closed_loc).text
        packing_closed = self.driver.find_element(*self.packing_closed_loc).text
        products_closed = self.driver.find_element(*self.products_closed_loc).text
        delivery_closed = self.driver.find_element(*self.delivery_closed_loc).text
        return orderno_closed,status_closed,customer_closed,purpose_closed,payment_closed,packing_closed,products_closed,delivery_closed

    @property
    def go_cancelled(self):
        '''switch to cancelled section'''
        self.driver.implicitly_wait(10)
        self.driver.find_element(*self.cancelled_loc).click()


    @property
    def check_canceldefault(self):
        '''check the default values in cancelled section'''
        neworderbuttoncancel = self.driver.find_element(*self.neworderbuttoncancel_loc).text
        return neworderbuttoncancel

    @property
    def check_cancelsearchbox(self):
        '''Check if it has search box in cancelled section'''
        cancelsearchbox_des = self.driver.find_element(*self.searchcancel_loc)
        if cancelsearchbox_des.is_displayed():
            return True
        else:
            return False

    @property
    def check_fromcancel(self):
        '''Check if it has From date filter in cancelled section'''
        fromcancel_des = self.driver.find_element(*self.fromcancel_loc)
        if fromcancel_des.is_displayed():
            return True
        else:
            return False

    @property
    def check_tocancel(self):
        '''Check if it has To date filter in cancelled section'''
        tocancel_des = self.driver.find_element(*self.tocancel_loc)
        if tocancel_des.is_displayed():
            return True
        else:
            return False

    @property
    def go_pwo(self):
        '''switch to pwo section'''
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.pwo_loc).click()

    @property
    def check_pwosearchbox(self):
        '''Check if it has search box in pwo section'''
        pwosearchbox_des = self.driver.find_element(*self.searchpwo_loc)
        if pwosearchbox_des.is_displayed():
            return True
        else:
            return False

    @property
    def check_frompwo(self):
        '''Check if it has From date filter in pwo section'''
        frompwo_des = self.driver.find_element(*self.frompwo_loc)
        if frompwo_des.is_displayed():
            return True
        else:
            return False

    @property
    def check_topwo(self):
        '''Check if it has To date filter in pwo section'''
        topwo_des = self.driver.find_element(*self.topwo_loc)
        if topwo_des.is_displayed():
            return True
        else:
            return False

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://portal.staging.abcd.com/")
    driver.implicitly_wait(5)
    login = Sales_Page(driver)
    login.typeUserName('yi_sun')
    login.typePassword('abcd')
    login.clickLogin
    login.go_production()
    login.check_salessection
    login.check_opendefault
    login.check_opensearchbox
    login.check_fromopen
    login.check_toopen
    login.check_opentable
    login.go_closed
    login.check_closeddefault
    login.check_closedsearchbox
    login.check_fromclosed
    login.check_toclosed
    login.check_closedtable
    login.go_cancelled
    login.check_canceldefault
    login.check_cancelsearchbox
    login.check_fromcancel
    login.check_tocancel



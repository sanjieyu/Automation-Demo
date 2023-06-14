# Author:Yi Sun(Tim) 2023-04-3

'''CRM Company Page'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from UIModule.crm_page import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class Company_page(CRM_Page):
    '''loc for default values in company page'''
    all_loc = (By.ID,'messages_all_address21')
    lead_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div[1]/div/span[2]')
    searchbox_loc = (By.CSS_SELECTOR,'button.sc-drKuOJ:nth-child(1)')
    from_loc = (By.CLASS_NAME,'/input')
    to_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div/div[3]/div/div/div/div[3]/input')
    editcolumnbox_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div/div/div')
    addcompanybutton_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div/button')

    '''loc for the columnu sections'''
    relationshop_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/table/thead/tr/th[1]/div/span[1]')
    name_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/table/thead/tr/th[2]/div/span[1]')
    industry_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/table/thead/tr/th[3]/div/span[1]')
    email_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/table/thead/tr/th[4]')
    phone_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/table/thead/tr/th[5]')
    create_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/table/thead/tr/th[6]/div/span[1]')
    status_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/table/thead/tr/th[7]/div/span[1]')
    action_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/table/thead/tr/th[8]')
    '''loc for the columnu sections for Lead'''
    companynamel_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[1]/div/span[1]')
    industryl_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[2]/div/span[1]')
    stage_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[3]/div/span[1]')
    countryl_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[4]/div/span[1]')
    lastcontact_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[5]/div/span[1]')
    statusl_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[6]/div/span[1]')
    actionl_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div/table/thead/tr/th[7]')

    '''loc for the sort order for each column'''
    relationship_sort_loc = (By.CLASS_NAME,'anticon anticon-filter')
    sortby_customer_loc = (By.XPATH,'/html/body/div[3]/div/div/div/ul/li[1]')
    sortby_supplier_loc = (By.XPATH,'/html/body/div[3]/div/div/div/ul/li[2]')
    sortby_lead_loc = (By.XPATH,'/html/body/div[3]/div/div/div/ul/li[3]')
    sortby_unassigned_loc = (By.XPATH,'/html/body/div[3]/div/div/div/ul/li[4]')
    company_tablelist_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[2]')
    status_sort_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div[1]/table/thead/tr/th[7]/div/span[2]')
    sortby_active_loc = (By.CLASS_NAME,'ant-dropdown-menu-title-content')
    sortby_inactive_loc = (By.CLASS_NAME,'ant-dropdown-menu-title-content')

    '''loc for 3 sections of Add Company window'''
    addcompanytitle_loc = (By.CLASS_NAME,'ant-modal-title')
    businessinfo_loc = (By.CSS_SELECTOR,'div.ant-steps-item:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1)')
    primarycontact_loc = (By.CSS_SELECTOR,'div.ant-steps-item:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1)')
    address_loc = (By.CSS_SELECTOR,'div.ant-steps-item:nth-child(3) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1)')

    nextp1_loc = (By.ID,'modal-btn-width-regular')
    '''loc for 1st page of Add Company window'''
    typedropdown_loc = (By.XPATH,'/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[1]/div/div/div/div/div[2]/div/div')
    typeselect_loc = (By.ID, 'business-info_businessType_list')
    typeselect1_loc = (By.ID,'business-info_businessType_list')
    typeunassign_loc = (By.XPATH,'/html/body/div[3]/div/div/div/div[2]/div[1]/div/div/div[1]')
    typelead_loc = (By.XPATH,'/html/body/div[3]/div/div/div/div[2]/div[1]/div/div/div[2]/div')
    typecustomer_loc = (By.XPATH,'/html/body/div[3]/div/div/div/div[2]/div[1]/div/div/div[3]')
    typesupplier_loc = (By.XPATH,'/html/body/div[3]/div/div/div/div[2]/div[1]/div/div/div[4]')
    requiremsg_loc = (By.CSS_SELECTOR,'.sc-bMVAic')
    busniesstype_loc = (By.CSS_SELECTOR,'#business-info > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)')
    companyname_loc = (By.CSS_SELECTOR,'div.ant-row:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)')
    country_loc = (By.CSS_SELECTOR,'div.ant-row:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)')
    abn_loc = (By.CSS_SELECTOR,'div.ant-row:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)')
    busniessemail_loc = (By.CSS_SELECTOR,'div.ant-row:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)')
    busniessphone_loc = (By.CSS_SELECTOR,'div.ant-row:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)')
    industryedit_loc = (By.CSS_SELECTOR,'div.ant-row:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)')
    url_loc = (By.CSS_SELECTOR,'div.ant-row:nth-child(5) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)')
    statusedit_loc = (By.CSS_SELECTOR,'div.ant-row:nth-child(6) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)')
    comments_loc = (By.CSS_SELECTOR,'div.ant-row:nth-child(7) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)')
    companyname_required_loc = (By.CSS_SELECTOR,'div.ant-row:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)')
    industry_required_loc = (By.CSS_SELECTOR,'div.ant-row:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)')
    nameeditbox_loc = (By.ID,'business-info_bus_name')
    industryeditbox_loc = (By.ID,'business-info_industry')
    emaileditbox_loc = (By.ID,'business-info_bus_email')
    '''loc for 2nd page of Add Company window'''
    businessinfo2_loc = (By.CSS_SELECTOR,'div.ant-steps-item:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1)')
    primarycontact2_loc = (By.CSS_SELECTOR,'div.ant-steps-item:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1)')
    address2_loc = (By.CSS_SELECTOR,'div.ant-steps-item:nth-child(3) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1)')
    requiremsg2_loc = (By.CSS_SELECTOR,'.sc-bMVAic')
    exist_loc = (By.CSS_SELECTOR,'label.ant-radio-wrapper:nth-child(1) > span:nth-child(2)')
    new_loc = (By.CSS_SELECTOR,'label.ant-radio-wrapper:nth-child(2) > span:nth-child(2)')
    newradiobutton_loc = (By.CSS_SELECTOR,'label.ant-radio-wrapper:nth-child(2)')
    contact2_loc = (By.CSS_SELECTOR, '.sc-gPzReC')
    title_loc = (By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[1]/div/div/div/div/div/div[1]')
    firstname_loc = (By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[2]/div/div/div/div/div/div')
    lastname_loc = (By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[3]/div/div/div/div/div/div')
    jobtitle_loc = (By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[2]/div/div/div/div/div')
    email2_loc = (By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[3]/div/div/div/div/div')
    mobileno_loc = (By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[4]/div/div/div/div/div[1]')
    skipexist_loc = (By.CLASS_NAME,'ant-checkbox-wrapper')
    skipnew_loc = (By.CLASS_NAME,'ant-checkbox-wrapper')
    firstnamerequired_loc = (By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[2]/div/div/div[2]/div')
    lastnamerequired_loc = (By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[1]/div[3]/div/div/div[2]/div')
    jobtitlerequired_loc = (By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[2]/div/div[2]/div')
    emailrequired_loc = (By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[3]/div/div[2]/div')
    mobilenorequired_loc = (By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[4]/div/div[2]/div')
    contactrequired_loc = (By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[1]/div/div[2]/div')
    nextp2_loc = (By.CSS_SELECTOR,'.sc-hMqMXs > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(2)')
    backp2_loc = (By.CSS_SELECTOR,'button.ant-btn:nth-child(1)')
    skipcheckbox_loc = (By.CLASS_NAME,'ant-checkbox-wrapper')
    '''loc for 3rd page of Add Company window'''
    businessinfo3_loc = (By.CSS_SELECTOR,'div.ant-steps-item:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1)')
    primarycontact3_loc = (By.CSS_SELECTOR,'div.ant-steps-item:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1)')
    address3_loc = (By.CSS_SELECTOR,'div.ant-steps-item:nth-child(3) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1)')
    requiredmsg3_loc = (By.CSS_SELECTOR,'.sc-bMVAic')
    deliveryaddress_loc = (By.CSS_SELECTOR,'#address > div:nth-child(1)')
    unit_loc = (By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[2]/div[1]/div/div/div/div/div/div')
    street_loc = (By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[2]/div[2]/div/div/div/div/div/div')
    country3_loc = (By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[2]/div[3]/div/div/div/div/div/div[1]')
    state_loc =(By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[3]/div[1]/div/div/div/div/div/div[1]')
    suburb_loc = (By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[3]/div[2]/div/div/div/div/div/div[1]')
    postcode_loc = (By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[3]/div[3]/div/div/div/div/div/div')
    billing_loc = (By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[4]')
    same_loc = (By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[5]/label/span[2]/span')
    billingunit_loc = (By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[6]/div[1]/div/div/div/div/div/div')
    billingstreet_loc = (By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[6]/div[2]/div/div/div/div/div/div')
    billingcountry_loc = (By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[6]/div[3]/div/div/div/div/div/div[1]')
    billingstate_loc = (By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[7]/div[1]/div/div/div/div/div/div[1]')
    billingsuburb_loc = (By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[7]/div[2]/div/div/div/div/div/div[1]')
    billingpostcode_loc = (By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[7]/div[3]/div/div/div/div/div/div')
    addbutton_loc = (By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[8]/button')
    backp3_loc = (By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[3]/div/div/div/div/div/button[1]')
    create3_loc = (By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[3]/div/div/div/div/div/button[2]')
    streetrequired3_loc = (By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[2]/div[2]/div/div/div[2]/div')
    staterequired3_loc = (By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[3]/div[1]/div/div/div[2]/div')
    suburbrequired3_loc = (By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[3]/div[2]/div/div/div[2]/div')
    postcoderequired3_loc = (By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[3]/div[3]/div/div/div[2]/div')
    streetbox_loc = (By.ID,'address_street')
    statebox_loc = (By.ID,'address_state')
    suburbbox_loc = (By.CSS_SELECTOR,'#address_suburb')
    postcodebox_loc = (By.ID,'address_postcode')
    samecheckbox_loc = (By.XPATH,'/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[5]/label/span[1]/input')


    def go_company(self):
        '''go to company page'''
        self.driver.find_element(*self.company_loc).click()

    @property
    def check_description(self):
        '''Check the description for each element'''
        all_des = self.driver.find_element(*self.all_loc).text
        lead_des = self.driver.find_element(*self.lead_loc).text
        addcompanybutton_des = self.driver.find_element(*self.addcompanybutton_loc).text
        return all_des,lead_des,addcompanybutton_des

    @property
    def check_searchbox(self):
        '''Check if it has search box'''
        searchbox_des = self.driver.find_element(*self.searchbox_loc)
        if searchbox_des.is_displayed():
            return True
        else:
            return False

    @property
    def check_fromdatebox(self):
        '''Check if it has From date filter'''
        fromdate_des = self.driver.find_element(*self.from_loc)
        if fromdate_des.is_displayed():
            return True
        else:
            return False

    @property
    def check_todatebox(self):
        '''Check if it has To date filter'''
        todate_des = self.driver.find_element(*self.to_loc)
        if todate_des.is_displayed():
            return True
        else:
            return False


    @property
    def check_column(self):
        '''Check each column of the company list table'''
        check_relationshop = self.driver.find_element(*self.relationshop_loc).text
        check_name = self.driver.find_element(*self.name_loc).text
        check_industry = self.driver.find_element(*self.industry_loc).text
        check_email = self.driver.find_element(*self.email_loc).text
        check_phone = self.driver.find_element(*self.phone_loc).text
        check_create = self.driver.find_element(*self.create_loc).text
        check_status = self.driver.find_element(*self.status_loc).text
        check_action = self.driver.find_element(*self.action_loc).text
        return check_relationshop,check_name,check_industry,check_email,check_phone,check_create,check_status,check_action

    @property
    def check_column_lead(self):
        '''Check each column of the company list table for Lead'''
        self.driver.find_element(*self.lead_loc).click()
        check_companynamel = self.driver.find_element(*self.companynamel_loc).text
        check_industryl = self.driver.find_element(*self.industryl_loc).text
        check_stage = self.driver.find_element(*self.stage_loc).text
        check_countryl = self.driver.find_element(*self.countryl_loc).text
        check_lastcontact = self.driver.find_element(*self.lastcontact_loc).text
        check_statusl = self.driver.find_element(*self.statusl_loc).text
        check_actionl = self.driver.find_element(*self.actionl_loc).text
        return check_companynamel,check_industryl,check_stage,check_countryl,check_lastcontact,check_statusl,check_actionl


    @property
    def sort_relationship(self):
        '''Check the sort function of relationship column'''
        time.sleep(1)
        self.driver.find_element(*self.relationship_sort_loc).click()
        wait = WebDriverWait(self.driver,5)
        filter_window = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'ant-table-filter-dropdown')))
        sortrelationship_menu = filter_window.find_element(*self.sortby_customer_loc).text
        sortsupplier_menu = filter_window.find_element(*self.sortby_supplier_loc).text
        sortlead_menu = filter_window.find_element(*self.sortby_lead_loc).text
        sortunassigned_menu = filter_window.find_element(*self.sortby_unassigned_loc).text
        return sortrelationship_menu,sortsupplier_menu,sortlead_menu,sortunassigned_menu

    @property
    def check_companyurl(self):
        '''Check the url of company page'''
        company_url = self.driver.current_url
        return company_url

    @property
    def sort_status(self):
        '''Check the sort function of status column'''
        company_tablelist = self.driver.find_element(*self.company_tablelist_loc)
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",company_tablelist)    #滚动条拉到最下面
        self.driver.execute_script("arguments[0].scrollLeft = arguments[0].scrollWidth",company_tablelist)   #滚动条拉到最右边
        self.driver.find_element(*self.status_sort_loc).click()
        wait = WebDriverWait(self.driver,10)
        filterstatus_window = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'ant-table-filter-dropdown')))
        sortactive_menu = filterstatus_window.find_element(*self.sortby_active_loc).text
        return sortactive_menu

    @property
    def add_companyptitle(self):
        '''Check the title of add company page'''
        self.driver.find_element(*self.addcompanybutton_loc).click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        addcompany_title = self.driver.find_element(*self.addcompanytitle_loc).text
        return addcompany_title

    @property
    def add_companyp1section(self):
        '''Check the three section in the first page of add company'''
        self.driver.find_element(*self.addcompanybutton_loc).click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        addcompany_info = self.driver.find_element(*self.businessinfo_loc).text
        addcompany_primary = self.driver.find_element(*self.primarycontact_loc).text
        addcompany_address = self.driver.find_element(*self.address_loc).text
        return addcompany_info,addcompany_primary,addcompany_address

    @property
    def add_companyp1(self):
        '''Check the default elements in the first page of add company'''
        self.driver.find_element(*self.addcompanybutton_loc).click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        requiremsg = self.driver.find_element(*self.requiremsg_loc).text
        busniesstype = self.driver.find_element(*self.busniesstype_loc).text
        companyname = self.driver.find_element(*self.companyname_loc).text
        country = self.driver.find_element(*self.country_loc).text
        abn = self.driver.find_element(*self.abn_loc).text
        busniessmail = self.driver.find_element(*self.busniessemail_loc).text
        busniessphone = self.driver.find_element(*self.busniessphone_loc).text
        industryedit = self.driver.find_element(*self.industryedit_loc).text
        url = self.driver.find_element(*self.url_loc).text
        statusedit = self.driver.find_element(*self.statusedit_loc).text
        comments = self.driver.find_element(*self.comments_loc).text
        return requiremsg,busniesstype,companyname,country,abn,busniessmail,busniessphone,industryedit,url,statusedit,comments

    @property
    def add_p1_required(self):
        '''Check the warning msg if doesn't input company name and industry in the first page of add company'''
        self.driver.find_element(*self.addcompanybutton_loc).click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element(*self.nextp1_loc).click()
        namerequired = self.driver.find_element(*self.companyname_required_loc).text
        industryrequired = self.driver.find_element(*self.industry_required_loc).text
        return namerequired,industryrequired

    @property
    def add_companyp2section(self):
        '''Check the three section in the 2nd page of add company'''
        self.driver.find_element(*self.addcompanybutton_loc).click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element(*self.nameeditbox_loc).send_keys('automationtest')
        self.driver.find_element(*self.industryeditbox_loc).send_keys('Software')
        self.driver.find_element(*self.emaileditbox_loc).send_keys('test@abcd.com')
        self.driver.find_element(*self.nextp1_loc).click()
        addcompany_info2 = self.driver.find_element(*self.businessinfo2_loc).text
        addcompany_primary2 = self.driver.find_element(*self.primarycontact2_loc).text
        addcompany_address2 = self.driver.find_element(*self.address2_loc).text
        return addcompany_info2,addcompany_primary2,addcompany_address2

    @property
    def add_companyp2_exsit(self):
        '''Check the default elements for exist contact in the 2nd page of add company'''
        self.driver.find_element(*self.addcompanybutton_loc).click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element(*self.nameeditbox_loc).send_keys('automationtest')
        self.driver.find_element(*self.industryeditbox_loc).send_keys('Software')
        self.driver.find_element(*self.emaileditbox_loc).send_keys('test@abcd.com')
        self.driver.find_element(*self.nextp1_loc).click()
        requiremsg2 = self.driver.find_element(*self.requiremsg2_loc).text
        exist2 = self.driver.find_element(*self.exist_loc).text
        new2 = self.driver.find_element(*self.new_loc).text
        contact2 = self.driver.find_element(*self.contact2_loc).text
        skipexist = self.driver.find_element(*self.skipexist_loc).text
        return requiremsg2,exist2,new2,contact2,skipexist

    @property
    def add_companyp2_new(self):
        '''Check the default elements for new contact in the 2nd page of add company'''
        self.driver.find_element(*self.addcompanybutton_loc).click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element(*self.nameeditbox_loc).send_keys('automationtest')
        self.driver.find_element(*self.industryeditbox_loc).send_keys('Software')
        self.driver.find_element(*self.emaileditbox_loc).send_keys('test@abcd.com')
        self.driver.find_element(*self.nextp1_loc).click()
        self.driver.find_element(*self.newradiobutton_loc).click()
        title2 = self.driver.find_element(*self.title_loc).text
        firstname = self.driver.find_element(*self.firstname_loc).text
        lastname = self.driver.find_element(*self.lastname_loc).text
        jobtitle = self.driver.find_element(*self.jobtitle_loc).text
        email2 = self.driver.find_element(*self.email2_loc).text
        mobileno = self.driver.find_element(*self.mobileno_loc).text
        skipnew = self.driver.find_element(*self.skipnew_loc).text
        return title2,firstname,lastname,jobtitle,email2,mobileno,skipnew

    @property
    def add_p2_newrequired(self):
        '''Check the warning msg if missing the mandatory values for new contact in the 2nd page of add company'''
        self.driver.find_element(*self.addcompanybutton_loc).click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element(*self.nameeditbox_loc).send_keys('automationtest')
        self.driver.find_element(*self.industryeditbox_loc).send_keys('Software')
        self.driver.find_element(*self.emaileditbox_loc).send_keys('test@abcd.com')
        self.driver.find_element(*self.nextp1_loc).click()
        self.driver.find_element(*self.newradiobutton_loc).click()
        self.driver.find_element(*self.nextp2_loc).click()
        firstnamerequired = self.driver.find_element(*self.firstnamerequired_loc).text
        lastnamerequired = self.driver.find_element(*self.lastnamerequired_loc).text
        jobtitlerequired = self.driver.find_element(*self.jobtitlerequired_loc).text
        emailrequired = self.driver.find_element(*self.emailrequired_loc).text
        mobilenorequired = self.driver.find_element(*self.mobilenorequired_loc).text
        return firstnamerequired,lastnamerequired,jobtitlerequired,emailrequired,mobilenorequired

    @property
    def add_p2_existrequired(self):
        '''Check the warning msg if missing the mandatory values for exist contact in the 2nd page of add company'''
        self.driver.find_element(*self.addcompanybutton_loc).click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element(*self.nameeditbox_loc).send_keys('automationtest')
        self.driver.find_element(*self.industryeditbox_loc).send_keys('Software')
        self.driver.find_element(*self.emaileditbox_loc).send_keys('test@abcd.com')
        self.driver.find_element(*self.nextp1_loc).click()
        self.driver.find_element(*self.nextp2_loc).click()
        contactrequired = self.driver.find_element(*self.contactrequired_loc).text
        return contactrequired

    @property
    def add_p2_back(self):
        '''Check the Back function in the 2nd page of add company'''
        self.driver.find_element(*self.addcompanybutton_loc).click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element(*self.nameeditbox_loc).send_keys('automationtest')
        self.driver.find_element(*self.industryeditbox_loc).send_keys('Software')
        self.driver.find_element(*self.emaileditbox_loc).send_keys('test@abcd.com')
        self.driver.find_element(*self.nextp1_loc).click()
        time.sleep(1)
        self.driver.find_element(*self.backp2_loc).click()
        companyname = self.driver.find_element(*self.companyname_loc).text
        return companyname

    @property
    def add_p2_skip(self):
        '''Check the Skip function in the 2nd page of add company'''
        self.driver.find_element(*self.addcompanybutton_loc).click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element(*self.nameeditbox_loc).send_keys('automationtest')
        self.driver.find_element(*self.industryeditbox_loc).send_keys('Software')
        self.driver.find_element(*self.emaileditbox_loc).send_keys('test@abcd.com')
        self.driver.find_element(*self.nextp1_loc).click()
        self.driver.find_element(*self.skipcheckbox_loc).click()
        self.driver.find_element(*self.nextp2_loc).click()
        deliveryaddress = self.driver.find_element(*self.deliveryaddress_loc).text
        return deliveryaddress

    @property
    def add_companyp3section(self):
        '''Check the three section in the 3rd page of add company'''
        self.driver.find_element(*self.addcompanybutton_loc).click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element(*self.nameeditbox_loc).send_keys('automationtest')
        self.driver.find_element(*self.industryeditbox_loc).send_keys('Software')
        self.driver.find_element(*self.emaileditbox_loc).send_keys('test@abcd.com')
        self.driver.find_element(*self.nextp1_loc).click()
        self.driver.find_element(*self.skipcheckbox_loc).click()
        self.driver.find_element(*self.nextp2_loc).click()
        addcompany_info3 = self.driver.find_element(*self.businessinfo3_loc).text
        addcompany_primary3 = self.driver.find_element(*self.primarycontact3_loc).text
        addcompany_address3 = self.driver.find_element(*self.address3_loc).text
        return addcompany_info3,addcompany_primary3,addcompany_address3

    @property
    def add_companyp3_delivery(self):
        '''Check the default elements for delivery in the 3rd page of add company'''
        self.driver.find_element(*self.addcompanybutton_loc).click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element(*self.nameeditbox_loc).send_keys('automationtest')
        self.driver.find_element(*self.industryeditbox_loc).send_keys('Software')
        self.driver.find_element(*self.emaileditbox_loc).send_keys('test@abcd.com')
        self.driver.find_element(*self.nextp1_loc).click()
        self.driver.find_element(*self.skipcheckbox_loc).click()
        self.driver.find_element(*self.nextp2_loc).click()
        requiredmsg3 = self.driver.find_element(*self.requiredmsg3_loc).text
        deliveryaddress = self.driver.find_element(*self.deliveryaddress_loc).text
        unit = self.driver.find_element(*self.unit_loc).text
        street = self.driver.find_element(*self.street_loc).text
        country3 = self.driver.find_element(*self.country3_loc).text
        state = self.driver.find_element(*self.state_loc).text
        subrub = self.driver.find_element(*self.suburb_loc).text
        postcode = self.driver.find_element(*self.postcode_loc).text
        return requiredmsg3,deliveryaddress,unit,street,country3,state,subrub,postcode

    @property
    def add_companyp3_billing(self):
        '''Check the default elements for billing in the 3rd page of add company'''
        self.driver.find_element(*self.addcompanybutton_loc).click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element(*self.nameeditbox_loc).send_keys('automationtest')
        self.driver.find_element(*self.industryeditbox_loc).send_keys('Software')
        self.driver.find_element(*self.emaileditbox_loc).send_keys('test@abcd.com')
        self.driver.find_element(*self.nextp1_loc).click()
        self.driver.find_element(*self.skipcheckbox_loc).click()
        self.driver.find_element(*self.nextp2_loc).click()
        billing = self.driver.find_element(*self.billing_loc).text
        samebox = self.driver.find_element(*self.same_loc).text
        billingunit = self.driver.find_element(*self.billingunit_loc).text
        billingstreet = self.driver.find_element(*self.billingstreet_loc).text
        billingcountry = self.driver.find_element(*self.billingcountry_loc).text
        billingstate = self.driver.find_element(*self.billingstate_loc).text
        billingsuburb = self.driver.find_element(*self.billingsuburb_loc).text
        billingpostcode = self.driver.find_element(*self.billingpostcode_loc).text
        addbutton = self.driver.find_element(*self.addbutton_loc).text
        backp3 = self.driver.find_element(*self.backp3_loc).text
        create3 = self.driver.find_element(*self.create3_loc).text
        return billing,samebox,billingunit,billingstreet,billingcountry,billingstate,billingsuburb,billingpostcode,addbutton,backp3,create3

    @property
    def add_p3_required(self):
        '''Check the warning msg if missing the mandatory values for new contact in the 3rd page of add company'''
        self.driver.find_element(*self.addcompanybutton_loc).click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element(*self.nameeditbox_loc).send_keys('automationtest')
        self.driver.find_element(*self.industryeditbox_loc).send_keys('Software')
        self.driver.find_element(*self.emaileditbox_loc).send_keys('test@abcd.com')
        self.driver.find_element(*self.nextp1_loc).click()
        self.driver.find_element(*self.skipcheckbox_loc).click()
        self.driver.find_element(*self.nextp2_loc).click()
        self.driver.find_element(*self.create3_loc).click()
        streetrequird3 = self.driver.find_element(*self.streetrequired3_loc).text
        staterequird3 = self.driver.find_element(*self.staterequired3_loc).text
        suburbrequird3 = self.driver.find_element(*self.suburbrequired3_loc).text
        postcoderequird3 = self.driver.find_element(*self.postcoderequired3_loc).text
        return streetrequird3,staterequird3,suburbrequird3,postcoderequird3

    @property
    def add_p3_back(self):
        '''Check the Back function in the 3rd page of add company'''
        self.driver.find_element(*self.addcompanybutton_loc).click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element(*self.nameeditbox_loc).send_keys('automationtest')
        self.driver.find_element(*self.industryeditbox_loc).send_keys('Software')
        self.driver.find_element(*self.emaileditbox_loc).send_keys('test@abcd.com')
        self.driver.find_element(*self.nextp1_loc).click()
        self.driver.find_element(*self.skipcheckbox_loc).click()
        self.driver.find_element(*self.nextp2_loc).click()
        self.driver.find_element(*self.backp3_loc).click()
        skipp2 = self.driver.find_element(*self.skipexist_loc).text
        return skipp2


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://portal.staging.abcd.com/")
    driver.implicitly_wait(10)

    login = Company_page(driver)
    login.typeUserName('yi_sun')
    login.typePassword('abcd')
    login.clickLogin
    login.go_crm()
    login.go_company()
    login.check_description
    login.check_column_lead
    login.check_searchbox
    login.check_fromdatebox
    login.check_todatebox
    login.check_description
    login.check_column
    login.sort_relationship
    login.check_companyurl
    login.sort_status
    login.add_companyptitle
    login.add_companyp1
    login.add_companyp1section
    login.add_p1_required
    login.add_p1_busniesstype
    login.add_companyp2section
    login.add_companyp2_exsit
    login.add_companyp2_new
    login.add_p2_newrequired
    login.add_p2_existrequired
    login.add_p2_back
    login.add_p2_skip
    login.add_companyp3section
    login.add_companyp3_delivery
    login.add_companyp3_billing
    login.add_p3_required
    login.add_p3_back
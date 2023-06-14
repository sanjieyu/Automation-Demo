
# Author:Yi Sun(Tim) 2023-03-31

'''Login Page'''

from selenium.webdriver.common.by import By
from UIModule.basePage import *
from selenium import webdriver
from time import sleep

class Admin_Portal(WebDriver):
    '''input username, password'''
    username_loc = (By.ID,'nest-messages_billing_address')
    password_loc = (By.XPATH,'/html/body/div[1]/div/div/div[2]/input[2]')
    login_loc = (By.CLASS_NAME,'/button')
    loginError_loc = (By.CSS_SELECTOR,'button.sc-drKuOJ:nth-child(3)')
    '''forget password,submit username page'''
    forgetpwd_loc = (By.XPATH,'/html/body/div/div/div[2]/div[2]/div[1]/button')
    forgetsubmit_loc = (By.XPATH,'/html/body/div/div/div[2]/button')
    forgetdescription_loc = (By.XPATH,'/html/body/div/div/div[2]/div/p')
    wrongemailwaring_loc = (By.XPATH,'/html/body/div/div/div[2]/div[1]')
    inputemail_loc = (By.XPATH,'/html/body/div/div/div[2]/div/input')
    '''forget password,submit code page'''
    forgetusernamesubmit_loc = (By.XPATH,'/html/body/div/div/div[2]/div[2]/input[1]')
    forgetentercode_loc = (By.XPATH,'/html/body/div/div/div[2]/div[2]/input[2]')
    forgetenternew_loc = (By.XPATH,'/html/body/div/div/div[2]/div[2]/input[3]')
    passwordrequire_loc = (By.XPATH,'/html/body/div/div/div[2]/div[2]/p')
    forgetsubmitbutton_loc = (By.XPATH,'/html/body/div/div/div[2]/button')

    '''CRM portal'''
    menu_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[1]/div/div[1]/button')
    CRM_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[1]/div/div[2]/div[3]/a/div/span[1]/img')
    OSM_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[1]/div/div[2]/div[2]/a/div/span[2]')
    production_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[1]/div/div[2]/div[2]/a[2]')
    dashboard_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[1]/button[1]')
    company_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[1]/button[2]')
    contact_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[1]/button[3]')
    task_loc = (By.XPATH,'/html/body/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[2]/div[1]/button[4]')


    def typeUserName(self,username):
        # self.driver.find_element(By.NAME,'email').send_keys(username)
        self.driver.find_element(*self.username_loc).send_keys(username)

    def typePassword(self,password):
        self.driver.find_element(*self.password_loc).send_keys(password)

    @property
    def clickLogin(self):
        self.driver.find_element(*self.login_loc).click()

    def login(self,username,password):
        self.typeUserName(username)
        self.typePassword(password)
        self.clickLogin

    @property
    def getUsername(self):
        print('username is:',self.driver.find_element(*self.username_loc).text)
        return self.driver.find_element(*self.username_loc).text

    @property
    def getLoginError(self):
        '''Catch wrong info'''
        login_error = self.driver.find_element(*self.loginError_loc).text
        # print('login_error:',login_error)
        return login_error

    @property
    def getURL(self):
        '''get the url of portal'''
        sleep(5)
        print('url is:',self.driver.current_url)
        return self.driver.current_url

    def clickForget(self):
        self.driver.find_element(*self.forgetpwd_loc).click()

    @property
    def getForget(self):
        '''Forget password description'''
        print('forgot username:',self.driver.find_element(*self.forgetdescription_loc).text)
        return self.driver.find_element(*self.forgetdescription_loc).text

    @property
    def submitwrongemail(self):
        '''Forget password, submit wrong emain in username page'''
        self.driver.find_element(*self.inputemail_loc).send_keys('ddd')
        self.driver.find_element(*self.forgetsubmit_loc).click()

    @property
    def submitwrongemail_description(self):
        '''Forget password, submit wrong emain in username page, description require check'''
        error_string = self.driver.find_element(*self.wrongemailwaring_loc).text
        print('pwdrequire is:',error_string)
        return error_string

    def submitusername(self):
        '''Forget password, submit username page'''
        self.driver.find_element(*self.inputemail_loc).send_keys('tim@itrazotracetech.com')
        self.driver.find_element(*self.forgetsubmit_loc).click()

    @property
    def submitcode_username(self):
        '''Forget password, submit code page, Username check'''
        username_string = self.driver.find_element(*self.forgetusernamesubmit_loc).text
        print('submit code is:',username_string)
        return username_string

    @property
    def submitcode_entercode(self):
        '''Forget password, submit code page, enter security code check'''
        entercode_string = self.driver.find_element(*self.forgetentercode_loc).text
        print('entercode is:',entercode_string)
        return entercode_string

    @property
    def submitcode_enternewpwd(self):
        '''Forget password, submit code page, enter new pwd check'''
        enternewpwd_string = self.driver.find_element(*self.forgetenternew_loc).text
        print('enternewpwd is:',enternewpwd_string)
        return enternewpwd_string

    @property
    def submitcode_pwdrequire(self):
        '''Forget password, submit code page, pwd require check'''
        pwdrequire_string = self.driver.find_element(*self.passwordrequire_loc).text
        # print('pwdrequire is:',pwdrequire_string)
        return pwdrequire_string

    @property
    def crm_portal(self):
        '''crm portal'''
        # sleep(10)
        self.driver.find_element(*self.menu_loc).click()
        self.driver.find_element(*self.CRM_loc).click()
        dashboard = self.driver.find_element(*self.dashboard_loc).text
        company = self.driver.find_element(*self.company_loc).text
        contact = self.driver.find_element(*self.contact_loc).text
        task = self.driver.find_element(*self.task_loc).text
        # print(dashboard,company,contact,task)
        return dashboard,company,contact,task



if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://portal.abcd.com/")
    driver.implicitly_wait(10)

    login = Admin_Portal(driver)
    login.typeUserName('tim_acg_admin')
    login.typePassword('abcd')
    # login.typeUserName('sanjieyu')
    # login.typePassword('124')
    login.clickLogin
    login.getUsername
    login.getLoginError
    login.getURL
    login.clickForget()
    login.getForget
    login.submitusername()
    login.submitcode_pwdrequire
    login.crm_portal
    login.submitusername()
    login.submitcode_username
    login.admin_portal



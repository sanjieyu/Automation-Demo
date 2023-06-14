# Author:Yi Sun(Tim) 2023-5-06

'''Test Login page for Mobile app for Demo'''

import uiautomator2 as u2

class LoginPage():
    def __init__(self):
        # self.d = u2.connect_usb('R9JT10GK63H')
        # self.d = u2.connect('R9JT10GK63H')  # Same as above
        self.d = u2.connect('192.168.1.125:5555')
        self.d.unlock()
        self.d.screen_on()
        self.d.app_start('gfmobile.gforce')
        self.d.implicitly_wait(40)

    def typeUserName(self,username):
        self.d.xpath('//*[@text="Username"]').set_text(username)

    def typePassword(self,password):
        self.d.xpath('//*[@text="Password"]').set_text(password)

    @property
    def clickLogin(self):
        self.d.xpath('//*[@text="LOGIN"]').click()

    def login(self,username,password):
        self.typeUserName(username)
        self.typePassword(password)
        self.clickLogin

    @property
    def getUsername(self):
        return self.d.xpath('//*[@text="Username"]').get_text()

    @property
    def getPassword(self):
        return self.d.xpath('//*[@text="Password"]').get_text()


if __name__ == '__main__':
    login = LoginPage()
    login.typeUserName('yi_sun')
    login.typePassword('abcd')
    login.clickLogin

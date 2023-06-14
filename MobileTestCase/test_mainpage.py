# Author:Yi Sun(Tim) 2023-1-03

'''Test Main page of Mobile app for Gforce'''

import uiautomator2 as u2
from time import *
import unittest
from CommonModule.read_config import *
from login_page import *


class Test_MainPage(unittest.TestCase,LoginPage):
    def setUp(self) -> None:
        self.d = u2.connect('192.168.1.125:5555')
        self.config_read = ReadConfig()
        self.rep_username = self.config_read.app_username()
        self.rep_password = self.config_read.app_password()
        self.loginrep = LoginPage()
        self.loginrep.login(self.rep_username,self.rep_password)
        self.d.implicitly_wait(40)

    def tearDown(self) -> None:
        self.d.app_stop('gfmobile.gforce')
        self.d.app_clear('gfmobile.gforce')
        self.d.screen_off()
        # pass

    def test_app_main001(self):
        '''verify the main page after login the APP'''
        self.d.implicitly_wait(40)
        self.d.xpath('//*[@resource-id="android:id/button1"]').click()
        self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.View[1]/android.view.View[4]/android.widget.ImageView[1]').click()
        sleep(3)
        self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.View[1]/android.view.View[3]/android.widget.ImageView[1]').click()
        sleep(3)
        self.d.xpath('//*[@text=""]').click()
        sleep(3)
        self.d.click(0.897,0.92)

if __name__ == "__main__":
    unittest.main(verbosity=2)
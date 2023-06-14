# Author:Yi Sun(Tim) 2023-1-03

'''Test Login page of Mobile app for Gforce'''

import uiautomator2 as u2
from time import *
import unittest
from CommonModule.read_config import *
from login_page import *


class Test_LoginPage(unittest.TestCase):
    def setUp(self) -> None:
        # self.d = u2.connect_usb('R9JT10GK63H')
        # self.d = u2.connect('R9JT10GK63H')  # Same as above
        self.d = u2.connect('192.168.1.125:5555')
        self.d.unlock()
        self.d.screen_on()
        self.d.app_start('gfmobile.gforce')
        self.d.implicitly_wait(40)

    def tearDown(self) -> None:
        self.d.app_stop('gfmobile.gforce')
        self.d.app_clear('gfmobile.gforce')
        self.d.screen_off()

    @unittest.skip
    def test_app_login001(self):
        '''Verify the username login function'''
        # print('info:',self.d.info)
        self.assertEqual(self.d.xpath('//*[@text="Username"]').get_text(),'Username')

    @unittest.skip
    def test_app_login002(self):
        '''Verify the password login function'''
        # print('word is:',self.d.xpath('//*[@resource-id="com.sec.android.app.launcher:id/workspace"]/android.view.ViewGroup[1]/android.view.ViewGroup[1]').get_text())
        self.assertEqual(self.d.xpath('//*[@text="Password"]').get_text(),'Password')

    def test_app_login003(self):
        # self.assertEqual(self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]').get_text(),'Forgot password?')
        self.assertEqual(self.d.xpath('//*[@resource-id="com.sec.android.app.launcher:id/workspace"]/android.view.ViewGroup[1]/android.view.ViewGroup[1]').get_text(),'Forgot password?')

    def test_app_login004(self):
        # self.assertEqual(self.d.xpath('//*[@resource-id="android:id/content"]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[3]').get_text(),'Remember Me')
        self.assertEqual(self.d.xpath('//*[@resource-id="com.sec.android.app.launcher:id/workspace"]/android.view.ViewGroup[1]/android.view.ViewGroup[1]').get_text(),'Remember Me')

if __name__ == "__main__":
    unittest.main(verbosity=2)
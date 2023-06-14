# Author:Yi Sun(Tim) 2023-2-7

'''API Testing for iTrazoADI 2.0'''

import requests
import json
import unittest
from CommonModule.read_excel_title import *
from requests.sessions import Session


class AllAPI(unittest.TestCase,ExcelData):
    def setUp(self):
        self.data = ExcelData().read_excel()
        self.session = Session()

    def tearDown(self):
        pass

    # @unittest.skip
    def test_001(self):
        '''verify the status code for CRM_Customer API'''
        self.url = self.data[0]['url']  # get the 'url' from the first item of the dict
        self.r = requests.request(method=self.data[0]['method'],url=self.url)   # read the method from excel
        # self.assertEqual(self.r.status_code,int(200))
        self.assertEqual(self.data[0]['expect_data'],self.r.status_code)

    def test_002(self):
        '''verify the status code for CRM_Supplier API'''
        self.url = self.data[1]['url']
        self.r = requests.request(method=self.data[1]['method'],url=self.url)
        self.assertEqual(self.data[1]['expect_data'],self.r.status_code)

    def test_003(self):
        '''verify the status code for AM_CustomerList API'''
        self.url = self.data[2]['url']
        self.r = requests.request(method=self.data[2]['method'],url=self.url)
        self.assertEqual(self.data[2]['expect_data'],self.r.status_code)

    @unittest.skip
    def test_004(self):
        '''verify the status code for POST of AM_CreateCustomer API'''
        self.url = self.data[3]['url']
        self.header = {
            'content-length': '342',
            'origin': 'https://portal.dev.itrazoadi.com',
            'referer': 'https://portal.dev.itrazoadi.com/',
            'host': '65.8.134.6:443',
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en,en-US;q=0.9,en-GB;q=0.8',
            'connection': 'keep-alive',
            'content-type': 'application/json;charset=UTF-8',
            # "content-type": "application/x-amz-json-1.1",
            # 'x-amz-target':'AWSCognitoIdentityProviderService.InitiateAuth',
            'sec-ch-ua': '"Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.78',
        }
        self.data1 = self.data[3]['request_data']
        self.r = requests.request(method=self.data[3]['method'], url=self.url, data=self.data1)
        self.assertEqual(self.data[3]['expect_data'],self.r.status_code)

    def test_005(self):
        '''verify the status code for AM_Observation API without login'''
        self.url = self.data[4]['url']
        # self.auth = "Bearer eyJraWQiOiJIVXhrVFJjKzVTakc4Y1p0XC9XTUo2RWtxRG1ja3NpMTlXWWZcLzNKdVEwSGM9IiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJjMzUyNGQ3YS01ZTkzLTQ5ODItOTZhYy0yNDBkNWMzOWYzOWUiLCJjb2duaXRvOmdyb3VwcyI6WyJvcmdhbmljb2xpdmVvaWwiXSwiZW1haWxfdmVyaWZpZWQiOnRydWUsImlzcyI6Imh0dHBzOlwvXC9jb2duaXRvLWlkcC5hcC1zb3V0aGVhc3QtMi5hbWF6b25hd3MuY29tXC9hcC1zb3V0aGVhc3QtMl9lVWpEc0ZIRnMiLCJwaG9uZV9udW1iZXJfdmVyaWZpZWQiOmZhbHNlLCJjb2duaXRvOnVzZXJuYW1lIjoicWlhbiIsImF1ZCI6IjFraXJnOXBnZnVtanZpdTVvNXVldmk5NTNrIiwiZXZlbnRfaWQiOiI2YmYxMWM3NC0wODM1LTQ1NTAtYTNhYy0yNDFiOTFmYjAzNWYiLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTY3NTgxMDc3OCwibmFtZSI6IlFpYW4iLCJwaG9uZV9udW1iZXIiOiIrNjE0MjQxMTgxMzUiLCJleHAiOjE2NzU4MTQzNzgsImN1c3RvbTpyb2xlIjoiYWRtaW4iLCJpYXQiOjE2NzU4MTA3NzgsImVtYWlsIjoicWlhbkBpdHJhem90cmFjZXRlY2guY29tIn0.cewhkSFU-hiRBhYfUTVMjZl9A2_5IC82oIpf0HvTl-BZAHeUs2vQE0Qgf-s0L9ee7CEWJkXS-o-99fNDKZQCl9kEJEQ4fE_YIzsvmt3fgReqiubosSsBzKP2nKqPedVDmU_ItfQBIJzp6_Cbm1klGjn0taUkeLc9VluEWyDj4AD4Jv7KjpdpVPCLbfIUSB7yb8sfgxDu_78DtqmJ0VnUM6HKHd22ESE_bsJbV9pgA5XVVDFqNsOpg5_aL8TFYQ4LZ1LOVQQLhHASGAwfzF6TeoZaEM4JXdpizOq-WHGdaVAHADen-I5RUjcG7amqtAismYYXNYMGQo-407GmUzVlhw"
        self.r = requests.request(method=self.data[4]['method'],url=self.url)
        self.assertEqual(self.data[4]['expect_data'],self.r.status_code)

    def test_006(self):
        '''verify the status code for AM_MasterData API'''
        self.url = self.data[5]['url']
        self.r = requests.request(method=self.data[5]['method'], url=self.url)
        self.assertEqual(self.data[5]['expect_data'],self.r.status_code)

    @unittest.skip
    def test_007(self):
        '''verify the ADD function for AM_MasterData_CreatePreSet API'''
        self.url = self.data[6]['url']
        self.data_old = self.data[6]['request_data']
        # self.data = json.loads(self.data_old)           # change "string indices must be integers"
        # print('data is:',self.data)
        self.r = requests.request(method=self.data[6]['method'],url=self.url,data=self.data_old)
        self.assertEqual(self.data[6]['expect_data'],self.r.status_code)
        # self.list = requests.request(method=self.data[5]['method'], url=self.data[5]['url'])    # go to last case to get the list dict
        # responsedata = json.loads(self.list.text)
        # # print('response data is:',responsedata)
        # global refID
        # IDKey = 'Items'
        # for dictionary in responsedata:
        #     if IDKey in dictionary:
        #         print('yes1111')
        #         print('refID is:',dictionary[IDKey])
        #     else:
        #         print(f"The key '{IDKey}' does not exist in the dictionary.")

        # for key1,value1 in responsedata.items():
        #     print('key1 is',key1)
        #     print('value1 is',value1)
        #     if key1 == 'Items':
        #         for key2,value2 in value1.items():
        #             if key2 == "refID":
        #                 print('id is',value2)
            # print('is or not dict', isinstance(value1, dict))
            # if isinstance(value1,dict):
            #
            #     for key2,value2 in value1.items():
            #         if key2 == 'refID':
            #             print('refID is:',value2)
                    # refID = value1['refID']
        # refID = responsedata[1]['refID']
        # print('ref ID is:',refID)
    #
    def test_008(self):
        '''verify the status code for AM_MasterData_PMRules API'''
        self.url = self.data[7]['url']
        self.r = requests.request(method=self.data[7]['method'], url=self.url)
        self.assertEqual(self.data[7]['expect_data'],self.r.status_code)

    def test_009(self):
        '''verify the status code for AM_Allocation API'''
        self.url = self.data[8]['url']
        self.r = requests.request(method=self.data[8]['method'], url=self.url)
        self.assertEqual(self.data[8]['expect_data'],self.r.status_code)

    def test_010(self):
        '''verify the status code for CRM_CustomerDetails API'''
        self.url = self.data[9]['url']
        self.r = requests.request(method=self.data[9]['method'], url=self.url)
        self.assertEqual(self.data[9]['expect_data'],self.r.status_code)

    def test_011(self):
        '''verify the function for CRM_CustomerDetails API,return the correct "ABN"'''
        self.url = self.data[10]['url']
        self.r = requests.request(method=self.data[10]['method'], url=self.url)
        self.assertIn(self.data[10]['response'],self.r.text)

    def test_012(self):
        '''verify the status code for CRM_SupplierDetails API'''
        self.url = self.data[11]['url']
        self.r = requests.request(method=self.data[11]['method'], url=self.url)
        self.assertEqual(self.data[11]['expect_data'],self.r.status_code)

    def test_013(self):
        '''verify the function for CRM_SupplierDetails API,return the correct "address_ID"'''
        self.url = self.data[12]['url']
        self.r = requests.request(method=self.data[12]['method'], url=self.url)
        self.assertIn(self.data[12]['response'],self.r.text)
    #
    # @unittest.skip
    def test_014(self):
        '''verify the status code for AM_AssetTrackingList API'''
        self.url = self.data[13]['url']
        self.r = requests.request(method=self.data[13]['method'], url=self.url)
        self.assertEqual(self.data[13]['expect_data'],self.r.status_code)

    # @unittest.skip
    def test_015(self):
        '''verify the function for AM_AssetTrackingList,return the correct "QR code"'''
        self.url = self.data[14]['url']
        self.r = requests.request(method=self.data[14]['method'], url=self.url)
        self.assertIn(self.data[14]['response'],self.r.text)

    # @unittest.skip
    def test_016(self):
        '''verify the function for AM_AssetTrackingList,return the correct "alert_name"'''
        self.url = self.data[15]['url']
        self.r = requests.request(method=self.data[15]['method'], url=self.url)
        self.assertIn(self.data[15]['response'],self.r.text)

    # @unittest.skip
    def test_017(self):
        '''verify the function for AM_AssetTrackingList,return the correct "GEOFENCE type"'''
        self.url = self.data[16]['url']
        self.r = requests.request(method=self.data[16]['method'], url=self.url)
        self.assertIn(self.data[16]['response'],self.r.text)

    # @unittest.skip
    def test_018(self):
        '''verify the function for AM_AssetTrackingList,return the correct "asset_ID"'''
        self.url = self.data[17]['url']
        self.r = requests.request(method=self.data[17]['method'], url=self.url)
        self.assertIn(self.data[17]['response'],self.r.text)

    # @unittest.skip
    def test_019(self):
        '''verify the function for AM_AssetTrackingList,return the correct "Current_deviceID"'''
        self.url = self.data[18]['url']
        self.r = requests.request(method=self.data[18]['method'], url=self.url)
        self.assertIn(self.data[18]['response'],self.r.text)

    # @unittest.skip
    def test_020(self):
        '''verify the function for AM_AssetTrackingList,return the correct "Geofence Name"'''
        self.url = self.data[19]['url']
        self.r = requests.request(method=self.data[19]['method'], url=self.url)
        self.assertIn(self.data[19]['response'],self.r.text)
    #
    def test_021(self):
        '''verify the status code for AM_MasterData_AlertRules API'''
        self.url = self.data[20]['url']
        self.r = requests.request(method=self.data[20]['method'], url=self.url)
        self.assertEqual(self.data[20]['expect_data'],self.r.status_code)

    # @unittest.skip
    def test_022(self):
        '''verify the function for AM_MasterData_AlertRules,return the correct "Alert Preset Name"'''
        self.url = self.data[21]['url']
        self.r = requests.request(method=self.data[21]['method'], url=self.url)
        self.assertIn(self.data[21]['response'],self.r.text)

    def test_023(self):
        '''verify the function for AM_MasterData_AlertRules,return the correct "Count"'''
        self.url = self.data[22]['url']
        self.r = requests.request(method=self.data[22]['method'], url=self.url)
        self.assertIn(self.data[22]['response'],self.r.text)

    def test_024(self):
        '''verify the function for AM_MasterData_AlertRules,return the correct "Items"'''
        self.url = self.data[23]['url']
        self.r = requests.request(method=self.data[23]['method'], url=self.url)
        self.assertIn(self.data[23]['response'],self.r.text)

    def test_025(self):
        '''verify the status code for AM_MasterData_Customer Directory API'''
        self.url = self.data[24]['url']
        self.r = requests.request(method=self.data[24]['method'], url=self.url)
        self.assertEqual(self.data[24]['expect_data'],self.r.status_code)

    def test_026(self):
        '''verify the function for AM_MasterData_AlertRules,"Count" should greater equal than 0'''
        self.url = self.data[25]['url']
        self.r = requests.request(method=self.data[25]['method'], url=self.url)
        self.response = self.r.json()
        count_number = self.response['Count']
        self.assertGreaterEqual(count_number,0)

    def test_027(self):
        '''verify the status code for CRM_Logs_Meetings API'''
        self.url = self.data[26]['url']
        self.r = requests.request(method=self.data[26]['method'], url=self.url)
        self.assertEqual(self.data[26]['expect_data'],self.r.status_code)

    def test_028(self):
        '''verify the function for CRM_Logs_Meetings,"Count" should greater equal than 0'''
        self.url = self.data[27]['url']
        self.r = requests.request(method=self.data[27]['method'], url=self.url)
        self.response = self.r.json()
        count_number = self.response['Count']
        self.assertGreaterEqual(count_number,0)

    def test_029(self):
        '''verify the function for CRM_Logs_Meetings,"Scanned Count" should greater equal than 0'''
        self.url = self.data[28]['url']
        self.r = requests.request(method=self.data[28]['method'], url=self.url)
        self.response = self.r.json()
        count_number = self.response['Count']
        self.assertGreaterEqual(count_number,0)

    def test_030(self):
        '''verify the status code for CRM_Logs_Email API'''
        self.url = self.data[29]['url']
        self.r = requests.request(method=self.data[29]['method'], url=self.url)
        self.assertEqual(self.data[29]['expect_data'],self.r.status_code)

    def test_031(self):
        '''verify the function for CRM_Logs_Email,"Count" should greater equal than 0'''
        self.url = self.data[30]['url']
        self.r = requests.request(method=self.data[30]['method'], url=self.url)
        self.response = self.r.json()
        count_number = self.response['Count']
        self.assertGreaterEqual(count_number,0)

    def test_032(self):
        '''verify the function for CRM_Logs_Email,"Scanned Count" should greater equal than 0'''
        self.url = self.data[31]['url']
        self.r = requests.request(method=self.data[31]['method'], url=self.url)
        self.response = self.r.json()
        count_number = self.response['ScannedCount']
        self.assertGreaterEqual(count_number,0)

    def test_033(self):
        '''verify the status code for CRM_Logs_Calls API'''
        self.url = self.data[32]['url']
        self.r = requests.request(method=self.data[32]['method'], url=self.url)
        self.assertEqual(self.data[32]['expect_data'],self.r.status_code)

    def test_034(self):
        '''verify the function for CRM_Logs_Calls,"Count" should greater equal than 0'''
        self.url = self.data[33]['url']
        self.r = requests.request(method=self.data[33]['method'], url=self.url)
        self.response = self.r.json()
        count_number = self.response['Count']
        self.assertGreaterEqual(count_number,0)

    def test_035(self):
        '''verify the function for CRM_Logs_Calls,"Scanned Count" should greater equal than 0'''
        self.url = self.data[34]['url']
        self.r = requests.request(method=self.data[34]['method'], url=self.url)
        self.response = self.r.json()
        count_number = self.response['ScannedCount']
        self.assertGreaterEqual(count_number,0)

    # @unittest.skip
    def test_036(self):
        '''verify the POST for login API'''
        self.url = self.data[35]['url']
        self.header = {
            "content-type":"application/x-amz-json-1.1",
            "x-amz-target":"AWSCognitoIdentityProviderService.InitiateAuth",
        }
        # self.data1 = {
        #     "AuthFlow":"USER_PASSWORD_AUTH",
        #     "ClientId":"1kirg9pgfumjviu5o5uevi953k",
        #     "AuthParameters":{"USERNAME":"qian","PASSWORD":"Qian@123"},
        #     "ClientMetadata":{}
        # }
        # self.r = requests.request(method=self.data[35]['method'], url=self.url, headers=self.header, json=self.data1)   # use json=data if hardcoding the self.data1
        self.data1 = self.data[36]['request_data']
        # self.data2 = {"AuthFlow": "USER_PASSWORD_AUTH", "ClientId": "1kirg9pgfumjviu5o5uevi953k",
        #               "AuthParameters": {"USERNAME": "qian", "PASSWORD": "Qian@123"}, "ClientMetadata": {}}
        # self.r = requests.request(method=self.data[35]['method'], url=self.url, headers=self.header,data=json.dumps(self.data2))  # Line 289-291 for using the data format as a dict
        self.r = requests.request(method=self.data[35]['method'], url=self.url, headers=self.header, data=self.data1)    # use data=data if use config file read the self.data1
        self.assertEqual(self.data[35]['expect_data'],self.r.status_code)
#
    def test_037(self):
        '''Get the correct token from login API'''
        # global token_info1
        self.url = self.data[36]['url']
        self.header = {
            "content-type":"application/x-amz-json-1.1",
            "x-amz-target":"AWSCognitoIdentityProviderService.InitiateAuth",
        }
        self.data1 = self.data[36]['request_data']
        self.r = requests.request(method=self.data[36]['method'], url=self.url, headers=self.header, data=self.data1)
        token_info = json.loads(self.r.text).get('AuthenticationResult').get('AccessToken')
        print('token is:',token_info)
        self.assertIn(self.data[36]['response'],token_info)
        # return token_info1
#
    def test_038(self):
        '''verify the status code for AM_MasterData_CustomerDirectory API'''
        self.url = self.data[37]['url']
        self.r = requests.request(method=self.data[37]['method'], url=self.url)
        self.assertEqual(self.data[37]['expect_data'],self.r.status_code)

    def test_039(self):
        '''verify the function for AM_MasterData_CustomerDirectory,"Count" should greater equal than 0'''
        self.url = self.data[38]['url']
        self.r = requests.request(method=self.data[38]['method'], url=self.url)
        self.response = self.r.json()
        count_number = self.response['Count']
        self.assertGreaterEqual(count_number,0)

    def test_040(self):
        '''verify the function for AM_MasterData_CustomerDirectory,"Scanned Count" should greater equal than 0'''
        self.url = self.data[39]['url']
        self.r = requests.request(method=self.data[39]['method'], url=self.url)
        self.response = self.r.json()
        count_number = self.response['ScannedCount']
        self.assertGreaterEqual(count_number,0)

    @unittest.skip
    def test_041(self):
        '''Get the function for AM_MasterData_CustomerDirectory_CreateMember'''
        self.url = self.data[40]['url']
        # self.header = {
        #     'authority': 'x8iwc8pij7.execute-api.ap-southeast-2.amazonaws.com',
        #     'method': 'POST',
        #     'path': '/stage/ADI/dropdowns',
        #     'scheme': 'https',
        #     'content-length': '342',
        #     'origin': 'https://portal.staging.itrazoadi.com',
        #     'referer': 'https://portal.staging.itrazoadi.com/',
        #     # 'host': '65.8.33.32:443',
        #     'accept': 'application/json, text/plain, */*',
        #     'accept-encoding': 'gzip, deflate, br',
        #     'accept-language': 'en,en-US;q=0.9,en-GB;q=0.8',
        #     'connection': 'keep-alive',
        #     'content-type': 'application/json;charset=UTF-8',
        #     # "content-type": "application/x-amz-json-1.1",
        #     'x-amz-target':'AWSCognitoIdentityProviderService.InitiateAuth',
        #     'sec-ch-ua': '"Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"',
        #     'sec-ch-ua-mobile': '?0',
        #     'sec-ch-ua-platform': '"Windows"',
        #     'sec-fetch-dest': 'empty',
        #     'sec-fetch-mode': 'cors',
        #     'sec-fetch-site': 'cross-site',
        #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.78',
        # }
        self.data1 = self.data[40]['request_data']
        self.r = requests.request(method=self.data[40]['method'], url=self.url, data=self.data1)
        print('response is:',self.r.text)
        self.assertEqual(self.data[40]['expect_data'],self.r.status_code)

    def test_042(self):
        '''verify the status code for POST for AM_MasterData_CreatePreSet API'''
        self.url = self.data[41]['url']
        self.requestdata = self.data[41]['request_data']
        self.r = requests.request(method=self.data[41]['method'], url=self.url, data=self.requestdata)
        self.assertEqual(self.data[41]['expect_data'],self.r.status_code)

    def test_043(self):
        '''verify the status code for AM_MasterData_AssetPreSet_CreateCategories API'''
        self.url = self.data[42]['url']
        self.r = requests.request(method=self.data[42]['method'], url=self.url)
        self.assertEqual(self.data[42]['expect_data'],self.r.status_code)

    def test_044(self):
        '''verify the status code for POST for AM_MasterData_NewPMRule_Click API'''
        self.url = self.data[43]['url']
        self.requestdata = self.data[43]['request_data']
        self.r = requests.request(method=self.data[43]['method'], url=self.url, data=self.requestdata)
        self.assertEqual(self.data[43]['expect_data'],self.r.status_code)

    def test_045(self):
        '''verify the function for CRM_Customer,"Count" should greater equal than 0'''
        self.url = self.data[44]['url']
        self.r = requests.request(method=self.data[44]['method'], url=self.url)
        self.response = self.r.json()
        count_number = self.response['Count']
        self.assertGreaterEqual(count_number,0)

    def test_046(self):
        '''verify the function for CRM_Customer,"Scanned Count" should greater equal than 0'''
        self.url = self.data[45]['url']
        self.r = requests.request(method=self.data[45]['method'], url=self.url)
        self.response = self.r.json()
        count_number = self.response['ScannedCount']
        self.assertGreaterEqual(count_number,0)

    # @unittest.skip
    # no need because it has no this feature

    #def test_047(self):
        #'''verify the status code for POST for CRM_Supplier_CreateSupplier API'''
        #self.url = self.data[46]['url']
        #self.requestdata = self.data[46]['request_data']
        #self.r = requests.request(method=self.data[46]['method'], url=self.url, data=self.requestdata)
        #self.assertEqual(self.data[46]['expect_data'],self.r.status_code)


    def test_048(self):
        '''verify the status code for AM_Asset_Tracking_AddAsset API'''
        self.url = self.data[47]['url']
        self.requestdata = self.data[47]['request_data']
        self.r = requests.request(method=self.data[47]['method'], url=self.url, data=self.requestdata)
        self.assertEqual(self.data[43]['expect_data'],self.r.status_code)

    def test_049(self):
        '''verify the function for AM_Asset_Tracking_AddAsset,"Count" should greater equal than 0'''
        self.url = self.data[48]['url']
        self.r = requests.request(method=self.data[48]['method'], url=self.url)
        self.response = self.r.json()
        count_number = self.response['Count']
        self.assertGreaterEqual(count_number,0)

    def test_050(self):
        '''verify the function for AM_Asset_Tracking_AddAsset,"Scanned Count" should greater equal than 0'''
        self.url = self.data[49]['url']
        self.r = requests.request(method=self.data[49]['method'], url=self.url)
        self.response = self.r.json()
        count_number = self.response['ScannedCount']
        self.assertGreaterEqual(count_number,0)

    def test_051(self):
        '''Verify the Duplicate ABN function for AM_MasterData_CustomerDirectory_CreateMember'''
        self.url = self.data[50]['url']
        self.data1 = self.data[50]['request_data']
        self.r = requests.request(method=self.data[40]['method'], url=self.url, data=self.data1)
        self.assertEqual(self.data[50]['expect_data'],self.r.status_code)

    def test_052(self):
        '''verify the status code for AM_Sensors API'''
        self.url = self.data[51]['url']
        self.r = requests.request(method=self.data[51]['method'], url=self.url)
        self.assertEqual(self.data[51]['expect_data'],self.r.status_code)

    def test_053(self):
        '''verify the function for AM_Sensors,should return the correct device id.'''
        self.url = self.data[52]['url']
        self.r = requests.request(method=self.data[52]['method'], url=self.url)
        self.assertIn(self.data[52]['response'],self.r.text)
    #
    def test_054(self):
        '''verify the function for AM_Sensors,should return the correct asset id.'''
        self.url = self.data[53]['url']
        self.r = requests.request(method=self.data[53]['method'], url=self.url)
        self.assertIn(self.data[53]['response'],self.r.text)

    def test_055(self):
        '''verify the function for AM_Sensors,should return the correct model.'''
        self.url = self.data[54]['url']
        self.r = requests.request(method=self.data[54]['method'], url=self.url)
        self.assertIn(self.data[54]['response'],self.r.text)

    def test_056(self):
        '''verify the function for AM_Sensors,should return the correct sensor type.'''
        self.url = self.data[55]['url']
        self.r = requests.request(method=self.data[55]['method'], url=self.url)
        self.assertIn(self.data[55]['response'],self.r.text)

    def test_057(self):
        '''verify the function for AM_Sensors,should return the correct serial.'''
        self.url = self.data[56]['url']
        self.r = requests.request(method=self.data[56]['method'], url=self.url)
        self.assertIn(self.data[56]['response'],self.r.text)

    def test_058(self):
        '''verify the function for AM_Sensors,should return the correct customer id.'''
        self.url = self.data[57]['url']
        self.r = requests.request(method=self.data[57]['method'], url=self.url)
        self.assertIn(self.data[57]['response'],self.r.text)

    def test_059(self):
        '''verify the EDIT function for AM_Sensors,verify the PUT method.'''
        self.url = self.data[58]['url']
        self.requestdata = self.data[58]['request_data']
        self.r = requests.request(method=self.data[58]['method'], url=self.url,data=self.requestdata)
        self.assertEqual(self.data[58]['expect_data'],self.r.status_code)

    def test_060(self):
        '''verify the ADD function for AM_Sensors,verify the POST method.'''
        self.url = self.data[59]['url']
        self.requestdata = self.data[59]['request_data']
        self.r = requests.request(method=self.data[59]['method'], url=self.url,data=self.requestdata)
        self.assertEqual(self.data[59]['expect_data'],self.r.status_code)

    def test_061(self):
        '''verify the DELETE function for AM_Sensors,verify the POST method.'''
        self.url = self.data[60]['url']
        self.requestdata = self.data[60]['request_data']
        self.r = requests.request(method=self.data[60]['method'], url=self.url,data=self.requestdata)
        self.assertEqual(self.data[60]['expect_data'],self.r.status_code)

    @unittest.skip
    def test_062(self):
        '''verify the EDIT function for CRM_Supplier,verify the return code for PUT method.'''
        self.url = self.data[61]['url']
        self.requestdata = self.data[61]['request_data']
        self.r = requests.request(method=self.data[61]['method'], url=self.url,data=self.requestdata)
        self.assertEqual(self.data[61]['expect_data'],self.r.status_code)

    @unittest.skip
    def test_063(self):
        '''verify the EDIT function for CRM_Supplier,verify the response value for PUT method.'''
        self.url = self.data[62]['url']
        self.requestdata = self.data[62]['request_data']
        self.r = requests.request(method=self.data[62]['method'], url=self.url,data=self.requestdata)
        self.assertIn(self.data[62]['response'],self.r.text)

    @unittest.skip
    def test_064(self):
        '''verify the EDIT function for CRM_Supplier_address,verify the return code for PUT method.'''
        self.url = self.data[63]['url']
        self.requestdata = self.data[63]['request_data']
        self.r = requests.request(method=self.data[61]['method'], url=self.url,data=self.requestdata)
        self.assertEqual(self.data[63]['expect_data'],self.r.status_code)

    @unittest.skip
    def test_065(self):
        '''verify the EDIT function for CRM_Supplier_address,verify the response value for PUT method.'''
        self.url = self.data[64]['url']
        self.requestdata = self.data[64]['request_data']
        self.r = requests.request(method=self.data[64]['method'], url=self.url,data=self.requestdata)
        self.assertIn(self.data[64]['response'],self.r.text)

    def test_066(self):
        '''verify the Delete function for AM_Delete_Preset_Asset,verify the return code for DELETE method.'''
        self.url = self.data[65]['url']
        self.requestdata = self.data[65]['request_data']
        # self.r = requests.request(method=self.data[65]['method'], url=os.path.join(self.url+self.requestdata))
        print('url is',self.url+self.requestdata)
        self.r = requests.request(method=self.data[65]['method'], url=(self.url+self.requestdata))
        self.assertEqual(self.data[65]['expect_data'],self.r.status_code)


    def test_067(self):
        '''verify the active status for CRM_CustomerDetails API'''
        self.url = self.data[66]['url']
        self.r = requests.request(method=self.data[66]['method'], url=self.url)
        self.assertIn(self.data[66]['response'],self.r.text)

    def test_068(self):
        '''verify the function for CRM_CustomerDetails API,return the correct "name"'''
        self.url = self.data[67]['url']
        self.r = requests.request(method=self.data[67]['method'], url=self.url)
        self.assertIn(self.data[67]['response'],self.r.text)

    def test_069(self):
        '''verify the function for CRM_CustomerDetails API,return the correct "Customer Status"'''
        self.url = self.data[68]['url']
        self.r = requests.request(method=self.data[68]['method'], url=self.url)
        self.assertIn(self.data[68]['response'],self.r.text)

    def test_070(self):
        '''verify the function for CRM_CustomerDetails API,return the correct "Customer ID"'''
        self.url = self.data[69]['url']
        self.r = requests.request(method=self.data[69]['method'], url=self.url)
        self.assertIn(self.data[69]['response'],self.r.text)

    def test_071(self):
        '''verify the function for CRM_CustomerDetails,return the correct "industry"'''
        self.url = self.data[70]['url']
        self.r = requests.request(method=self.data[70]['method'], url=self.url)
        self.assertIn(self.data[70]['response'],self.r.text)

    def test_072(self):
        '''verify the ADD MEETING function for CRM_LogMeeting'''
        self.url = self.data[71]['url']
        self.requestdata = self.data[71]['request_data']
        self.r = requests.request(method=self.data[71]['method'], url=self.url,data=self.requestdata)
        self.assertEqual(self.data[71]['expect_data'],self.r.status_code)
        response_data = json.loads(self.r.text)      # change to dict
        global record_id                             # global this record_id to let the next function call
        record_id = response_data['record_ID']       # get the ID for the new added
        return record_id

    def test_073(self):
        '''verify the DELETE MEETING function for CRM_LogMeeting'''
        self.url = self.data[72]['url']
        self.r = requests.request(method=self.data[72]['method'],url=(self.url+'record_ID='+record_id+'&deleted_by=mc_admin'))
        self.assertEqual(self.data[72]['expect_data'],self.r.status_code)

    def test_074(self):
        '''verify the ADD CALL function for CRM_LogMeeting'''
        self.url = self.data[73]['url']
        self.requestdata = self.data[73]['request_data']
        self.r = requests.request(method=self.data[73]['method'], url=self.url,data=self.requestdata)
        self.assertEqual(self.data[73]['expect_data'],self.r.status_code)
        response_data = json.loads(self.r.text)      # change to dict
        global record_id                             # global this record_id to let the next function call
        record_id = response_data['record_ID']       # get the ID for the new added
        return record_id

    def test_075(self):
        '''verify the DELETE CALL function for CRM_LogMeeting'''
        self.url = self.data[74]['url']
        self.r = requests.request(method=self.data[74]['method'],url=(self.url+'record_ID='+record_id+'&deleted_by=mc_admin'))
        self.assertEqual(self.data[74]['expect_data'],self.r.status_code)

    def test_076(self):
        '''verify the return code for AM_AssetTracking Data'''
        self.url = self.data[75]['url']
        self.r = requests.request(method=self.data[75]['method'],url=self.url)
        self.assertEqual(self.data[75]['expect_data'],self.r.status_code)

    def test_077(self):
        '''verify the update function for CRM_Update_categories'''
        self.url = self.data[76]['url']
        self.requestdata = self.data[76]['request_data']
        self.r = requests.request(method=self.data[76]['method'],url=self.url,data=self.requestdata)
        self.assertEqual(self.data[76]['expect_data'],self.r.status_code)

    @unittest.skip
    def test_078(self):
        '''verify the Add function for AM_AlertRule'''
        self.url = self.data[77]['url']
        self.requestdata = self.data[77]['request_data']
        self.r = requests.request(method=self.data[77]['method'],url=self.url,data=self.requestdata)
        self.assertEqual(self.data[77]['expect_data'],self.r.status_code)

    def test_079(self):
        '''verify the EDIT function for AM_AlertRule, veriry the PUT method'''
        self.url = self.data[78]['url']
        self.requestdata = self.data[78]['request_data']
        self.r = requests.request(method=self.data[78]['method'],url=self.url,data=self.requestdata)
        self.assertEqual(self.data[78]['expect_data'],self.r.status_code)

    def test_080(self):
        '''verify the EDIT function for AM_AlertRule, update the "Alert Pre-set" name'''
        self.url = self.data[79]['url']
        self.requestdata = self.data[79]['request_data']
        self.r = requests.request(method=self.data[79]['method'],url=self.url,data=self.requestdata)
        self.assertIn(self.data[79]['response'],self.r.text)

    def test_081(self):
        '''verify the EDIT function for AM_AlertRule, update the "Measurement Type"'''
        self.url = self.data[80]['url']
        self.requestdata = self.data[80]['request_data']
        self.r = requests.request(method=self.data[80]['method'],url=self.url,data=self.requestdata)
        self.assertIn(self.data[80]['response'],self.r.text)

    def test_082(self):
        '''verify the EDIT function for AM_AlertRule, update the "Rule" name'''
        self.url = self.data[81]['url']
        self.requestdata = self.data[81]['request_data']
        self.r = requests.request(method=self.data[81]['method'],url=self.url,data=self.requestdata)
        self.assertIn(self.data[81]['response'],self.r.text)

    @unittest.skip
    def test_083(self):
        '''verify the ADD function for AM_PMRule'''
        self.url = self.data[82]['url']
        self.requestdata = self.data[82]['request_data']
        self.r = requests.request(method=self.data[82]['method'],url=self.url,data=self.requestdata)
        self.assertEqual(self.data[82]['expect_data'],self.r.status_code)

    def test_084(self):
        '''verify the EDIT function for AM_PMRule, verify the return code'''
        self.url = self.data[83]['url']
        self.requestdata = self.data[83]['request_data']
        self.r = requests.request(method=self.data[83]['method'],url=self.url,data=self.requestdata)
        self.assertEqual(self.data[83]['expect_data'],self.r.status_code)

    def test_085(self):
        '''verify the EDIT function for AM_PMRule, update the "PM Pre-set" name'''
        self.url = self.data[84]['url']
        self.requestdata = self.data[84]['request_data']
        self.r = requests.request(method=self.data[84]['method'],url=self.url,data=self.requestdata)
        self.assertIn(self.data[84]['response'],self.r.text)

    def test_086(self):
        '''verify the EDIT function for AM_PMRule, update the "name"'''
        self.url = self.data[85]['url']
        self.requestdata = self.data[85]['request_data']
        self.r = requests.request(method=self.data[85]['method'],url=self.url,data=self.requestdata)
        self.assertIn(self.data[85]['response'],self.r.text)

    def test_087(self):
        '''verify the EDIT function for AM_PMRule, update the "pm type"'''
        self.url = self.data[86]['url']
        self.requestdata = self.data[86]['request_data']
        self.r = requests.request(method=self.data[86]['method'],url=self.url,data=self.requestdata)
        self.assertIn(self.data[86]['response'],self.r.text)

    # @unittest.skip
    # def test_088(self):
    #     '''verify the ADD function for CRM_Contact'''
    #     self.url = self.data[87]['url']
    #     self.requestdata = self.data[87]['request_data']
    #     self.r = requests.request(method=self.data[87]['method'],url=self.url,data=self.requestdata)
    #     self.assertEqual(self.data[87]['expect_data'],self.r.status_code)

    # @unittest.skip
    def test_089(self):
        '''verify the EDIT function for CRM_Contact, verify the return code'''
        self.url = self.data[88]['url']
        self.requestdata = self.data[88]['request_data']
        self.r = requests.request(method=self.data[88]['method'],url=self.url,data=self.requestdata)
        self.assertEqual(self.data[88]['expect_data'],self.r.status_code)

    # @unittest.skip
    def test_090(self):
        '''verify the EDIT function for CRM_Contact, update the name'''
        self.url = self.data[89]['url']
        self.requestdata = self.data[89]['request_data']
        self.r = requests.request(method=self.data[89]['method'],url=self.url,data=self.requestdata)
        self.assertIn(self.data[89]['response'],self.r.text)

    @unittest.skip
    def test_091(self):
        '''verify the EDIT function for CRM_Contact, update the email'''
        self.url = self.data[90]['url']
        self.requestdata = self.data[90]['request_data']
        self.r = requests.request(method=self.data[90]['method'],url=self.url,data=self.requestdata)
        self.assertIn(self.data[90]['response'],self.r.text)

    # @unittest.skip
    def test_092(self):
        '''verify the EDIT function for CRM_Contact, update the position'''
        self.url = self.data[91]['url']
        self.requestdata = self.data[91]['request_data']
        self.r = requests.request(method=self.data[91]['method'],url=self.url,data=self.requestdata)
        self.assertIn(self.data[91]['response'],self.r.text)

    def test_093(self):
        '''verify the return code for CRM_Company'''
        self.url = self.data[92]['url']
        self.r = requests.request(method=self.data[92]['method'],url=self.url)
        self.assertEqual(self.data[92]['expect_data'],self.r.status_code)

    def test_094(self):
        '''verify the return value for CRM_Company which including "Companies"'''
        self.url = self.data[93]['url']
        self.r = requests.request(method=self.data[93]['method'],url=self.url)
        self.assertIn(self.data[93]['response'],self.r.text)

    def test_095(self):
        '''verify the return value for CRM_Company which including "Leads"'''
        self.url = self.data[94]['url']
        self.r = requests.request(method=self.data[94]['method'],url=self.url)
        self.assertIn(self.data[94]['response'],self.r.text)

    def test_096(self):
        '''verify the return value for CRM_Company which including "Customers"'''
        self.url = self.data[95]['url']
        self.r = requests.request(method=self.data[95]['method'],url=self.url)
        self.assertIn(self.data[95]['response'],self.r.text)

    def test_097(self):
        '''verify the return value for CRM_Company which including "Suppliers"'''
        self.url = self.data[96]['url']
        self.r = requests.request(method=self.data[96]['method'],url=self.url)
        self.assertIn(self.data[96]['response'],self.r.text)

    def test_098(self):
        '''verify the return code for CRM_Contact'''
        self.url = self.data[97]['url']
        self.r = requests.request(method=self.data[97]['method'],url=self.url)
        self.assertEqual(self.data[97]['expect_data'],self.r.status_code)

    def test_099(self):
        '''verify the return value for CRM_Contact,"Count" should greater equal than 0'''
        self.url = self.data[98]['url']
        self.r = requests.request(method=self.data[98]['method'], url=self.url)
        self.response = self.r.json()
        count_number = self.response['Count']
        self.assertGreaterEqual(count_number,0)

    def test_100(self):
        '''verify the return value for CRM_Contact,"ScannedCount" should greater equal than 0'''
        self.url = self.data[99]['url']
        self.r = requests.request(method=self.data[99]['method'], url=self.url)
        self.response = self.r.json()
        count_number = self.response['Count']
        self.assertGreaterEqual(count_number,0)

    def test_101(self):
        '''verify the return value for CRM_Company which including the correct "business_ID"'''
        self.url = self.data[100]['url']
        self.r = requests.request(method=self.data[100]['method'],url=self.url)
        self.assertIn(self.data[100]['response'],self.r.text)

    def test_102(self):
        '''verify the return code for CRM_ContactCompany'''
        self.url = self.data[101]['url']
        self.r = requests.request(method=self.data[101]['method'],url=self.url)
        self.assertEqual(self.data[101]['expect_data'],self.r.status_code)

    def test_103(self):
        '''verify the return value for CRM_ContactCompany,"Count" should greater equal than 0'''
        self.url = self.data[102]['url']
        self.r = requests.request(method=self.data[102]['method'], url=self.url)
        self.response = self.r.json()
        count_number = self.response['Count']
        self.assertGreaterEqual(count_number,0)

    def test_104(self):
        '''verify the return value for CRM_ContactCompany,"ScannedCount" should greater equal than 0'''
        self.url = self.data[103]['url']
        self.r = requests.request(method=self.data[103]['method'], url=self.url)
        self.response = self.r.json()
        count_number = self.response['Count']
        self.assertGreaterEqual(count_number,0)

    def test_105(self):
        '''verify the return code for CRM_Contact_Lead'''
        self.url = self.data[104]['url']
        self.r = requests.request(method=self.data[104]['method'],url=self.url)
        self.assertEqual(self.data[104]['expect_data'],self.r.status_code)

    def test_106(self):
        '''verify the return value for CRM_Contact_Lead,"Count" should greater equal than 0'''
        self.url = self.data[105]['url']
        self.r = requests.request(method=self.data[105]['method'], url=self.url)
        self.response = self.r.json()
        count_number = self.response['Count']
        self.assertGreaterEqual(count_number,0)

    def test_107(self):
        '''verify the return value for CRM_Contact_Lead,"ScannedCount" should greater equal than 0'''
        self.url = self.data[106]['url']
        self.r = requests.request(method=self.data[106]['method'], url=self.url)
        self.response = self.r.json()
        count_number = self.response['Count']
        self.assertGreaterEqual(count_number,0)

if __name__ == '__main__':
    unittest.main(verbosity=2)



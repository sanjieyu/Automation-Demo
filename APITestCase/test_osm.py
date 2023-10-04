# Author:Yi Sun(Tim) 2023-4-13

'''API Testing for OSM'''

import requests
import json
import unittest
from CommonModule.read_excel_title import *
from requests.sessions import Session

class OSM_API(unittest.TestCase,ExcelData):
    def setUp(self) -> None:
        self.data = ExcelData().read_excel()
        self.session = Session()

    def tearDown(self) -> None:
        pass

    def test_osm001(self):
        '''Get the correct token from login OSM API'''
        global token_info
        self.url = self.data[107]['url']
        self.header = {
            "content-type":"application/x-amz-json-1.1",
            "x-amz-target":"AWSCognitoIdentityProviderService.InitiateAuth",
        }
        self.data1 = self.data[107]['request_data']
        self.r = requests.request(method=self.data[107]['method'], url=self.url, headers=self.header, data=self.data1)
        token_info = json.loads(self.r.text).get('AuthenticationResult').get('IdToken')
        print('token is:',token_info)
        return token_info
    # #
    def test_osm002(self):
        '''verify the function POST call for OSM_AddItems'''
        # print('2',token_info)
        self.url = self.data[108]['url']
        self.postdata = self.data[108]['request_data']
        self.header = {
            "content-type": "application/json;charset=UTF-8",
            # "x-amz-target": "AWSCognitoIdentityProviderService.InitiateAuth",
            "authorization": token_info
        }
        self.r = requests.request(method=self.data[108]['method'],url=self.url,headers=self.header,data=self.postdata)
        self.assertEqual(self.data[108]['expect_data'],self.r.status_code)
    #
    def test_osm003(self):
        '''verify the status code for GET call of OSM_items'''
        # print('3',token_info)
        self.url = self.data[109]['url']
        self.header = {
            "content-type": "application/x-amz-json-1.1",
            "x-amz-target": "AWSCognitoIdentityProviderService.InitiateAuth",
            "authorization": token_info
        }
        self.r = requests.request(method=self.data[109]['method'], url=self.url,headers=self.header)
        self.assertEqual(self.data[109]['expect_data'],self.r.status_code)

    def test_osm004(self):
        '''verify the GET call for OSM_items,should return the correct itme name.'''
        self.url = self.data[110]['url']
        self.header = {
            "content-type": "application/json",
            "authorization": token_info
        }
        self.r = requests.request(method=self.data[110]['method'], url=self.url,headers=self.header)
        print('return ext is:',self.r.text)
        self.assertIn(self.data[110]['response'],self.r.text)

    def test_osm005(self):
        '''verify the GET call for OSM_items,should return the correct supplier_name.'''
        self.url = self.data[111]['url']
        self.header = {
            "content-type": "application/json",
            "authorization": token_info
        }
        self.r = requests.request(method=self.data[111]['method'], url=self.url,headers=self.header)
        # print('return ext is:', self.r.text)
        self.assertIn(self.data[111]['response'],self.r.text)

    def test_osm006(self):
        '''verify the GET call for OSM_items,should return the correct cost price.'''
        self.url = self.data[112]['url']
        self.header = {
            "content-type": "application/json",
            "authorization": token_info
        }
        self.r = requests.request(method=self.data[112]['method'], url=self.url,headers=self.header)
        # print('return ext is:', self.r.text)
        self.assertIn(self.data[112]['response'],self.r.text)

    def test_osm007(self):
        '''verify the GET call for OSM_items,should return the correct item_category.'''
        self.url = self.data[113]['url']
        self.header = {
            "content-type": "application/json",
            "authorization": token_info
        }
        self.r = requests.request(method=self.data[113]['method'], url=self.url,headers=self.header)
        # print('return ext is:', self.r.text)
        self.assertIn(self.data[113]['response'],self.r.text)

    def test_osm008(self):
        '''verify the GET call for OSM_items,should return the correct supplier_id.'''
        self.url = self.data[114]['url']
        self.header = {
            "content-type": "application/json",
            "authorization": token_info
        }
        self.r = requests.request(method=self.data[114]['method'], url=self.url,headers=self.header)
        # print('return ext is:', self.r.text)
        self.assertIn(self.data[114]['response'],self.r.text)
    #
    def test_osm009(self):
        '''verify the function DELETE call for OSM_AddItems'''
        self.url = self.data[115]['url']
        self.header = {
            "content-type": "application/json",
            "authorization": token_info
        }
        self.r = requests.request(method=self.data[115]['method'],url=self.url,headers=self.header)
        self.assertEqual(self.data[115]['expect_data'],self.r.status_code)
    # #
    def test_osm010(self):
        '''verify the function Get call for OSM_PSO_Add Inventory'''
        self.url = self.data[116]['url']
        self.header = {
            "content-type": "application/json",
            "authorization": token_info
        }
        self.r = requests.request(method=self.data[116]['method'],url=self.url,headers=self.header)
        self.assertEqual(self.data[116]['expect_data'],self.r.status_code)
    #
    def test_osm011(self):
        '''verify the function Get call for OSM_PSO_Table'''
        self.url = self.data[117]['url']
        self.header = {
            "content-type": "application/json",
            "authorization": token_info
        }
        self.r = requests.request(method=self.data[117]['method'],url=self.url,headers=self.header)
        self.assertEqual(self.data[117]['expect_data'],self.r.status_code)

    def test_osm012(self):
        '''verify the function Get call for OSM_PSO_Table to check the Created by'''
        self.url = self.data[118]['url']
        self.header = {
            "content-type": "application/json",
            "authorization": token_info
        }
        self.r = requests.request(method=self.data[118]['method'],url=self.url,headers=self.header)
        self.assertIn(self.data[118]['response'],self.r.text)

    def test_osm013(self):
        '''verify the Auto Generate Order ID function when create a PSO'''
        self.url = self.data[119]['url']
        self.header = {
            "content-type": "application/json",
            "authorization": token_info
        }
        self.r = requests.request(method=self.data[119]['method'],url=self.url,headers=self.header)
        self.assertEqual(self.data[119]['expect_data'],self.r.status_code)

    def test_osm014(self):
        '''verify the function of return the correct Order ID format when create a PSO'''
        self.url = self.data[120]['url']
        self.header = {
            "content-type": "application/json",
            "authorization": token_info
        }
        self.r = requests.request(method=self.data[120]['method'],url=self.url,headers=self.header)
        self.assertIn(self.data[120]['response'],self.r.text)

    def test_osm015(self):
        '''verify the Inspection Report Table'''
        self.url = self.data[121]['url']
        self.header = {
            "content-type": "application/json",
            "authorization": token_info
        }
        self.r = requests.request(method=self.data[121]['method'],url=self.url,headers=self.header)
        self.assertEqual(self.data[121]['expect_data'],self.r.status_code)

    @unittest.skip
    def test_osm016(self):
        '''verify the status of the Inspection Report'''
        self.url = self.data[122]['url']
        self.header = {
            "content-type": "application/json",
            "authorization": token_info
        }
        self.r = requests.request(method=self.data[122]['method'],url=self.url,headers=self.header)
        self.assertIn(self.data[122]['response'],self.r.text)

    @unittest.skip
    def test_osm017(self):
        '''verify the inspect by value of the Inspection Report'''
        self.url = self.data[123]['url']
        self.header = {
            "content-type": "application/json",
            "authorization": token_info
        }
        self.r = requests.request(method=self.data[123]['method'],url=self.url,headers=self.header)
        self.assertIn(self.data[123]['response'],self.r.text)

    def test_osm018(self):
        '''verify the Incident Report Table'''
        self.url = self.data[124]['url']
        self.header = {
            "content-type": "application/json",
            "authorization": token_info
        }
        self.r = requests.request(method=self.data[124]['method'],url=self.url,headers=self.header)
        self.assertEqual(self.data[124]['expect_data'],self.r.status_code)

    def test_osm019(self):
        '''verify the report by value of the Incident Report'''
        self.url = self.data[125]['url']
        self.header = {
            "content-type": "application/json",
            "authorization": token_info
        }
        self.r = requests.request(method=self.data[125]['method'],url=self.url,headers=self.header)
        self.assertIn(self.data[125]['response'],self.r.text)

    def test_osm020(self):
        '''verify the function for Incident report,"Count" should greater equal than 0'''
        self.url = self.data[126]['url']
        self.header = {
            "content-type": "application/json",
            "authorization": token_info
        }
        self.r = requests.request(method=self.data[126]['method'],url=self.url,headers=self.header)
        self.response = self.r.json()
        count_number = self.response['body']['Count']
        self.assertGreaterEqual(count_number,0)

    def test_osm021(self):
        '''verify the function for Inspection report,"Count" should greater equal than 0'''
        self.url = self.data[127]['url']
        self.header = {
            "content-type": "application/json",
            "authorization": token_info
        }
        self.r = requests.request(method=self.data[127]['method'],url=self.url,headers=self.header)
        self.response = self.r.json()
        count_number = self.response['body']['Count']
        self.assertGreaterEqual(count_number,0)

    def test_osm022(self):
        '''verify the function for Incident report,"ScannedCount" should greater equal than 0'''
        self.url = self.data[128]['url']
        self.header = {
            "content-type": "application/json",
            "authorization": token_info
        }
        self.r = requests.request(method=self.data[128]['method'],url=self.url,headers=self.header)
        self.response = self.r.json()
        count_number = self.response['body']['ScannedCount']
        self.assertGreaterEqual(count_number,0)

    def test_osm023(self):
        '''verify the function for Inspection report,"ScannedCount" should greater equal than 0'''
        self.url = self.data[129]['url']
        self.header = {
            "content-type": "application/json",
            "authorization": token_info
        }
        self.r = requests.request(method=self.data[129]['method'],url=self.url,headers=self.header)
        self.response = self.r.json()
        count_number = self.response['body']['ScannedCount']
        self.assertGreaterEqual(count_number,0)

    @unittest.skip
    def test_osm024(self):
        '''verify the Add a new  Inspection report function for POST Call'''
        self.url = self.data[130]['url']
        self.header = {
            "content-type": "application/json",
            "authorization": token_info
        }
        self.r = requests.request(method=self.data[129]['method'],url=self.url,headers=self.header)
        self.response = self.r.json()
        latest_inspection_ID = self.response['body']['Items'][0]['inspection_ID']
        num_id = int(latest_inspection_ID[3:])+1
        num_id_str = str(num_id).zfill(len(latest_inspection_ID)-3)
        new_inspection_ID = latest_inspection_ID[:3] + num_id_str
        latest_picklist_ID = self.response['body']['Items'][0]['picklist_ID']
        post_data = {"inspection_ID":new_inspection_ID,"inspected_on":"2023-05-02T00:29:11.803Z","inspected_by":"tim_acg_admin","picklist_ID":latest_picklist_ID,"total_orders":"1","inspection_outcome":"inspected","comments":"","reject_reason":""}
        print('post data is:',post_data)
        self.r1 = requests.request(method=self.data[130]['method'],url=self.url,headers=self.header,data=post_data)
        self.assertEqual(self.data[130]['expect_data'], self.r.status_code)

    def test_osm025(self):
        '''verify the Open Order Table'''
        self.url = self.data[131]['url']
        self.header = {
            "content-type": "application/json",
            "authorization": token_info
        }
        self.r = requests.request(method=self.data[131]['method'],url=self.url,headers=self.header)
        self.assertEqual(self.data[131]['expect_data'],self.r.status_code)

    def test_osm026(self):
        '''verify the Order Sumary'''
        self.url = self.data[132]['url']
        self.header = {
            "content-type": "application/json",
            "authorization": token_info
        }
        self.r = requests.request(method=self.data[132]['method'],url=self.url,headers=self.header)
        self.assertEqual(self.data[132]['expect_data'],self.r.status_code)

    def test_osm027(self):
        '''verify the function for Order table,"Open Order" count should greater equal than 0'''
        self.url = self.data[133]['url']
        self.header = {
            "content-type": "application/json",
            "authorization": token_info
        }
        self.r = requests.request(method=self.data[133]['method'],url=self.url,headers=self.header)
        self.response = self.r.json()
        print('response',self.response)
        open_number = self.response['body']['Item']['open']
        print('number is:',open_number)
        self.assertGreaterEqual(open_number,0)

    def test_osm028(self):
        '''verify the function for Order table,"Closed Order" count should greater equal than 0'''
        self.url = self.data[134]['url']
        self.header = {
            "content-type": "application/json",
            "authorization": token_info
        }
        self.r = requests.request(method=self.data[134]['method'],url=self.url,headers=self.header)
        self.response = self.r.json()
        print('response',self.response)
        open_number = self.response['body']['Item']['closed']
        print('number is:',open_number)
        self.assertGreaterEqual(open_number,0)

    def test_osm029(self):
        '''verify the function for Order table,"Canceld Order" count should greater equal than 0'''
        self.url = self.data[135]['url']
        self.header = {
            "content-type": "application/json",
            "authorization": token_info
        }
        self.r = requests.request(method=self.data[135]['method'],url=self.url,headers=self.header)
        self.response = self.r.json()
        print('response',self.response)
        open_number = self.response['body']['Item']['cancelled']
        print('number is:',open_number)
        self.assertGreaterEqual(open_number,0)

    def test_osm030(self):
        '''verify the function for Order table,"picklist Order" count should greater equal than 0'''
        self.url = self.data[136]['url']
        self.header = {
            "content-type": "application/json",
            "authorization": token_info
        }
        self.r = requests.request(method=self.data[136]['method'],url=self.url,headers=self.header)
        self.response = self.r.json()
        print('response',self.response)
        open_number = self.response['body']['Item']['picklist']
        # print('number is:',open_number)
        self.assertGreaterEqual(open_number,0)

    def test_osm031(self):
        '''verify the function for Order table,"incident_report" count should greater equal than 0'''
        self.url = self.data[137]['url']
        self.header = {
            "content-type": "application/json",
            "authorization": token_info
        }
        self.r = requests.request(method=self.data[137]['method'],url=self.url,headers=self.header)
        self.response = self.r.json()
        print('response',self.response)
        open_number = self.response['body']['Item']['incident_report']
        # print('number is:',open_number)
        self.assertGreaterEqual(open_number,0)

    def test_osm032(self):
        '''verify the Delivered Order Table'''
        self.url = self.data[138]['url']
        self.header = {
            "content-type": "application/json",
            "authorization": token_info
        }
        self.r = requests.request(method=self.data[138]['method'],url=self.url,headers=self.header)
        self.assertEqual(self.data[138]['expect_data'],self.r.status_code)

    def test_osm033(self):
        '''verify the Canceled Order Table'''
        self.url = self.data[139]['url']
        self.header = {
            "content-type": "application/json",
            "authorization": token_info
        }
        self.r = requests.request(method=self.data[139]['method'],url=self.url,headers=self.header)
        self.assertEqual(self.data[139]['expect_data'],self.r.status_code)

if __name__ == '__main__':
    unittest.main(verbosity=2)

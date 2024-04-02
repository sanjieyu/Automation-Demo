# Author:Yi Sun(Tim) 2023-8-29

'''Scheduled Automation Execution'''

import unittest
import time
import os
from CommonModule.send_report_api_hotmail import *
from CommonModule.send_report_UI_HTML import *
# from CommonModule.send_report_UI_hotmail import *


def ui_execution():
    '''These are for BeautifulReport'''
    # test_dir_ui = "C:\\Users\\Yi Sun\\PycharmProjects\\EGD\\UITestCase"
    # test_report_ui = "C:\\Users\\Yi Sun\\PycharmProjects\\EGD\\Report\\UI"
    #
    # loader_ui = unittest.TestLoader()
    # discover_ui = loader_ui.discover(test_dir_ui, pattern='test_*.py')
    # now = time.strftime("%Y-%m-%d_%H_%M_%S")
    #
    #
    # filename1 = '\\' + now + '_result1.html'
    # runner_ui = BeautifulReport(discover_ui)
    # runner_ui.report(description='EGD_UI_Automation_Test_Report', filename=filename1,
    #               log_path='C:\\Users\\Yi Sun\\PycharmProjects\\EGD\\Report\\UI')
    # new_report1 =send_report_ui.new_report_ui(test_report_ui)
    # send_report_ui.send_mail_ui(new_report1)

    '''These are for HTMLTestReport'''
    test_dir_ui = "C:\\Users\\Yi Sun\\PycharmProjects\\EGD\\UITestCase"
    test_report_ui = "C:\\Users\\Yi Sun\\PycharmProjects\\EGD\\Report\\UI"

    loader_ui = unittest.TestLoader()
    discover = loader_ui.discover(test_dir_ui, pattern='test_*.py')
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    filename1 = test_report_ui + '\\' + now + '_result.html'
    runner = HTMLTestReport(file_path=filename1,title='EGD_UI_Automation_Test_Report',
                            description='Automation Test starts at 18:00 everyday, and the Report automatically sent,DO NOT reply.You can check details from the attachment,thank you!')
    runner.run(discover)
    new_report1 = send_report_ui.new_report_ui(test_report_ui)
    send_report_ui.send_mail_ui(new_report1)

def api_execution():
    test_dir_api = "C:\\Users\\Yi Sun\\PycharmProjects\\EGD\\APITest"
    test_report_api = "C:\\Users\\Yi Sun\\PycharmProjects\\EGD\\Report\\API"

    loader_api = unittest.TestLoader()
    discover_api = loader_api.discover(test_dir_api, pattern='test_*.py')
    now = time.strftime("%Y-%m-%d_%H_%M_%S")


    filename2 = '\\' + now + '_result2.html'
    runner_api = BeautifulReport(discover_api)
    runner_api.report(description='EGD_API_Automation_Test_Report', filename=filename2,
                  log_path='C:\\Users\\Yi Sun\\PycharmProjects\\EGD\\Report\\API')
    new_report2 = send_report_api.new_report_api(test_report_api)
    send_report_api.send_mail_api(new_report2)
    # report_path = test_report_api+filename2
    # print('report path is:',report_path)
    # os.remove(report_path)

if __name__ == "__main__":
    '''for API automation'''
    # sys.path.append("C:\\Users\\Yi Sun\\PycharmProjects\\EGD")
    k = 1
    while k < 2:
        timing = time.strftime('%H_%M',time.localtime(time.time()))
        if timing == '18_00':    # will trigle the test at 18:00
            print('start to run API automation test')
            api_execution()
            print('finish running API automation test')
            break
        else:
            time.sleep(60)  # check every 60 sec
            print(timing)
    j = 1
    while j < 2:
        timing = time.strftime('%H_%M', time.localtime(time.time()))
        if timing == '18_05':  # will trigle the test at 18:15
            print('start to run UI automation test')
            ui_execution()
            print('finish running UI automation test')
            break
        else:
            time.sleep(60)  # check every 60 sec
            print(timing)
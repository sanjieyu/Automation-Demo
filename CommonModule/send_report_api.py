# Author:Yi Sun(Tim) 2022-9-07

'''Automation Test Report'''

import unittest
import time
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header
from BeautifulReport import BeautifulReport

class send_report_api:
    def new_report_api(test_report):
        lists = os.listdir(test_report)
        lists.sort(key=lambda fn: os.path.getmtime(test_report + '\\' + fn))
        file_new = os.path.join(test_report, lists[-1])
        print(file_new)
        return file_new

    def send_mail_api(file_new):
        with open(file_new, 'rb') as f:
            mail_body = f.read()

        sender = 'jerrymayi@hotmail.com'
        receiver = 'timsun1999@gmail.com'
        # receiver = ['timsun1999@gmail.com','jerrymayi@hotmail.com']
        subject = 'Automation API Test Report for Demo'
        '''mail body'''
        msg = MIMEMultipart('mixed')
        msg_html1 = MIMEText(
            'API Automation Test Report automatically sends everyday, DO NOT reply.You can check details from the attachment,thank you!')
        msg.attach(msg_html1)
        '''mail attachement'''
        m = MIMEText(mail_body, "html", "utf-8")
        m["Content-Type"] = "application/octet-stream"
        m["Content-Disposition"] = "attachment;filename = Automation_API_Test_Report for Demo.html"
        msg.attach(m)

        msg['From'] = sender
        msg['To'] = receiver
        # msg['To'] = ";".join(receiver)
        msg['Subject'] = subject

        try:
            smtpserver = 'smtp.hotmail.com'
            smtp = smtplib.SMTP(smtpserver, 587)
            smtp.ehlo()
            smtp.starttls()
            user = 'jerrymayi@hotmail.com'
            password = 'abcd'
            smtp.login(user, password)
            print('Start to send')
            smtp.sendmail(sender, receiver, msg.as_string())
            print('Mail send out, well done!')
            smtp.quit()
        except smtplib.SMTPException:
            print('Mail send error')

if __name__ == "__main__":+                                                 +
    # '''for API automation'''
    test_dir_api = "C:\\PycharmProjects\\Demo\\APITestCase"
    test_report_api = "C:\\PycharmProjects\\Demo\\Report"

    discover = unittest.defaultTestLoader.discover(test_dir_api, pattern='test_api.py')
    now = time.strftime("%Y-%m-%d_%H_%M_%S")

    filename1 = '\\' + now + '_result.html'
    runner = BeautifulReport(discover)
    runner.report(description='Automation_API_Test_Report', filename=filename1,
                  log_path='C:\\PycharmProjects\\Demo\\Report')

    new_report1 = send_report_api.new_report_api(test_report_api)
    send_report_api.send_mail_api(new_report1)







# Author:Yi Sun(Tim) 2022-09-13

'''Read Config function'''

import configparser
import os

class ReadConfig():
    def __init__(self):
        # current_path = os.path.abspath("..")   # get the 上一级目录
        # configfile_path = os.path.join(current_path,'Config\\config.ini')  # get the config file
        current_path = os.path.dirname(os.path.abspath(__file__))
        configfile_path = os.path.join(current_path,'..','Config','config.ini')
        # print('config loaction',configfile_path)
        self.cf = configparser.ConfigParser()
        self.cf.read(configfile_path)
        # print('section is:',self.cf.sections())
        # print('option is:',self.cf.options('config'))

    def get_url(self):
        url = self.cf.get('config','url')
        # print(url)
        return url

    def admin_username(self):
        username_admin = self.cf.get('member','username')
        # print(username_admin)
        return username_admin

    def admin_password(self):
        password_admin = self.cf.get('member','password')
        # print(password_admin)
        return password_admin

    # def app_username(self):
    #     username_rep = self.cf.get('rep','username')
    #     # print(username_rep)
    #     return username_rep
    #
    # def app_password(self):
    #     password_rep = self.cf.get('rep','password')
    #     # print(password_rep)
    #     return password_rep
    #
    # def supplier_username(self):
    #     username_supplier = self.cf.get('supplier','username')
    #     # print(username_supplier)
    #     return username_supplier
    #
    # def supplier_password(self):
    #     password_supplier = self.cf.get('supplier','password')
    #     # print(password_supplier)
    #     return password_supplier



if __name__ == '__main__':
    config1 = ReadConfig()
    config1.get_url()
    config1.admin_username()
    config1.admin_password()
    # config1.supplier_username()
    # config1.supplier_password()
    # config1.app_username()
    # config1.app_password()













# Author:Yi Sun(Tim) 2022-12-06

'''Read json function'''

import json
import os

class ReadJsonFile:
    def __init__(self):
        current_loc = "C:\\Users\\jerry\\PycharmProjects\\Gforce_New\\"
        self.json_file = os.path.join(current_loc,'Config\config.json')
        print('json file is',self.json_file)
        self.data = self.read_data()

    def read_data(self):
        with open(self.json_file) as j:
            data = json.load(j)
            print('data is:',data)
        return data

    def get_value(self,id):
        print("value is:",self.data[id])
        return self.data[id]

if __name__ == '__main__':
    readjson = ReadJsonFile()
    readjson.get_value('name')
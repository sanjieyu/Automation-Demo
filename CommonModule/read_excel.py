# Author:Yi Sun(Tim) 2022-12-06

'''Read Excel function'''

import xlrd
from xlrd import xldate_as_tuple
import datetime
import os

class ExcelData():
    '''
    xlrd中单元格的数据类型
    数字一律按浮点型输出，日期输出成一串小数，布尔型输出0或1，所以我们必须在程序中做判断处理转换
    成我们想要的数据类型
    0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
    '''

    def __init__(self):
        # current_loc = "C:\\Users\\jerry\\PycharmProjects\\Gforce_New\\"
        current_loc = "C:\\Users\\jerry\\PycharmProjects\\ADI\\"
        self.excel_file = os.path.join(current_loc, 'Config\\api_ADI_Staging.xlsx')
        # self.sheetname = 'Sheet1'
        self.data = xlrd.open_workbook(self.excel_file)
        # self.table = self.data.sheet_by_name(self.sheetname)
        # OR read the sheet from the sheet index
        self.table = self.data.sheet_by_index(0)
        # 获取第一行所有内容,如果括号中1就是第二行，这点跟列表索引类似
        self.keys = self.table.row_values(0)
        # 获取工作表的有效行数
        self.rowNum = self.table.nrows
        # 获取工作表的有效列数
        self.colNum = self.table.ncols

    def readExcel(self):
        datas = []
        for i in range(1,self.rowNum):
            sheet_data = {}
            for j in range(self.colNum):
                # 获取单元格数据类型
                c_type = self.table.cell(i,j).ctype
                # 获取单元格数据
                c_cell = self.table.cell_value(i,j)
                if c_type == 2 and c_type % 1 == 0:  # 如果是整形
                    c_cell = int(c_cell)
                elif c_type == 3:
                    # 转成datetime对象
                    date = datetime.datetime(*xldate_as_tuple(c_cell,0))
                    c_cell = date.strftime('%Y/%d/%m %H:%M:%S')
                elif c_type == 4:
                    c_cell = True if c_cell == 1 else False
                # sheet_data[self.keys[j]] = c_cell
                # 循环每一个有效的单元格，将字段与值对应存储到字典中
                # 字典的key就是excel表中每列第一行的字段
                sheet_data[self.keys[j]] = self.table.row_values(i)[j]
            # 再将字典追加到列表中
            datas.append(sheet_data)
        print('data is:',datas)
        return datas

if __name__ == "__main__":
    read_data = ExcelData()
    datas = read_data.readExcel()
    print('data is',datas)

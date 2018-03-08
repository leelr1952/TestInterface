import xlrd
from xlutils.copy import copy


class OperationExcel(object):
    def __init__(self,filename=None,sheet_id=None):
        if filename:
            self.filename = filename
            self.sheet_id = sheet_id
            self.data = self.get_data()
        else:
            self.filename = '../dataconfig/testinterface.xlsx'
            self.sheet_id = 0
            self.data = self.get_data()

    def get_data(self):
        data = xlrd.open_workbook(self.filename)
        tables = data.sheets()[self.sheet_id]
        return tables

    def get_lines(self):
        tables = self.data
        return tables.nrows

    def get_cell_value(self,row,col):
        return self.data.cell_value(row,col)

    def write_value(self,row,col,value):
        read_file = xlrd.open_workbook(self.filename)
        write_file = copy(read_file)
        write_sheet = write_file.get_sheet(0)
        write_sheet.write(row,col,value)
        write_file.save(self.filename)

if __name__ == '__main__':
    operationexcle = OperationExcel('../dataconfig/case1.xls',0)
    print(operationexcle.get_cell_value(2,0))
#/Users/lirui/PycharmProjects/testInterface/interface.xlsx
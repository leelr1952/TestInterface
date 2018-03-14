import xlrd
from xlutils.copy import copy


class OperationExcel(object):
    def __init__(self,filename=None,sheet_id=None):
        if filename:
            self.filename = filename
            self.sheet_id = sheet_id
            self.data = self.get_data()
        else:
            self.filename = '../dataconfig/case1.xlsx'
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

    #根据case_id获取行号对应到内容
    def from_case_id_get_row_data(self,case_id):
        num = self.from_case_id_get_row_num(case_id)
        row_data = self.get_row_data(num)
        return row_data

    #根据case_id获取行号
    def from_case_id_get_row_num(self, case_id):
        num = 0
        col_datas =self.get_col_data()
        for col_data in col_datas:
            if case_id in col_data:
                return num
            num += 1

    #获取行的内容
    def get_row_data(self,row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    #获取列的内容
    def get_col_data(self, col=None):
        tables = self.data
        if col is not None:
            col_data = tables.col_values(col)
        else:
            col_data = tables.col_values(0)
        return col_data


if __name__ == '__main__':
    operationexcle = OperationExcel('../dataconfig/case1.xls',0)
    print(operationexcle.get_cell_value(2,0))
#/Users/lirui/PycharmProjects/testInterface/interface.xlsx
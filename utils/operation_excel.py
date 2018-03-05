import xlrd


class OperationExcel(object):
    def __init__(self,filename=None,sheet_id=0):
        if filename:
            self.filename = filename
            self.sheet_id = sheet_id
            self.data = self.get_data()
        else:
            self.filename = '../dataconfig/interface.xlsx'

    def get_data(self):
        data = xlrd.open_workbook(self.filename)
        tables = data.sheets()[self.sheet_id]
        return tables

    def get_lines(self):
        tables = self.data
        return tables.nrows

    def get_cell_value(self,row,col):
        return self.data.cell_value(row,col)

if __name__ == '__main__':
    operationexcle = OperationExcel('../dataconfig/interface.xlsx',0)
    print(operationexcle.get_cell_value(2,0))
#/Users/lirui/PycharmProjects/testInterface/interface.xlsx
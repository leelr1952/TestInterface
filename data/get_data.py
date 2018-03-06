from utils.operation_excel import OperationExcel
from data import data_config
from utils.operation_json import OperationJson


class GetData(object):
    def __init__(self):
        self.opera_excel = OperationExcel()

    def get_case_lines(self):
        return self.opera_excel.get_lines()

    def get_is_run(self,row):
        flag =None
        col = data_config.global_val.get_run()
        run_model = self.opera_excel.get_cell_value(row,int(col))
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    def is_header(self,row):
        col = data_config.global_val.get_header()
        header = self.opera_excel.get_cell_value(row,col)
        if header == 'yes':
            return data_config.get_header.value()
        else:
            return None

    def get_request_method(self,row):
        col = data_config.global_val.get_request_way()
        request_method = self.opera_excel.get_cell_value(row,col)
        return request_method

    def get_url(self,row):
        col = data_config.global_val.get_url()
        url = self.opera_excel.get_cell_value(row,col)
        return url

    def get_request_data(self,row):
        col = data_config.global_val.get_data()
        data = self.opera_excel.get_cell_value(row,col)
        if data == '':
            return None
        else:
            return data

    def get_data_for_json(self,row):
        self.opera_json = OperationJson()
        data_json = self.opera_json.get_data(self.get_request_data(row))
        return data_json

    def get_expect(self,row):
        col = data_config.global_val.get_expect()
        expect = self.opera_excel.get_cell_value(row,col)
        if expect == '':
            return None
        else:
            return expect

if __name__ == '__main__':
    gd = GetData()
    print(gd.get_is_run(1))

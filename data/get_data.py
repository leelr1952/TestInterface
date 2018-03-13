from utils.operation_excel import OperationExcel
from data import data_config
from utils.operation_json import OperationJson


class GetData(object):
    def __init__(self,filename=None,sheet_id=None):
        self.opera_excel = OperationExcel(filename,sheet_id)

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
        header = self.opera_excel.get_cell_value(row,int(col))
        if header == 'yes':
            return data_config.get_header.value()
        else:
            return None

    def get_request_method(self,row):
        col = data_config.global_val.get_request_way()
        request_method = self.opera_excel.get_cell_value(row,int(col))
        return request_method

    def get_url(self,row):
        col = data_config.global_val.get_url()
        url = self.opera_excel.get_cell_value(row,int(col))
        return url

    def get_request_data(self,row):
        col = data_config.global_val.get_data()
        data = self.opera_excel.get_cell_value(row,int(col))
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
        expect = self.opera_excel.get_cell_value(row,int(col))
        if expect == '':
            return None
        else:
            return expect

    def write_result(self,row,value):
        col = data_config.global_val.get_result()
        self.opera_excel.write_value(row,int(col),value)

    def get_data_depend(self,row):
        col = data_config.global_val.get_data_depend()
        data_depend = self.opera_excel.get_cell_value(row, int(col))
        if data_depend == "":
            return None
        else:
            return data_depend

if __name__ == '__main__':
    gd = GetData()
    print(gd.get_is_run(1))

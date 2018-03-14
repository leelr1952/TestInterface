from utils.operation_excel import OperationExcel
from base.runmethod import RunMethod
from data.get_data import GetData
from jsonpath_rw import jsonpath,parse


class DependentData(object):

    def __init__(self, case_id):
        self.opexcel = OperationExcel()
        self.getdata = GetData()
        self.case_id = case_id
        self.runmethod = RunMethod()

    def get_case_line_data(self):
        row_data = self.opexcel.from_case_id_get_row_data(self.case_id)
        return row_data

    def rundependent(self):
        row_num = self.opexcel.from_case_id_get_row_num(self.case_id)
        request_data = self.getdata.get_data_for_json(row_num)
        url = self.getdata.get_url(row_num)
        method = self.getdata.get_request_method(row_num)
        header = self.getdata.is_header(row_num)
        res = self.runmethod.run_main(url, method, request_data, header)
        return res

    #在依赖response中查找依赖数据
    def get_data_for_key(self,row):
        depend_data = self.getdata.get_data_depend(row)
        response_data = self.rundependent()
        print(depend_data)
        print("************************")
        print(response_data)
        p_depend_data = parse(depend_data)
        madle = p_depend_data.find(response_data)
        return [math.value for math in madle][0]
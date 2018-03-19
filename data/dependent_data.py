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


if __name__ == '__main__':
    order = {
        "data": {
            "_input_charset": "utf-8",
            "body": "慕课网订单-1710141907182334",
            "it_b_pay": "1d",
            "notify_url": "http://order.imooc.com/pay/notifyalipay",
            "out_trade_no": "1710141907182334",
            "partner": "2088002966755334",
            "payment_type": "1",
            "seller_id": "yangyan01@tcl.com",
            "service": "mobile.securitypay.pay",
            "sign": "kZBV53KuiUf5HIrVLBCcBpWDg%2FnzO%2BtyEnBqgVYwwBtDU66Xk8VQUTbVOqDjrNymCupkVhlI%2BkFZq1jOr8C554KsZ7Gk7orC9dDbQlpr%2BaMmdjO30JBgjqjj4mmM%2Flphy9Xwr0Xrv46uSkDKdlQqLDdGAOP7YwOM2dSLyUQX%2Bo4%3D",
            "sign_type": "RSA",
            "string": "_input_charset=utf-8&body=慕课网订单-1710141907182334&it_b_pay=1d&notify_url=http://order.imooc.com/pay/notifyalipay&out_trade_no=1710141907182334&partner=2088002966755334&payment_type=1&seller_id=yangyan01@tcl.com&service=mobile.securitypay.pay&subject=慕课网订单-1710141907182334&total_fee=299&sign=kZBV53KuiUf5HIrVLBCcBpWDg%2FnzO%2BtyEnBqgVYwwBtDU66Xk8VQUTbVOqDjrNymCupkVhlI%2BkFZq1jOr8C554KsZ7Gk7orC9dDbQlpr%2BaMmdjO30JBgjqjj4mmM%2Flphy9Xwr0Xrv46uSkDKdlQqLDdGAOP7YwOM2dSLyUQX%2Bo4%3D&sign_type=RSA",
            "subject": "慕课网订单-1710141907182334",
            "total_fee": 299
            },
            "errorCode": 1000,
            "errorDesc": "成功",
            "status": 1,
            "timestamp": 1507979239100
        }
    res = "data.out_trade_no"
    json_exe = parse(res)
    madle = json_exe.find(order)
    print([math.value for math in madle][0])
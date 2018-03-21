from base.runmethod import RunMethod
from data.get_data import GetData
from data.dependent_data import DependentData
from utils.common_util import CommonUtil
from utils.send_mail import SendMail
from utils.operation_cookie import OperationCookie
from utils.operation_json import OperationJson
import json


class RunTest(object):
    def __init__(self):
        self.runmethod = RunMethod()
        self.getdata = GetData()
        self.commonutil = CommonUtil()
        self.sendmail = SendMail()

    def go_on_run(self):
        pass_count = []
        fail_count = []
        cookies = None
        rows = self.getdata.get_case_lines()
        for i in range(1,rows):
            is_run = self.getdata.get_is_run(i)
            if is_run:
                url = self.getdata.get_url(i)
                is_depend = self.getdata.is_depend(i)
                request_method = self.getdata.get_request_method(i)
                expect = self.getdata.get_expect(i)
                # print(expect)
                is_cookie = self.getdata.is_cookie(i)
                is_header = self.getdata.is_header(i)
                data = self.getdata.get_data_for_json(i)
                print(data)
                depend_case = self.getdata.is_depend(i)
                if is_depend:
                    self.depend_data = DependentData(depend_case)
                    field_depend = self.getdata.get_field_depend(i)
                    data_depend = self.depend_data.get_data_for_key(i)
                    data[field_depend] = data_depend

                if is_cookie == 'write':
                    res = self.runmethod.run_main(url, request_method, data)
                    op_cookie = OperationCookie(json.loads(res))
                    op_cookie.write_cookie()

                if is_cookie == 'yes':
                    op_json = OperationJson('../dataconfig/cookie.json')
                    cookie = op_json.get_data("apsid")
                    cookies = {
                        "apsid":cookie
                    }


                res = self.runmethod.run_main(url,request_method,data,is_header,cookies)

                if self.commonutil.iscontain(expect,res):
                    print("测试通过")
                    self.getdata.write_result(i,"测试通过")
                    pass_count.append(i)
                else:
                    print(expect)
                    print(res)
                    print("测试失败")
                    self.getdata.write_result(i,res)
                    fail_count.append(i)
            else:
                return None
        #self.sendmail.sendmain(pass_count, fail_count)

if __name__=='__main__':
    runtest = RunTest()
    runtest.go_on_run()
from base.runmethod import RunMethod
from data.get_data import GetData
from data.dependent_data import DependentData
from utils.common_util import CommonUtil


class RunTest(object):
    def __init__(self):
        self.runmethod = RunMethod()
        self.getdata = GetData()
        self.commonutil = CommonUtil()

    def go_on_run(self):
        rows = self.getdata.get_case_lines()
        for i in range(1,rows):
            is_run = self.getdata.get_is_run(i)
            if is_run:
                url = self.getdata.get_url(i)
                is_depend = self.getdata.is_depend(i)
                request_method = self.getdata.get_request_method(i)
                expect = self.getdata.get_expect(i)
                is_header = self.getdata.is_header(i)
                data = self.getdata.get_data_for_json(i)
                depend_case = self.getdata.is_depend(i)
                if is_depend:
                    self.depend_data = DependentData(depend_case)
                    field_depend = self.getdata.get_field_depend(i)
                    data_depend = self.depend_data.get_data_for_key(i)
                    data[field_depend] = data_depend
                res = self.runmethod.run_main(url,request_method,data,is_header)
                #print(res)
                if self.commonutil.iscontain(expect,res):
                    #print("测试通过")
                    self.getdata.write_result(i,"测试通过")
                else:
                    #print("测试失败")
                    self.getdata.write_result(i,"测试失败")
            else:
                return None

if __name__=='__main__':
    runtest = RunTest()
    runtest.go_on_run()
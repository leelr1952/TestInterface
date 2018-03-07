import unittest
import mock
import json
from demo import RunMain
from mock_demo import mock_test


class TestMethod(unittest.TestCase):
    def setUp(self):
        self.run = RunMain()
        print('test---->setUp')

    def test_01(self):
        url = 'http://coding.imooc.com/api/cate'
        data = {
            'timestamp':'1507006626132',
            'uid':'5249191',
            'uuid':'5ae7d1a22c82fb89c78f603420870ad7',
            'secrect':'078474b41dd37ddd5efeb04aa591ec12',
            'token':'0b4c502ba647664be04dfedb32ad4f3d',
            'cid':'0',
            'errorCode':1001
        }
        #mock_data = mock.Mock(return_value=data)
        #self.run.run_main = mock_data
        #res = self.run.run_main(url,'POST',data)

        res = mock_test(self.run.run_main, url, 'POST', data, data)
        print(json.dumps(res, indent=2, sort_keys=True))
        self.assertEqual(res['errorCode'],1001,'测试失败')
        print('这是第一个测试方法')

    def test_02(self):
        url = 'http://coding.imooc.com/api/cate'
        data = {
            'timestamp': '1507006626132',
            'uid': '5249191',
            'uuid': '5ae7d1a22c82fb89c78f603420870ad7',
            'secrect': '078474b41dd37ddd5efeb04aa591ec12',
            'token': '0b4c502ba647664be04dfedb32ad4f3d',
            'cid': '0'
        }
        res = self.run.run_main(url, 'POST', data)
        print(res)
        print('这是第二个测试方法')

    def tearDown(self):
        print('test---->tearDown')


if __name__ == '__main__':
    unittest.main()
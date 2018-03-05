import requests
import json


class RunMain(object):
    def send_get(self, url, data=None):
        res = requests.get(url, data).json()
        #print(json.dumps(res, indent=2, sort_keys=True))
        return json.dumps(res, indent=2, sort_keys=True)

    def send_post(self,url, data=None):
        res = requests.post(url, data).json()
        #print(json.dumps(res, indent=2, sort_keys=True))
        #return json.dumps(res, indent=2, sort_keys=True)
        return res

    def run_main(self,url,method,data=None):
        if method == 'GET':
            res = self.send_get(url,data)
        if method == 'POST':
            res = self.send_post(url,data)
        return res

if __name__ == '__main__':
    #url = 'http://www.imooc.com/m/web/shizhanapi/loadmorepingjia.html?cart=11'
    url = 'http://coding.imooc.com/api/cate'
    data = {
        'timestamp': '1507006626132',
        'uid': '5249191',
        'uuid': '5ae7d1a22c82fb89c78f603420870ad7',
        'secrect': '078474b41dd37ddd5efeb04aa591ec12',
        'token': '0b4c502ba647664be04dfedb32ad4f3d',
        'cid': '0'
    }
    run = RunMain()
    print(run.run_main(url,'POST',data))
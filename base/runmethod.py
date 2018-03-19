import requests
import json
import urllib
import urllib3


class RunMethod(object):
    def post_main(self,url,data,header=None):
        res = None
        if header is not None:
            res = requests.post(url=url,data=data,headers=header).json()
        else:
            res = requests.post(url=url,data=data).json()
        return res

    def get_main(self,url,data,header=None):
        urllib3.disable_warnings()
        res = None
        if header is not None:
            url_data = urllib.parse.urlencode(data)
            #print(data)
            url = url + "?" + url_data
            print(url)
            res = requests.get(url=url, data=data, headers=header ,verify=False)
        else:
            res = requests.get(url=url, data=data)

        return res.text

    def run_main(self,url,method,data=None,header=None):
        res = None
        if method == 'POST':
            res = self.post_main(url,data,header)
            return json.dumps(res, ensure_ascii=True, sort_keys=True, indent=2)

        else:
            res = self.get_main(url,data,header)
            return res


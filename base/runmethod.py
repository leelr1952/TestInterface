import requests
import json
import urllib
import urllib3


class RunMethod(object):
    def post_main(self,url,data,header=None,cookies=None):
        res = None
        s = requests.session()
        s.keep_alive = False
        if header is not None:
            res = s.post(url=url,data=data,headers=header,cookies=cookies).json()
        else:
            res = s.post(url=url,data=data,cookies=cookies).json()
        return res

    def get_main(self,url,data,header=None,cookies=None):
        urllib3.disable_warnings()
        res = None
        s = requests.session()
        s.keep_alive = False
        if header is not None:
            url_data = urllib.parse.urlencode(data)
            #print(data)
            url = url + "?" + url_data
            print(url)
            res = s.get(url=url, data=data, headers=header, cookies=cookies, verify=False)
        else:
            res = s.get(url=url, data=data, cookies=cookies, verify=False)

        return res.text

    def run_main(self,url,method,data=None,header=None,cookies=None):
        res = None
        if method == 'POST':
            res = self.post_main(url,data,header,cookies)
            return json.dumps(res, ensure_ascii=True, sort_keys=True, indent=2)

        else:
            res = self.get_main(url,data,header,cookies)
            return res


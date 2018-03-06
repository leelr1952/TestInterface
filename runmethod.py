import requests


class RunMethod(object):
    def post_main(self,url,data,header=None):
        res = None
        if header is not None:
            res = requests.post(url=url,data=data,headers=header).json()
        else:
            res = requests.post(url=url,data=data).json()
        return res

    def get_main(self,url,data,header=None):
        res = None
        if header is not None:
            res = requests.get(url=url, data=data, headers=header).json()
        else:
            res = requests.get(url=url, data=data).json()
        return res

    def run_main(self,url,method,data=None,header=None):
        res = None
        if method == 'POST':
            res = self.post_main(url,data,header)
        else:
            res = self.get_main(url,data,header)
        return res
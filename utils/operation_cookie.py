import requests
from utils.operation_json import OperationJson


class OperationCookie(object):
    def __init__(self, res):
        self.res = res

    def get_response_url(self):
        url = self.res["data"]["url"][0]
        return url + "&callback=jQuery191009915392497100939_1521640415811&_=1521640415814"

    def get_cookie(self):
        cookie = requests.get(self.get_response_url()).cookies
        cookie = requests.utils.dict_from_cookiejar(cookie)
        cookie = str(cookie).replace("\'","\"")
        return cookie

    def write_cookie(self):
        op_json = OperationJson("../dataconfig/cookie.json")
        op_json.write_json(self.get_cookie())


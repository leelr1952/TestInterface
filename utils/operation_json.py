import json


class OperationJson(object):

    def __init__(self):
        self.data = self.read_data()

    def read_data(self):
        with open('../dataconfig/user.json') as fp:
            data = json.load(fp)
            return data

    def get_data(self,id):
        return self.data[id]


if __name__ == '__main__':
    opjson = OperationJson()
    print(opjson.get_data('addcart'))
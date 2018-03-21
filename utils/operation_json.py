import json


class OperationJson(object):

    def __init__(self, file_path = None):
        if file_path is not None:
            self.file_path = file_path
        else:
            self.file_path = "../dataconfig/user.json"
        # self.data = self.read_data()

    def read_data(self):
        with open(self.file_path) as fp:
            data = json.load(fp)
            return data

    def get_data(self,id):
        return self.read_data()[id]

    def write_json(self, data):
        with open("../dataconfig/cookie.json", "w+") as f:
            f.write(data)


if __name__ == '__main__':
    opjson = OperationJson()
    print(opjson.get_data('addcart'))
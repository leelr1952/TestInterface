class global_val:
    id = '0'
    name = '1'
    url = '2'
    run = '3'
    request_way = '4'
    header = '5'
    case_depend = '6'
    data_depend = '7'
    field_depend = '8'
    data = '9'
    expect = '10'
    result = '11'

    def get_id():
        return global_val.id

    def get_name():
        return global_val.name

    def get_url():
        return global_val.url

    def get_run():
        return global_val.run

    def get_request_way():
        return global_val.request_way

    def get_header():
        return global_val.header

    def get_case_depend():
        return global_val.case_depend

    def get_data_depend():
        return global_val.data_depend

    def get_field_depend():
        return global_val.field_depend

    def get_data():
        return global_val.data

    def get_expect():
        return global_val.expect

    def get_result():
        return global_val.result

    def get_header_value():
        header = {
            "Host":"m.imooc.com",
            "Connection":"keep-alive",
            "Accept":"application/json, text/javascript, */*; q=0.01",
            "X-Requested-With":"XMLHttpRequest",
            "User-Agent":"Mozilla/5.0 (Linux; Android 4.4.2; OPPO R11 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36",
            "Referer":"https://m.imooc.com/confirmorder?type=1&typeid=144",
            "Accept-Encoding":"gzip,deflate",
            "Accept-Language":"zh-CN,en-US;q=0.8",
            "Cookie":"UM_distinctid=1622d85eb9e33-009e8e888-5b546908-4f1a0-1622d85eb9f12b; imooc_uuid=e767fc32-c5db-447f-bca3-813448a4761c; imooc_isnew_ct=1521190318; page=https://m.imooc.com/; imooc_isnew=2; cvde=5aae4a0880e67-1; loginstate=1; apsid=M5M2Q3YzBkOGVjYzdkYzE3OTM4M2IwYzIwYjRkMWYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANTI0OTE5MQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGYyMWRhOTg4NzQ4YzA5NDBlYWNmOGFmMzE1NDFjOGJmCEquWghKrlo%3DMG; CNZZDATA1261728817=787280194-1521177869-%7C1521367055; Hm_lvt_c92536284537e1806a07ef3e6873f2b3=1521182175,1521371573,1521371668; Hm_lpvt_c92536284537e1806a07ef3e6873f2b3=1521371743"
        }

        return header

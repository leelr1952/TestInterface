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
            "header":"1234",
            "cookie":"Mushishi"
        }

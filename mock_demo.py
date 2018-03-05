from mock import Mock


def mock_test(mock_method, url, method, request_data, response_data):
    mock_method = Mock(return_value=response_data)
    return mock_method(url, method, request_data)
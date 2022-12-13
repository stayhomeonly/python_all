# coding:utf-8
"""
#@Time：2022/10/18-10:20
#@file：test_login
#@Project:python_new_study
#@Content:

"""
"""主流程"""
from comms.excel_utiles import ReadExcel
import pytest, requests, json
from comms.constants import DATA_FILE


class TestLogin:
    cases = ReadExcel.read_data_all(DATA_FILE, 'login')

    @pytest.mark.parametrize('case', cases)
    def test_login(self, case):
        # 请求内容

        request_body = case.data
        request_body1 = json.dumps(request_body)
        # 请求体
        headers = {"Content-type": "application/json"}

        response = requests.post(url=case.url, data=eval(request_body1), headers=headers)
        res = response.json()
        # print(res)

        assert res['code'] == '200'


if __name__ == '__main__':
    pytest.main(['-vs', './test_login.py'])

"""
---------------------------------
作者: 星光_黄宗泽
创建时间: 2022/9/4-16:27
知识点: 
---------------------------------
"""
import requests, pytest
from autotest01.comms.db_utils import DBUtils


class TestRegister():
    datas = [
        {'case_id': '1',
         'case_data': {"username": "xiaozhen", "password": "a123456", "re_password": "a123456", "phone": "18822223334",
                       "sex": "",
                       "birthday": "", "qq": '', 'email': ''}, 'exp': '注册成功'},
        {'case_id': '2',
         'case_data': {"username": "", "password": "a123456", "re_password": "a123456", "phone": "18822223333",
                       "sex": "",
                       "birthday": "", "qq": '', 'email': ''}, 'exp': "用户名不能为空"},
        {'case_id': '3',
         'case_data': {"username": "xiaozhen1", "password": "", "re_password": "a123456", "phone": "18822223332",
                       "sex": "",
                       "birthday": "", "qq": '', 'email': ''}, 'exp': '密码不能为空'}
    ]

    @pytest.mark.parametrize('data', datas)
    def test_register(self, data):
        res = requests.post(url='http://127.0.0.1:6666/business/regist_form', data=data['case_data'])
        res = res.json()
        assert data['exp'] == res['msg']

        if data['case_id'] in ('1',):
            db = DBUtils()
            db.cud('delete from tb_user where name = %s', (data["case_data"]["username"],))


if __name__ == '__main__':
    pytest.main(['-vs', './test_register'])

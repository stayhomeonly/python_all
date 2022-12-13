"""
-------------------------------------------------
   Author:Mr.Liu
   date: 2022/8/14-15:13
   contents:
-------------------------------------------------
"""
import os

import pytest, requests
from day15.test_excel_data.excel_test02 import ReadExcel
from logger02 import logger
import allure


@allure.feature("登录模块")  # allure报告的模块名称
class TestLogin:
    cases = ReadExcel.read_data_all('./cases.xlsx', 'Login')

    @allure.story("登录模块的子模块")  # allure报告的模块子层
    @allure.severity("critical")  # allure报告修改case优先级
    @allure.description('我们的第一个登录小程序')  # 备注(用例描述)
    @pytest.mark.parametrize("case", cases)
    def test_login(self, case):
        allure.dynamic.title(case.case_title)
        allure.attach(body=case.url,name='接口地址')
        allure.attach(body=case.case_data, name='接口参数')
        response = requests.post(url=case.url, data=eval(case.case_data))
        res = response.json()  # 把响应结果转换成字典
        allure.attach(body=str(res), name='响应结果')
        try:
            assert eval(case.expect) == res
        except AssertionError as e:
            ReadExcel.write_data('./cases.xlsx', 'Login', case.case_id, 7, '失败')
            logger.error("测试编号{},测试用例标题{},执行失败！实际结果是{}".format(case.case_id, case.case_title, res))
            logger.exception(e)
            raise e  # 由于使用了异常捕捉，会导致pytest框架去捕捉异常时，会捕捉不到，所以我们需要再次将异常抛出
        else:
            ReadExcel.write_data('./cases.xlsx', 'Login', case.case_id, 7, '成功')
            logger.info("测试编号{},测试用例标题{},执行成功！".format(case.case_id, case.case_title))


if __name__ == '__main__':
    pytest.main(["--alluredir", './report/allure_json', '--clean-alluredir', './test_login.py'])
    os.system('allure generate report/allure_json -o report/allure_report --clean')

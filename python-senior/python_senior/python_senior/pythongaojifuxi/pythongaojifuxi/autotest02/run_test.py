"""
---------------------------------
作者: 星光_黄宗泽
创建时间: 2022/9/4-16:50
知识点: 
---------------------------------
"""
import pytest, os

if __name__ == '__main__':
    # 生成json的结果报告 存放在./resports/allure_json
    pytest.main(['--alluredir', './resports/allure_json', './testcase','--clean-alluredir'])
    # 将json的结果报告转化为html类型的结果报告
    os.system('allure generate ./resports/allure_json -o ./resports/allure_html --clean')

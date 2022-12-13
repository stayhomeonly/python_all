# coding=gbk

import logging
import time
import unittest



from BSTestRunner import BSTestRunner


# ָ�����������Ͳ��Ա����·��
test_dir = '../testcases'
report_dir = '../reports'

# ���ز�������
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_login.py')

# ���屨����ļ���ʽ
now = time.strftime("%Y-%m-%d %H_%M_%S")
report_name = report_dir + '/' + now + ' test_report.html'

# �������������ɲ��Ա���
with open(report_name, 'wb') as f:
    runner = BSTestRunner(stream=f, title="Kyb Test Report", description="kyb Andriod app Test Report")
    logging.info("start run testcase...")
    runner.run(discover)

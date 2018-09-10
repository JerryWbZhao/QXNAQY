#coding=utf-8
import re, os, math
import unittest, doctest
import HTMLTestRunner
from QXN import allcase_list

alltestnames = allcase_list.caselist()

suite = unittest.TestSuite()

if __name__ == '__main__':
# 这里我们可以使用defaultTestLoader.loadTestsFromNames(),
# 但如果不提供一个良好的错误消息时，它无法加载测试
# 所以我们加载所有单独的测试，这样将会提高脚本错误的确定。
    for test in alltestnames:
        try:
            #最关键的就是这一句，循环执行数据数的里的用例。
            suite.addTest(unittest.defaultTestLoader.loadTestsFromName(test))
        except Exception:
            print ('ERROR: Skipping tests from "%s".' % test)
            try:
                __import__(test)
            except ImportError:
                print ('Could not import the test module.')
            else:
                print ('Could not load the test suite.')
            from traceback import print_exc
            print_exc()
    print ('Running the tests...')
    
filename = 'D:\\QXNZ_Result_20180910.html'
fp = open(filename, 'wb')

runner =HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'黔西南安全云测试报告',
    description=u'报告描述')

runner.run(suite)
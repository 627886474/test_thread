# coding=utf-8

import unittest,os,time,sys
import multiprocessing
import HTMLTestRunner


#查找多有含有 thread 的文件，文件夹
def EEEcreatsuit():
    casedir=[]
    listaa=os.listdir('E:\\pyproject\\zefun\\test_case')
    for aa in listaa:
        if "thread" in aa:
            casedir.append(aa)
    print casedir

    suite=[]
    for n in casedir:
        testunit = unittest.TestSuite()
        discover = unittest.defaultTestLoader.discover(str(n),pattern='test*.py',top_level_dir=n)
        for test_suite in discover:
            for test_case in test_suite:
                testunit.addTests(test_case)
                print testunit
        suite.append(testunit)

    return suite,casedir

    # 多线程运行测试套件，将结果写入 HTMLTestRunner 报告
def EEmultiRunCase(suite, casedir):
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    filename = 'E:\\pyproject\\zefun'+now+'result.html'
    fp = file(filename, 'wb')
    proclist = []
    s = 0
    for i in suite:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=str(casedir[s])+u'测试报告',description=u'用例执行情况：')

        proc = multiprocessing.Process(target=runner.run,args=(i,))
        proclist.append(proc)
        s = s + 1
    for proc in proclist:proc.start()
    for proc in proclist:proc.join()
    fp.close()

if __name__ == '__main__':
    runtmp = EEEcreatsuit()
    EEmultiRunCase(runtmp[0],runtmp[1])


#
# def createsuite():
#     testunit = unittest.TestSuite()
#     # 定义测试文件查找的目录
#     test_dir='E:\\pyproject\\zefun\\test_case'
#
#     # 定义discover方法的参数
#     discover=unittest.defaultTestLoader.discover(
#         test_dir,
#         pattern='test*.py',
#         top_level_dir=None)
#
#     # discover方法筛选出来的用例（在test_dir目录下以test开头的文件），循环添加到测试套件中
#
#     for test_case in discover:
#         testunit.addTests(test_case)
#         print testunit
#     return testunit
#
# now = time.strftime("%Y-%m-%d %H_%M_%S")
# filename = 'E:\\pyproject\\zefun'+now+'result.html'
# fp = file(filename, 'wb')
# runner =HTMLTestRunner.HTMLTestRunner(
# stream=fp,
# title=u'百度搜索测试报告',
# description=u'用例执行情况')
#
# if __name__ == '__main__':
#     runner.run(createsuite())
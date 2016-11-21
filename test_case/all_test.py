# coding=utf-8

import unittest,os,time
import threading
import HTMLTestRunner


#查找多有含有 thread 的文件，文件夹
def Ecreatsuit():
    casedir=[]
    listaa=os.listdir('/Users/coco/work/pyproject/zefundev/test_case')
    for aa in listaa:
        if "thread" in aa:
            casedir.append(aa)

    suite=[]
    for n in casedir:
        testunit = unittest.TestSuite()
        discover = unittest.defaultTestLoader.discover(n,pattern='test*.py',top_level_dir=n)
        for test_suite in discover:
            for test_case in test_suite:
                testunit.addTests(test_case)
        suite.append(testunit)

    return suite,casedir

    # 多线程运行测试套件，将结果写入 HTMLTestRunner 报告
def EmultiRunCase(suite, casedir):
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    filename = '/Users/coco/work/pyproject/zefundev/'+now+'result.html'
    fp = open(filename, 'wb')
    proclist = []
    s = 0
    for i in suite:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=str(casedir[s])+u'测试报告',description=u'用例执行情况：')

        proc = threading.Thread(target=runner.run,args=(i,))
        proclist.append(proc)
        s = s + 1
    for proc in proclist:proc.start()
    for proc in proclist:proc.join()
    fp.close()

if __name__ == '__main__':
    runtmp = Ecreatsuit()
    EmultiRunCase(runtmp[0],runtmp[1])



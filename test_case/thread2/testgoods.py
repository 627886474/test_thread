# coding=utf-8
import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
import login
from page_object.test_Receptionist import Receptionist
from page_object.BasePage import BasePage

class checkgoods(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('/Users/coco/Desktop/chromedriver')
        self.base_url="http://www.baidu.com"
        self.driver.implicitly_wait(30)
        self.driver.get(self.base_url)
        login.login(self)
        self.verificationErrors=[]
        self.accept_next_alert=True

        # 商品销售人员业绩值
        self.src1="return jQuery('[name=commissionCalculate]').val()"
        # 商品销售人员提成值
        self.src2 = "return jQuery('[name=commissionAmount]').val()"
        # 商品销售人员2的业绩值
        self.src3="return jQuery(jQuery('[name=commissionCalculate]')[1]).val()"
        # 商品销售人员2的提成值
        self.src4 = "return jQuery(jQuery('[name=commissionAmount]')[1]).val()"
        # 商品销售人员3的业绩值
        self.src5="return jQuery(jQuery('[name=commissionCalculate]')[2]).val()"
        # 商品销售人员3的提成值
        self.src6 = "return jQuery(jQuery('[name=commissionAmount]')[2]).val()"
        # 调出下拉框部门业绩的分配
        self.src7='jQuery("#tab2 [name=deptSelectValue]").val(95);jQuery("#tab2 [name=deptSelectValue]").trigger("change");'



    def test_goods1(self):
        u"""开单商品_001"""
        # 待测试商品编号为1
        self.commoditynumber='1'
        # 商品销售人员编号为1100
        self.salesman1number='1100'

        driver = Receptionist(self.driver,self.base_url)
        self.driver.implicitly_wait(30)
        driver.click_kaidan()
        time.sleep(1)
        driver.click_commodity()
        time.sleep(1)
        driver.input_commodity(self.commoditynumber)
        time.sleep(1)
        driver.input_salesman1(self.salesman1number)
        time.sleep(1)
        driver.click_accounts()
        time.sleep(1)
        text1 =driver.script(self.src1)
        print (text1)
        text2 = driver.script(self.src2)
        print (text2)
        self.assertEqual(text1, "400.00")
        self.assertEqual(text2, "40.00")
        time.sleep(1)
        driver.click_accounts2()
        time.sleep(1)

    def test_goods2(self):
        u"""开单商品_002"""
        # 待测试商品编号为1
        self.commoditynumber='1'
        # 销售人员1的编号
        self.salesman1number='1100'
        # 销售人员2的编号
        self.salesman2number='1205'
        # 销售人员3的编号
        self.salesman3number='3301'

        driver = Receptionist(self.driver,self.base_url)
        self.driver.implicitly_wait(30)
        time.sleep(1)
        driver.click_kaidan()
        time.sleep(1)
        driver.click_commodity()
        time.sleep(1)
        driver.input_commodity(self.commoditynumber)
        time.sleep(1)
        driver.input_salesman1(self.salesman1number)
        time.sleep(1)
        driver.input_salesman2(self.salesman2number)
        time.sleep(1)
        driver.input_salesman3(self.salesman3number)
        time.sleep(1)
        driver.click_accounts()
        time.sleep(1)
        text1 = driver.script(self.src1)
        print (text1)
        text2 = driver.script(self.src2)
        print (text2)
        text3 = driver.script(self.src3)
        print (text3)
        text4 = driver.script(self.src4)
        print (text4)
        text5 = driver.script(self.src5)
        print (text5)
        text6 = driver.script(self.src6)
        print (text6)
        # 设置断言比较销售人员的业绩与提成值是否与预期的一样
        self.assertEqual(text1, "200.00")
        self.assertEqual(text2, "20.00")
        self.assertEqual(text3, "120.00")
        self.assertEqual(text4, "12.00")
        self.assertEqual(text5, "80.00")
        self.assertEqual(text6, "8.00")
        time.sleep(1)
        driver.click_accounts2()
        time.sleep(1)

    def test_goods3(self):
        u"""开单商品_003"""
        # 会员
        self.member='123456'
        # 待测试商品编号为1
        self.commoditynumber='1'
        # 销售人员1的编号
        self.salesman1number='1100'


        driver = Receptionist(self.driver,self.base_url)
        self.driver.implicitly_wait(30)
        driver.click_kaidan()
        time.sleep(1)
        driver.click_commodity()
        time.sleep(1)
        driver.input_member(self.member)
        time.sleep(1)
        driver.click_member()
        time.sleep(1)
        driver.input_commodity(self.commoditynumber)
        time.sleep(1)
        driver.input_salesman1(self.salesman1number)
        time.sleep(1)
        driver.click_accounts()
        time.sleep(1)
        text1 = driver.script(self.src1)
        print (text1)
        text2 = driver.script(self.src2)
        print (text2)
        self.assertEqual(text1, "360.00")
        self.assertEqual(text2, "36.00")
        driver.click_accounts2()
        time.sleep(3)

    def test_goods4(self):
        u"""开单商品_004"""
        # 会员编号为
        self.member='123456'
        # 待测试商品编号为1
        self.commoditynumber='1'
        # 销售人员1的编号
        self.salesman1number='1100'
        # 销售人员2的编号
        self.salesman2number='1205'
        # 销售人员3的编号
        self.salesman3number='1205'


        driver = Receptionist(self.driver,self.base_url)
        self.driver.implicitly_wait(30)
        driver.click_kaidan()
        time.sleep(1)
        driver.click_commodity()
        time.sleep(1)
        driver.input_member(self.member)
        time.sleep(1)
        driver.click_member()
        time.sleep(1)
        driver.input_commodity(self.commoditynumber)
        time.sleep(1)
        driver.input_salesman1(self.salesman1number)
        time.sleep(1)
        driver.input_salesman2(self.salesman2number)
        time.sleep(1)
        driver.input_salesman3(self.salesman3number)
        time.sleep(1)
        driver.click_accounts()
        time.sleep(1)
        text1 = driver.script(self.src1)
        print (text1)
        text2 = driver.script(self.src2)
        print (text2)
        text3 = driver.script(self.src3)
        print (text3)
        text4 = driver.script(self.src4)
        print (text4)
        text5 = driver.script(self.src5)
        print (text5)
        text6 = driver.script(self.src6)
        print (text6)
        self.assertEqual(text1, "180.00")
        self.assertEqual(text2, "18.00")
        self.assertEqual(text3, "108.00")
        self.assertEqual(text4, "10.80")
        self.assertEqual(text5, "72.00")
        self.assertEqual(text6, "7.20")
        driver.click_accounts2()
        time.sleep(3)

    def test_goods5(self):
        u"""开单商品_005"""
        # 会员编号为
        self.member='123456'
        # 现金充值2000
        self.cash='2000'


        driver = Receptionist(self.driver,self.base_url)
        self.driver.implicitly_wait(30)
        driver.click_kaidan()
        time.sleep(1)
        driver.click_commodity()
        time.sleep(1)
        driver.input_member(self.member)
        time.sleep(1)
        driver.click_member()
        time.sleep(1)
        driver.click_recharge()
        time.sleep(1)
        driver.input_cash(self.cash)
        time.sleep(1)
        driver.script(self.src7)
        time.sleep(1)
        driver.click_rechargeaccount()
        time.sleep(1)




        # 对弹窗的异常处理
    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

        # 关闭警告以及对得到的文本框进行处理
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        # 对前面的verificationErrors方法获得的列表进行比较，输出报错信息

if __name__ == "__main__":
    unittest.main()


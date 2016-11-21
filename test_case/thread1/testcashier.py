# coding=utf-8
import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
import login
from case import cashier
from page_object.test_Receptionist import Receptionist


class checkstand(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('/Users/coco/Desktop/chromedriver')
        self.base_url="http://www.baidu.com/"
        self.driver.implicitly_wait(30)
        self.driver.get(self.base_url)
        login.login(self)
        # 获得第一个轮牌的业绩值
        self.src1="return jQuery('[name=commissionCalculate]').val()"
        # 获得第一个轮牌的提成值
        self.src2="return jQuery('[name=commissionAmount]').val()"
        # 获得第二个轮牌的业绩值
        self.src3="return jQuery(jQuery('[name=commissionCalculate]')[1]).val()"
        # 获得第二个轮牌的提成值
        self.src4="return jQuery(jQuery('[name=commissionAmount]')[1]).val()"
        # 获得第三个轮牌的业绩值
        self.src5="return jQuery(jQuery('[name=commissionCalculate]')[2]).val()"
        # 获得第三个轮牌的提成值
        self.src6="return jQuery(jQuery('[name=commissionAmount]')[2]).val()"
        self.verificationErrors=[]
        self.accept_next_alert=True


    def test_shouyin1(self):
        u"""开单项目_001"""
        # 开单项目编号
        self.projectnumber='11104'
        # 第1个服务人员编号
        self.server1number='1100'

        driver = Receptionist(self.driver,self.base_url)
        self.driver.implicitly_wait(30)
        time.sleep(1)
        driver.click_kaidan()
        time.sleep(1)
        driver.input_project(self.projectnumber)
        time.sleep(2)
        driver.input_server1(self.server1number)
        time.sleep(2)
        driver.click_accounts()
        time.sleep(3)
        text1 = driver.script(self.src1)
        print (text1)
        text2 = driver.script(self.src2)
        print (text2)
        self.assertEqual(text1, "12.50")
        self.assertEqual(text2, "10.00")
        driver.click_accounts2()
        time.sleep(1)

    def test_shouyin2(self):
        u"""开单项目_002"""
        self.projectnumber='11105'
        self.server1number='1206'
        self.server2number='1103'
        # 修改项目价格
        self.projectprice='58'

        driver = Receptionist(self.driver,self.base_url)
        self.driver.implicitly_wait(30)
        time.sleep(1)
        driver.click_kaidan()
        time.sleep(1)
        driver.input_project(self.projectnumber)
        time.sleep(1)
        driver.input_server1(self.server1number)
        time.sleep(1)
        driver.input_server2(self.server2number)
        time.sleep(1)
        driver.click_accounts()
        time.sleep(1)
        driver.input_price(self.projectprice)
        time.sleep(1)
        driver.click_rechagecash()
        time.sleep(1)
        text1 = driver.script(self.src1)
        print (text1)
        text2 = driver.script(self.src2)
        print (text2)
        text3 = driver.script(self.src3)
        print (text3)
        text4 = driver.script(self.src4)
        print (text4)
        self.assertEqual(text1, "20.00")
        self.assertEqual(text2, "7.00")
        self.assertEqual(text3, "28.00")
        self.assertEqual(text4, "7.35")
        driver.click_accounts2()
        time.sleep(1)

    def test_shouyin3(self):
        u"""开单项目_003"""
        self.projectnumber='11115'
        self.server1number='1207'
        self.server2number='3301'
        self.server3number='1101'


        driver = Receptionist(self.driver,self.base_url)
        self.driver.implicitly_wait(30)
        time.sleep(1)

        driver.click_kaidan()
        time.sleep(1)
        driver.input_project(self.projectnumber)
        time.sleep(1)
        driver.input_server1(self.server1number)
        time.sleep(1)
        driver.input_server2(self.server2number)
        time.sleep(1)
        driver.input_server3(self.server3number)
        time.sleep(1)
        driver.click_accounts()
        time.sleep(1)
        text1 = driver.script(self.src1)
        print (text1)
        text2 = driver.script(self.src2)
        print (text2)
        text3 = driver.script(self.src3)
        print (text3)
        text4 =driver.script(self.src4)
        print (text4)
        text5 = driver.script(self.src5)
        print (text5)
        text6 = driver.script(self.src6)
        print (text6)
        self.assertEqual(text1, "10.00")
        self.assertEqual(text2, "8.00")
        self.assertEqual(text3, "94.40")
        self.assertEqual(text4, "7.78")
        self.assertEqual(text5, "118.00")
        self.assertEqual(text6, "38.50")
        driver.click_accounts2()
        time.sleep(1)

    def test_shouyin4(self):
        u"""开单项目_004"""
        self.member='123456'
        self.projectnumber = '11101'
        self.server1number='1100'


        driver = Receptionist(self.driver,self.base_url)
        self.driver.implicitly_wait(30)
        time.sleep(1)
        driver.click_kaidan()
        time.sleep(1)
        driver.input_member(self.member)
        time.sleep(1)
        driver.click_member()
        time.sleep(1)
        driver.input_project(self.projectnumber)
        time.sleep(1)
        driver.input_server1(self.server1number)
        time.sleep(1)
        driver.click_accounts()
        time.sleep(1)
        text1 = driver.script(self.src1)
        print (text1)
        text2 = driver.script(self.src2)
        print (text2)
        self.assertEqual(text1, "30.00")
        self.assertEqual(text2, "10.50")
        driver.click_accounts2()
        time.sleep(1)

    def test_shouyin5(self):
        u"""开单项目_005"""
        self.member='123456'
        self.projectnumber='11105'
        self.server1number='1206'
        self.server2number='1103'
        self.projectprice='56.2'

        driver = Receptionist(self.driver,self.base_url)
        self.driver.implicitly_wait(30)
        time.sleep(1)

        driver.click_kaidan()
        time.sleep(1)
        driver.input_member(self.member)
        time.sleep(1)
        driver.click_member()
        time.sleep(1)
        driver.input_project(self.projectnumber)
        time.sleep(1)
        driver.input_server1(self.server1number)
        time.sleep(1)
        driver.input_server2(self.server2number)
        time.sleep(1)
        driver.click_accounts()
        time.sleep(1)
        driver.input_price(self.projectprice)
        time.sleep(1)
        driver.click_cardcash()
        time.sleep(1)
        text1 = driver.script(self.src1)
        print (text1)
        text2 = driver.script(self.src2)
        print (text2)
        text3 = driver.script(self.src3)
        print (text3)
        text4 = driver.script(self.src4)
        print (text4)
        self.assertEqual(text1, "20.00")
        self.assertEqual(text2, "7.00")
        self.assertEqual(text3, "26.20")
        self.assertEqual(text4, "6.72")
        driver.click_accounts2()
        time.sleep(1)

    def test_shouyin6(self):
        u"""开单项目_006"""
        self.member='123456'
        self.projectnumber='11115'
        self.server1number='1206'
        self.server2number='3301'
        self.server3number='1100'
        self.projectprice='56.2'

        driver = Receptionist(self.driver,self.base_url)
        self.driver.implicitly_wait(30)
        time.sleep(1)

        driver.click_kaidan()
        time.sleep(1)
        driver.input_member(self.member)
        time.sleep(1)
        driver.click_member()
        time.sleep(1)
        driver.input_project(self.projectnumber)
        time.sleep(1)
        driver.input_server1(self.server1number)
        time.sleep(1)
        driver.input_server2(self.server2number)
        time.sleep(1)
        driver.input_server3(self.server3number)
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
        self.assertEqual(text1, "10.00")
        self.assertEqual(text2, "8.00")
        self.assertEqual(text3, "94.40")
        self.assertEqual(text4, "7.78")
        self.assertEqual(text5, "118.00")
        self.assertEqual(text6, "38.50")
        driver.click_accounts2()
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



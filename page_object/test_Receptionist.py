# coding=utf-8

from selenium.webdriver.common.by import By

from BasePage import BasePage


# 继承BasePage类
class Receptionist(BasePage):

    # 开单按钮
    submit_kaidan = (By.LINK_TEXT, u'收银开卡')
    # 商品按钮
    submit_commodity=(By.XPATH,'//li[2]/span')
    # 会员搜索按钮
    submit_member=(By.XPATH,'//*[@id="Membersearch"]/div[1]/div/div/div[1]/button')
    # 充值按钮
    submit_recharge=(By.XPATH,'//li[6]/span')
    # 开单并结账按钮
    submit_accounts=(By.XPATH,'//*[@id="kaidan"]/div[2]/div/input')
    # 弹出框的结账按钮
    submit_accounts2=(By.XPATH,'//*[@id="pay"]')
    # 充值并结账按钮
    submit_rechargeaccount=(By.XPATH,'//*[@id="tab2"]/div/div[10]/button')



    # 充值现金输入框
    inputbox_cash=(By.XPATH,'//*[@id="tab2"]/div/div[4]/div[1]/input')
    # 会员输入框
    inputbox_member=(By.ID,'searchBox')
    # 项目编号输入框
    inputbox_project=(By.XPATH,'//*[@id="projecttxt"]')
    # 项目服务人员1
    inputbox_server1=(By.XPATH,'//*[@id="pjtable"]/td[4]/table/tbody/tr/td[1]/input')
    # 项目服务人员2
    inputbox_server2=(By.XPATH,'//*[@id="pjtable"]/td[5]/table/tbody/tr/td[1]/input')
    # 项目服务人员3
    inputbox_server3=(By.XPATH,'//*[@id="pjtable"]/td[6]/table/tbody/tr/td[1]/input')



    # 商品编号输入框
    inputbox_commodity=(By.XPATH,'//*[@id="goodstxt"]')
    # 商品销售人员1编号输入框
    inputbox_salesman1=(By.XPATH,'//*[@id="goods"]/div/div/table/tbody/tr/td[5]/input')
    # 商品销售人员2编号输入框
    inputbox_salesman2=(By.XPATH,'//*[@id="goods"]/div/div/table/tbody/tr/td[6]/input')
    # 商品销售人员3编号输入框
    inputbox_salesman3=(By.XPATH,'//*[@id="goods"]/div/div/table/tbody/tr/td[7]/input')

    # 项目售价输入框
    inputbox_price=(By.XPATH,'//*[@id="tbody-datainfo"]/tr[1]/td[4]/input')
    # 结账方式现金输入框
    inputbox_rechagecash=(By.XPATH,'//*[@id="cashAmount"]')
    # 结账方式卡金输入框
    inputbox_cardcash=(By.XPATH,'//*[@id="cardpayAmount"]')





    # 打开网页
    def open(self):
        # 调用page中的_open打开连接
        self._open(self.base_url)

    # 调用submit_kaidan对象，点击开单
    def click_kaidan(self):
        self.find_element(*self.submit_kaidan).click()

    # 点击商品
    def click_commodity(self):
        self.find_element(*self.submit_commodity).click()

    # 点击会员搜索按钮
    def click_member(self):
        self.find_element(*self.submit_member).click()

    # 点击充值按钮
    def click_recharge(self):
        self.find_element(*self.submit_recharge).click()

    # 点击充值并结账按钮
    def click_rechargeaccount(self):
        self.find_element(*self.submit_rechargeaccount).click()

    # 点击结账方式现金输入框，修改售价后，结账方式这里的值应该会自动变化的
    def click_rechagecash(self):
        self.find_element(*self.inputbox_rechagecash).click()

    # 点击结账方式现金输入框，修改售价后，结账方式这里的值应该会自动变化的
    def click_cardcash(self):
        self.find_element(*self.inputbox_cardcash).click()


    # 输入现金输入框
    def input_cash(self,cash):
        self.find_element(*self.inputbox_cash).clear()
        self.find_element(*self.inputbox_cash).send_keys(cash)

    # 输入会员信息
    def input_member(self,member):
        self.find_element(*self.inputbox_member).clear()
        self.find_element(*self.inputbox_member).send_keys(member)

    # 输入项目编号
    def input_project(self,projectnumber):
        self.find_element(*self.inputbox_project).clear()
        self.find_element(*self.inputbox_project).send_keys(projectnumber)

    # 输入第1个服务人员编号
    def input_server1(self,server1number):
        self.find_element(*self.inputbox_server1).clear()
        self.find_element(*self.inputbox_server1).send_keys(server1number)

    # 输入第2个服务人员编号
    def input_server2(self,server2number):
        self.find_element(*self.inputbox_server2).clear()
        self.find_element(*self.inputbox_server2).send_keys(server2number)

    # 输入第3个服务人员编号
    def input_server3(self,server3number):
        self.find_element(*self.inputbox_server3).clear()
        self.find_element(*self.inputbox_server3).send_keys(server3number)



    # 输入商品编号
    def input_commodity(self,commoditynumber):
        self.find_element(*self.inputbox_commodity).clear()
        self.find_element(*self.inputbox_commodity).send_keys(commoditynumber)

    # 输入第1个销售人员编号
    def input_salesman1(self,salesman1number):
        self.find_element(*self.inputbox_salesman1).clear()
        self.find_element(*self.inputbox_salesman1).send_keys(salesman1number)

    # 输入第2个销售人员编号
    def input_salesman2(self,salesman2number):
        self.find_element(*self.inputbox_salesman2).clear()
        self.find_element(*self.inputbox_salesman2).send_keys(salesman2number)

    # 输入第3个销售人员编号
    def input_salesman3(self,salesman3number):
        self.find_element(*self.inputbox_salesman3).clear()
        self.find_element(*self.inputbox_salesman3).send_keys(salesman3number)

    # 输入项目售价
    def input_price(self,projectprice):
        self.find_element(*self.inputbox_price).clear()
        self.find_element(*self.inputbox_price).send_keys(projectprice)



    # 点击开单结账按钮
    def click_accounts(self):
        self.find_element(*self.submit_accounts).click()

    # 点击弹出框的结账按钮
    def click_accounts2(self):
        self.find_element(*self.submit_accounts2).click()







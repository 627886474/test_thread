# coding=utf-8
import time

def shouyin1(self):
    # 散客开项目
    driver = self.driver
    driver.find_element_by_name("kaidan").click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="tabs"]/div[1]/div/div[1]/ul/li[2]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="pjtable"]/td[4]/table/tbody/tr/td[1]/input').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="pjStaff"]/div/div/div/div/ul/li[1]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="kaidan"]/div[2]/div/input').click()
    time.sleep(5)

def shouyin2(self):
    # 自助收银
    driver = self.driver
    driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[2]/ul[1]/li[1]/a').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="thead-body"]/tr[1]/td[7]/div[3]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="pay"]').click()
    time.sleep(3)
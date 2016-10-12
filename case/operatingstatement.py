# coding=utf-8
import time

def summary(self):
    # 门店汇总
    driver=self.driver
    driver.find_element_by_link_text(u"营业报表").click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="custom-toolbar"]/div/div/span[1]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="custom-toolbar"]/div/div/span[2]').click()
    time.sleep(3)


def membership(self):
    driver = self.driver
    driver.find_element_by_link_text(u"营业报表").click()
    time.sleep(3)
    driver.find_element_by_link_text(u"卡项销售").click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="custom-toolbar"]/div/div/span[1]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="custom-toolbar"]/div/div/span[2]').click()
    time.sleep(3)


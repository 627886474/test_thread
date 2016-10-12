# coding=utf-8
import time

def search1(self):
    # 散客开项目
    driver = self.driver
    driver.find_element_by_xpath("/html/body/div[1]/div[4]/div[2]/ul[1]/li[5]/a").click()
    time.sleep(3)

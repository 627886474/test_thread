# coding=utf-8
from time import sleep
from selenium import webdriver
import time
import multiprocessing


def check(self):
    driver = webdriver.Chrome()
    driver.get("http://test.maywant.com/zefun/")
    driver.maximize_window()
    time.sleep(1)
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys("123456")
    time.sleep(1)
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys("123456")
    driver.find_element_by_class_name("loginButton").click()
    time.sleep(5)
    driver.find_element_by_link_text(u"营业报表").click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="custom-toolbar"]/div/div/span[1]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="custom-toolbar"]/div/div/span[2]').click()
    time.sleep(3)



def pay(self):

    driver = webdriver.Chrome()
    driver.get("http://test.maywant.com/zefun/")
    driver.maximize_window()
    time.sleep(1)
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys("huazhong")
    time.sleep(1)
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys("123456")
    driver.find_element_by_class_name("loginButton").click()
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[2]/ul[1]/li[1]/a').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="thead-body"]/tr[1]/td[7]/div[3]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="pay"]').click()
    time.sleep(3)


threads = []
t1 = multiprocessing.Process(target=check, args=(u'1',))
threads.append(t1)
t2 = multiprocessing.Process(target=pay, args=(u'2',))
threads.append(t2)

if __name__ == '__main__':

    for i in threads:
        i.start()
    # keep thread
    for i in threads:
        i.join()


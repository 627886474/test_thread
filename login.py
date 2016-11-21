# coding=utf-8
import time

# 登录操作
def login(self):

    driver = self.driver
    driver.set_window_size(1500, 1000)
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys("123456")
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys("123456")
    self.driver.find_element_by_class_name("loginButton").click()
    time.sleep(2)



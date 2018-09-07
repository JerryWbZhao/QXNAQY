#coding=utf-8
'''
Created on 2018年8月24日
@author: Jerry
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, os
import HTMLTestRunner
class ZFJC1(unittest.TestCase):
    def setUp(self):
        chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:7070/platform"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    #政府登录用例
    def test_ZFJC1(self):
        u"""进入煤矿执法检查"""
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.find_element_by_xpath("//*[@id='username']").send_keys("qxnzajj")
        driver.find_element_by_xpath("//*[@id='password']").send_keys("123456")
        driver.find_element_by_xpath("//*[@id='fm11']/button").click()
        time.sleep(2)
        # 获取当前窗口handle name
        current_window = driver.current_window_handle
        driver.find_element_by_xpath("//*[@id='firstmenu']/li[3]/a").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='leftMenu']/li[3]/a").click()
        driver.find_element_by_xpath("//*[@id='leftMenu']/li[3]/ul/li[2]/a").click()
        driver.find_element_by_xpath("//*[@id='leftMenu']/li[3]/ul/li[2]/ul/li[1]/a").click()
        # 获取所有窗口handle name
        all_windows = driver.window_handles  # 获取所有窗口handle name
        # 切换window，如果window不是当前window，则切换到该window
        for window in all_windows:
            if window != current_window:
                driver.switch_to_window(window)
                time.sleep(2)
                #进入待办事项
                driver.find_element_by_xpath("//*[@id='leftMenu']/li[2]/a").click()
                time.sleep(2)
                #进入年度检查计划
                driver.find_element_by_xpath("//*[@id='leftMenu']/li[3]/a").click()
                driver.find_element_by_xpath("//*[@id='leftMenu']/li[3]/ul/li/a").click()
                time.sleep(2)
                #进入现场检查方案
                driver.find_element_by_xpath("//*[@id='leftMenu']/li[4]/a").click()
                driver.find_element_by_xpath("//*[@id='leftMenu']/li[4]/ul/li[1]/a").click()
                time.sleep(2)
                #进入现场监督检查
                driver.find_element_by_xpath("//*[@id='leftMenu']/li[4]/ul/li[2]/a").click()
                time.sleep(2)
                #进入执法档案
                driver.find_element_by_xpath("//*[@id='leftMenu']/li[5]/a").click()
                time.sleep(2)
                #进入执法库查询
                driver.find_element_by_xpath("//*[@id='leftMenu']/li[6]/a").click()
                time.sleep(2)
                #进入文书统计
                driver.find_element_by_xpath("//*[@id='leftMenu']/li[7]/a").click()
                driver.find_element_by_xpath("//*[@id='leftMenu']/li[7]/ul/li[1]/a").click()
                time.sleep(2)
                #进入违法违规
                driver.find_element_by_xpath("//*[@id='leftMenu']/li[7]/ul/li[2]/a").click()
                time.sleep(2)
                #进入执法人员
                driver.find_element_by_xpath("//*[@id='leftMenu']/li[7]/ul/li[3]/a").click()
                time.sleep(2)
                #进入现场处理
                driver.find_element_by_xpath("//*[@id='leftMenu']/li[7]/ul/li[4]/a").click()
                time.sleep(2)
                #进入一般隐患
                driver.find_element_by_xpath("//*[@id='leftMenu']/li[7]/ul/li[5]/a").click()
                time.sleep(2)
                #进入重大隐患
                driver.find_element_by_xpath("//*[@id='leftMenu']/li[7]/ul/li[6]/a").click()
                time.sleep(2)
                driver.find_element_by_xpath("//*[@id='leftMenu']/li[7]/a").click()
                time.sleep(2)
                #进入文书查询
                driver.find_element_by_xpath("//*[@id='leftMenu']/li[8]/a").click()
                time.sleep(2)
                #进入执法人员管理
                driver.find_element_by_xpath("//*[@id='leftMenu']/li[9]/a").click()
                driver.find_element_by_xpath("//*[@id='leftMenu']/li[9]/ul/li/a").click()
                time.sleep(2)
                
        
        driver.close()
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(ZFJC1("test_ZFJC1"))
    results = unittest.TextTestRunner().run(suite)    
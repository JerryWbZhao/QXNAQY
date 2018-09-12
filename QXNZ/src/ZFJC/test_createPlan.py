#coding=utf-8
'''
Created on 2018年9月11日
@author: Jerry
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, os
import HTMLTestRunner
class createPlan(unittest.TestCase):
    def setUp(self):
        chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:7070/platform"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    #创建检查计划用例
    def test_createPlan(self):
        u"""创建检查计划"""
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.find_element_by_xpath("//*[@id='username']").send_keys("qxnzajj")
        driver.find_element_by_xpath("//*[@id='password']").send_keys("123456")
        driver.find_element_by_xpath("//*[@id='fm11']/button").click()
        driver.implicitly_wait(30)
        # 获取当前窗口handle name
        current_window = driver.current_window_handle
        driver.find_element_by_xpath("//*[@id='firstmenu']/li[3]/a").click()
        time.sleep(5)
        driver.find_element_by_xpath("//*[@id='leftMenu']/li[3]/a").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='leftMenu']/li[3]/ul/li[2]/a").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='leftMenu']/li[3]/ul/li[2]/ul/li[1]/a").click()
        # 获取所有窗口handle name
        all_windows = driver.window_handles
        # 切换window，如果window不是当前window，则切换到该window
        for window in all_windows:
            if window != current_window:
                driver.switch_to_window(window)
                time.sleep(2)
                #进入年度检查计划
                driver.find_element_by_xpath("//*[@id='leftMenu']/li[3]/a").click()
                driver.find_element_by_xpath("//*[@id='leftMenu']/li[3]/ul/li/a").click()
                driver.implicitly_wait(30)
                #创建年度检查计划
                driver.find_element_by_xpath("//*[@id='btn_add']").click()
                driver.implicitly_wait(30)
                driver.find_element_by_xpath("//*[@id='fanf']").click()
                driver.implicitly_wait(30)
                driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[3]/table/tbody/tr/td/span[9]").click()
                driver.implicitly_wait(30)
                driver.find_element_by_xpath("//*[@id='sbrq']").click()
                driver.implicitly_wait(30)
                driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[7]").click()
                driver.implicitly_wait(30)
                sel1 = driver.find_element_by_xpath("//*[@id='selected-xzzfhy']")
                Select(sel1).select_by_value('7')
                driver.implicitly_wait(30)
                driver.find_element_by_xpath("//*[@id='jhjcqysl']").send_keys("10")
                driver.find_element_by_xpath("//*[@id='fafj']/button").click()
                time.sleep(2)
                driver.find_element_by_xpath("//*[@id='fileupload']/div[1]/div[1]/span").click()
                time.sleep(2)
                #调用upfile.exe上传程序
                os.system("D:\\upfile.exe")
                time.sleep(2)
                driver.find_element_by_xpath("//*[@id='fileupload']/div[1]/div[2]/button").click()
                time.sleep(2)              
                driver.find_element_by_xpath("//*[@id='addxzzffa']/span").click()
                time.sleep(2)
                driver.find_element_by_xpath("//*[@id='table_xzzffa']/tbody/tr[2]/td[8]/a[2]").click()
                time.sleep(2)
                driver.find_element_by_xpath("//*[@id='addXzzfxxjh']").click()
                time.sleep(2)
                driver.find_element_by_xpath("//*[@id='flfgxx_search_btn']").click()
                time.sleep(2)
                driver.find_element_by_xpath("//*[@id='qyxx_table']/div[1]/span").click()
                time.sleep(2)
                driver.find_element_by_xpath("//*[@id='saveBtn']").click()
                time.sleep(2)
                #返回列表删除计划
                driver.find_element_by_xpath("//*[@id='go-back']").click()
                time.sleep(2)
                driver.find_element_by_xpath("//*[@id='table_xzzffa']/tbody/tr[2]/td[1]/input").click()
                time.sleep(2)
                driver.find_element_by_xpath("//*[@id='deleteBtn']").click()
                time.sleep(2)
                driver.find_element_by_xpath("//*[@type='dialog']/div[3]/a[1]").click()
                time.sleep(2)
        
        driver.close()
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(createPlan("test_createPlan"))
    results = unittest.TextTestRunner().run(suite)    
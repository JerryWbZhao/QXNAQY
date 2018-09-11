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
from selenium.webdriver.common.action_chains import ActionChains

import unittest, time, re, os
import HTMLTestRunner
class createProject(unittest.TestCase):
    def setUp(self):
        chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:7070/platform"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    #办理检查方案用例
    def test_createProject(self):
        u"""办理检查方案"""
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
        time.sleep(3)
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
                #进入现场监督检查
                driver.find_element_by_xpath("//*[@id='leftMenu']/li[4]/a").click()
                driver.find_element_by_xpath("//*[@id='leftMenu']/li[4]/ul/li[2]/a").click()
                time.sleep(2)
                
                #文书管理
                driver.find_element_by_xpath("//*[@id='table_xczfjh']/tbody/tr/td[1]/input").click()
                driver.find_element_by_xpath("//*[@id='opwsgl_a']").click()
                time.sleep(2)
                driver.find_element_by_xpath("//*[@id='addzfws_a']").click()
                time.sleep(3)
                driver.find_element_by_xpath("//*[@id='zfwsForm']/div/div[1]/div[1]/span").click()
                time.sleep(3)
                driver.find_element_by_xpath("//*[@id='addBtn']").click()
                time.sleep(2)
                driver.find_element_by_xpath("//*[@id='leftMenu']/li[4]/ul/li[2]/a").click()                
                time.sleep(2)
               
                #办结方案
                driver.find_element_by_xpath("//*[@id='table_xczfjh']/tbody/tr/td[1]/input").click()
                driver.find_element_by_xpath("//*[@id='clkbj_a']").click()
                time.sleep(2)
                driver.find_element_by_xpath("//*[@type='dialog']/div[2]/a[1]").click()
                time.sleep(2)
                
                
        
        driver.close()
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(createProject("test_createProject"))
    results = unittest.TextTestRunner().run(suite)    
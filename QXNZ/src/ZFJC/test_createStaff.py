#coding=utf-8

'''
Created on 2018年9月12日
@author: Jerry
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re, os

class createStaff(unittest.TestCase):
    def setUp(self):
        chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:7070/platform"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    #办理检查方案用例
    def test_createStaff(self):
        u"""新增执法人员"""
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
        driver.refresh()
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
                
                #进入执法人员管理
                driver.find_element_by_xpath("//*[@id='leftMenu']/li[9]/a").click()
                driver.find_element_by_xpath("//*[@id='leftMenu']/li[9]/ul/li/a").click()
                time.sleep(2)
                
                #新增人员
                driver.find_element_by_xpath("//*[@id='container-viewer']/div[2]/div/div/div[1]/button[1]").click()
                time.sleep(2)
                driver.find_element_by_xpath("//*[@id='chooseUser']").click()
                time.sleep(2)
                driver.find_element_by_xpath("//*[@id='table_user']/tbody/tr[6]/td[1]/input").click()
                time.sleep(3)
                driver.find_element_by_xpath("//*[@id='user_modal']/div/div/div[3]/button[1]").click()
                time.sleep(3)
                driver.find_element_by_xpath("//*[@id='ajzfUserinfoFrom']/div/div[4]/div/input").send_keys("12345678")
                time.sleep(2)
                driver.find_element_by_xpath("//*[@id='ajzfUserinfoFrom']/div/div[6]/div/div/input").click()
                driver.implicitly_wait(30)
                driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[7]").click()
                driver.implicitly_wait(30)
                driver.find_element_by_xpath("//*[@id='ajzfUserinfoFrom']/div/div[7]/div/input").send_keys("黔西南州安监局")
                driver.implicitly_wait(30)
                driver.find_element_by_xpath("//*[@id='yxqQsrqStr']/input").click()
                driver.implicitly_wait(30)
                driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[7]").click()
                driver.implicitly_wait(30)
                driver.find_element_by_xpath("//*[@id='yxqJzrqStr']/input").click()
                driver.implicitly_wait(30)
                driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[7]").click()                
                driver.implicitly_wait(30)
                driver.find_element_by_xpath("//*[@id='addBtn']").click()
                time.sleep(2)
               
                #删除人员
                driver.find_element_by_xpath("//*[@id='leftMenu']/li[9]/ul/li/a").click()
                time.sleep(2)
                driver.find_element_by_xpath("//*[@id='table_userinfo']/tbody/tr[5]/td[1]/input").click()
                driver.find_element_by_xpath("//*[@id='container-viewer']/div[2]/div/div/div[1]/button[3]").click()
                time.sleep(2)
                driver.find_element_by_xpath("//*[@type='dialog']/div[3]/a[1]").click()
                time.sleep(2)
                
                
        
        driver.close()
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(createStaff("test_createStaff"))
    results = unittest.TextTestRunner().run(suite)    
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

class createProject(unittest.TestCase):
    def setUp(self):
        chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:7070/platform"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    #创建检查方案用例
    def test_createProject(self):
        u"""创建检查方案"""
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
                
                #进入现场检查方案
                driver.find_element_by_xpath("//*[@id='leftMenu']/li[4]/a").click()
                driver.find_element_by_xpath("//*[@id='leftMenu']/li[4]/ul/li[1]/a").click()
                time.sleep(2)
                
                #点击新增
                driver.find_element_by_xpath("//*[@id='addchose']").click()
                time.sleep(2)
                driver.find_element_by_xpath("//*[@id='add-xcjcfa']").click()
                time.sleep(2)
                
                #选择企业
                qy1=driver.find_element_by_xpath("//*[@id='dataform']/table/tbody/tr[1]/td[2]/input")
                ActionChains(driver).double_click(qy1).perform()
                time.sleep(2)
                driver.find_element_by_xpath("//*[@id='table_enterprise']/tbody/tr[1]/td[1]").click()
                driver.find_element_by_xpath("//*[@id='chooseEnt_btn']").click()
                time.sleep(2)
                
                #选择日期
                driver.find_element_by_xpath("//*[@id='dataform']/table/tbody/tr[4]/td[2]/input[1]").click()
                driver.implicitly_wait(30)
                driver.find_element_by_xpath("/html/body/div[5]/div[3]/table/tbody/tr[1]/td[7]").click()
                driver.implicitly_wait(30)
                driver.find_element_by_xpath("//*[@id='dataform']/table/tbody/tr[4]/td[2]/input[2]").click()
                driver.implicitly_wait(30)
                driver.find_element_by_xpath("/html/body/div[6]/div[3]/table/tbody/tr[1]/td[7]").click()
                driver.implicitly_wait(30)
                
                #选择检查人员
                ry1=driver.find_element_by_xpath("//*[@id='dataform']/table/tbody/tr[5]/td[2]/input")
                ActionChains(driver).double_click(ry1).perform()
                time.sleep(2)
                driver.find_element_by_xpath("//*[@id='table_user']/tbody/tr[1]/td[1]/input").click()
                driver.find_element_by_xpath("//*[@id='table_user']/tbody/tr[3]/td[1]/input").click()
                driver.find_element_by_xpath("//*[@id='user_modal']/div/div/div[3]/button[1]").click()
                time.sleep(2)
                
                #选择检查内容
                js = "window.scrollTo(0,500)" 
                driver.execute_script(js)
                nr1=driver.find_element_by_xpath("//*[@id='JianChaNeiRong']")
                ActionChains(driver).double_click(nr1).perform()
                time.sleep(2)
                driver.find_element_by_xpath("//*[@id='addDiv_aj']").click()
                time.sleep(2)
                driver.find_element_by_xpath("//*[@id='ztree-hy_5_span']").click()
                time.sleep(2)
                driver.find_element_by_xpath("//*[@id='treeDemo_1_switch']").click()
                driver.find_element_by_xpath("//*[@id='treeDemo_2_check']").click()
                driver.find_element_by_xpath("//*[@id='submit_btn']").click()
                time.sleep(2)
                driver.find_element_by_xpath("//*[@id='saveXczfjh_a']").click()
                time.sleep(2)
                
                #选择检查方式
                fs1=driver.find_element_by_xpath("//*[@id='dataform']/table/tbody/tr[7]/td[2]/input")
                ActionChains(driver).double_click(fs1).perform()
                time.sleep(2)
                driver.find_element_by_xpath("//*[@id='edit_modal']/div/div/div[2]/div/div[1]/input").click()
                driver.find_element_by_xpath("//*[@id='save_btn']").click()
                time.sleep(2)
                
                #提交审核
                js = "window.scrollTo(0,0)" 
                driver.execute_script(js)
                driver.find_element_by_xpath("//*[@id='container-viewer']/div[2]/div/div/div[1]/div[1]/div[2]").click()
                time.sleep(2)
                
                #审核通过
                driver.find_element_by_xpath("//*[@id='table_xczfjh']/tbody/tr[1]/td[8]/a").click()
                time.sleep(2)
                driver.find_element_by_xpath("//*[@id='spr']").send_keys("张阳")
                driver.find_element_by_xpath("//*[@id='agree']").click()
                time.sleep(2)
                
        
        driver.close()
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(createProject("test_createProject"))
    results = unittest.TextTestRunner().run(suite)    
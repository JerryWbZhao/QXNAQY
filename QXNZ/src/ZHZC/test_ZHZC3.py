#coding=utf-8

'''
Created on 2018年9月7日
@author: Jerry
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, os, random, gc

class ZHZC3(unittest.TestCase):
    def setUp(self):
        chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:7070/platform"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    #注册用例
    def test_ZHZC3(self):
        u"""考试培训机构注册"""
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.find_element_by_xpath("//*[@id='fm11']/div[4]/a[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='btnList']/a[3]").click()
        time.sleep(2)
        
        #搜索企业注册与否        
        s=random.randint(100000000000000000,999999999999999999)
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div[1]/input").send_keys(s)
        driver.find_element_by_xpath("//*[@id='regSearch']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='scroll-1']/table/tbody/tr[1]/td[2]/a").click()
        time.sleep(2)
        
        #填报第一步信息录入
        driver.find_element_by_xpath("//*[@id='tab1']/div[1]/div/div/input[1]").send_keys(s)
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='fullName']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='fullName']").send_keys("考试培训机构注册")
        
        #选择监管类型
        driver.find_element_by_xpath("//*[@id='JGLX']/a").click()
        driver.find_element_by_xpath("//*[@id='JGLX']/ul/li[1]/a").click()
        
        driver.find_element_by_xpath("//*[@id='shortName']").send_keys("考试")
        driver.find_element_by_xpath("//*[@id='contact']").send_keys("单位法人")
        driver.find_element_by_xpath("//*[@id='telephone']").send_keys("13000000000")
        
        #选择行业分类
        sel1 = driver.find_element_by_xpath("//*[@id='tab1']/div[8]/div/div/div/div[1]/select")
        Select(sel1).select_by_value('A')
        sel2 = driver.find_element_by_xpath("//*[@id='tab1']/div[8]/div/div/div/div[2]/select")
        Select(sel2).select_by_value('01')
        sel3 = driver.find_element_by_xpath("//*[@id='tab1']/div[8]/div/div/div/div[3]/select")
        Select(sel3).select_by_value('011')
        sel4 = driver.find_element_by_xpath("//*[@id='tab1']/div[8]/div/div/div/div[4]/select")
        Select(sel4).select_by_value('0111')
        
        #选择所在地区
        sel5 = driver.find_element_by_xpath("//*[@id='qyxzqh1']")
        Select(sel5).select_by_value('522300000000')
        sel6 = driver.find_element_by_xpath("//*[@id='qyxzqh2']")
        Select(sel6).select_by_value('522301000000')
        sel7 = driver.find_element_by_xpath("//*[@id='qyxzqh3']")
        Select(sel7).select_by_value('522301001000')
        
        driver.find_element_by_xpath("//*[@id='tab1']/div[10]/div/div/input").send_keys("黔西南")
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='submitButton']/a").click()
        
        #填报第二步信息录入
        driver.find_element_by_xpath("//*[@id='userName']").send_keys(s)
        driver.find_element_by_xpath("//*[@id='tab2']/div/div[2]/div/div/input").send_keys("黔西南")
        driver.find_element_by_xpath("//*[@id='passOne']").send_keys("123456")
        driver.find_element_by_xpath("//*[@id='passTwo']").send_keys("123456")
        driver.find_element_by_xpath("//*[@id='tab2']/div/div[5]/div/div/input").send_keys("13000000000")
        driver.find_element_by_xpath("//*[@id='tab2']/div/div[6]/div/div/input").send_keys("86000000")
        driver.find_element_by_xpath("//*[@id='tab2']/div/div[7]/div/div/input").send_keys("123")
        driver.find_element_by_xpath("//*[@id='tab2']/div/div[8]/div/div/input").send_keys("123@qq.com")
        driver.find_element_by_xpath("//*[@id='submitButton']/a").click()
        time.sleep(2)
        
        #填报第三步信息确认
        driver.find_element_by_xpath("//*[@id='submitButton']/a").click()
        time.sleep(2)      
        
        del s
        gc.collect()
        driver.close()
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(ZHZC3("test_ZHZC3"))
    results = unittest.TextTestRunner().run(suite)    
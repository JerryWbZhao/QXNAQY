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
import unittest, time, re, os, random, gc

class ZHZC1_2(unittest.TestCase):
    def setUp(self):
        chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:7070/platform"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    #注册用例
    def test_ZHZC1_2(self):
        u"""在已注册生产经营单位下创建账户"""
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.find_element_by_xpath("//*[@id='fm11']/div[4]/a[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='btnList']/a[1]").click()
        time.sleep(2)
        
        #搜索企业注册与否        
        s=random.randint(100000000000000000,999999999999999999)
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div[1]/input").send_keys("测试企业")
        driver.find_element_by_xpath("//*[@id='regSearch']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='scroll-1']/table/tbody/tr[2]/td[4]/a").click()
        time.sleep(2)
        
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
    suite.addTest(ZHZC1_2("test_ZHZC1_2"))
    results = unittest.TextTestRunner().run(suite)    
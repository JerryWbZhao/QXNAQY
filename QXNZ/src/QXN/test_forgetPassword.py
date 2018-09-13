#coding=utf-8
'''
Created on 2018年9月10日
@author: Jerry
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, os 

class Forget(unittest.TestCase):
    def setUp(self):
        chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:7070/platform"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    #找回密码用例
    def test_forgetPassword(self):
        u"""找回密码"""
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.find_element_by_xpath("//*[@id='fm11']/div[4]/a[2]").click()
        driver.implicitly_wait(30)
        
        #查询企业
        driver.find_element_by_xpath("//*[@id='scjydwjbxx']/a[2]/div/div[1]/input").send_keys("测试")
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='scjydwjbxx']/a[2]/div/div[1]/ul/li[1]").click()
        driver.implicitly_wait(30)
        driver.find_element_by_xpath("//*[@id='startFindPass']").click()
        driver.implicitly_wait(30)
        
        #找回密码
        driver.find_element_by_xpath("//*[@id='userTable']/tbody/tr/td[4]/button").click()
        driver.find_element_by_xpath("//*[@id='findPassForm']/div[1]/input").send_keys("mkqycs1")
        driver.find_element_by_xpath("//*[@id='findPassForm']/div[2]/input").send_keys("13000000000")
        driver.find_element_by_xpath("//*[@id='findPassForm']/div[3]/input").send_keys("123@qq.com")
        driver.find_element_by_xpath("//*[@id='findPassword']").click()
        driver.implicitly_wait(30)
        password = self.driver.find_element_by_xpath("//*[@id='layui-layer3']/div[2]").text
        self.assertEqual("找回成功：123456", password)          
        driver.find_element_by_xpath("//*[@id='layui-layer3']/div[3]/a").click()
        driver.implicitly_wait(30)
        driver.close()
        
    def tearDown(self):
        self.driver.quit()          
        self.assertEqual([], self.verificationErrors)
        
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Forget("test_forgetPassword"))
    results = unittest.TextTestRunner().run(suite)    
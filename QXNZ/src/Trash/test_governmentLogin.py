#coding=utf-8
'''
Created on 2018年7月16日
@author: Jerry
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, os
import HTMLTestRunner
class login(unittest.TestCase):
    def setUp(self):
        chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.base_url = "http://202.98.201.114:7070/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    #政府登录用例
    def test_government_login(self):
        u"""政府登录用例"""
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.implicitly_wait(30)
        driver.switch_to_frame("loginVue")
        driver.find_element_by_xpath("//*[@id='username']").send_keys("qxnzajj")
        driver.find_element_by_xpath("//*[@id='password']").send_keys("123456")
        driver.find_element_by_xpath("//*[@id='fm1']/div[2]/ul/li[3]/button").click()
        time.sleep(2)        
        driver.find_element_by_xpath("//*[@id='go-platform']").click()        
        time.sleep(3)
        try:
        #是一个无法找到的元素id
            driver.find_element_by_xpath("//*[@id='firstmenu']/li[1]/a")
        except:
            driver.get_screenshot_as_file("D:\\selenium_use_case\\error_png\\s_username.png")
        #如果没有找到上面的元素就截取当前页面。
        driver.close()
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(login("test_government_login"))
    results = unittest.TextTestRunner().run(suite)    
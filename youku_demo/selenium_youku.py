#!/usr/bin/env python
# encoding: utf-8
"""
@author: sunlava
@website: YouTubeTop100.com
@license: (C) Copyright 2013-2019, Muzhuangzhu
@contact: sunlava2046@gmail.com
@software: PyCharm
@file: selenium_youku.py
@time: 2019/12/24 22:56
@desc:
"""

import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


FILEPATH = 'h:\\youku_videos\\'


def login(driver):
    driver.get("https://cloud.youku.com/")
    #点击登录按钮
    driver.find_element_by_id("link_login").click()
    # 将焦点切换到当前页面弹出的警告，并获取弹出框的text
    alert = driver.switch_to_active_element()
    time.sleep(2)
    # 向输入框写内容
    driver.find_element_by_id("YT-ytaccount").send_keys("你的用户名")
    driver.find_element_by_id("YT-ytpassword").send_keys("你的密码")
    # 点击搜索按钮
    time.sleep(2)
    driver.find_element_by_id("YT-nloginSubmit").click()
    time.sleep(10)
def uploadFile(driver):
    #获得指定目录下的mp4文件
    mp4s = [i for i in os.listdir(FILEPATH) if i.split('.')[1][-3:] == 'mp4']
    url = 'http://cloud.youku.com/videos'
    if mp4s.__len__()>0:
        for mp4 in mp4s:
            if 0==mp4s.index(mp4):
                driver.get(url)
            else:
                js = 'window.open("{}");'.format(url)
                driver.execute_script(js)
                handles = driver.window_handles
                driver.switch_to.window(handles[mp4s.index(mp4)])
            driver.find_element_by_class_name("upload").click()
            time.sleep(2)
            WebDriverWait(driver, 10)
            driver.switch_to_frame("iframe_reload")
            time.sleep(5)
            WebDriverWait(driver, 10)
            doFile(driver, FILEPATH, mp4)
            time.sleep(20)
    else:
        print("没有可以上传的内容")


def doFile(driver,filePath,fileName):
    driver.find_element_by_id('selectfiles').send_keys(filePath+fileName)  # 定位上传按钮，定位本地文件
    time.sleep(2)
    driver.find_element_by_id("input01").send_keys(" python学习")
    time.sleep(2)
    driver.find_element_by_id("textarea").send_keys(" python学习")
    time.sleep(2)
    driver.find_element_by_id("input02").send_keys(" python学习")
    time.sleep(2)
    driver.find_element_by_id("postfiles").click()
    time.sleep(10)
    print("马上上传完毕.......")

def openNewTab(driver,url):
    # 新开一个窗口，通过执行js来新开一个窗口
    js = 'window.open("{}");'.format(url)
    browser = driver
    browser.execute_script(js)
    print(browser.current_window_handle)  # 输出当前窗口句柄
    handles = browser.window_handles  # 获取当前窗口句柄集合（列表类型）
    print(handles)  # 输出句柄集合
    for handle in handles:  # 切换窗口（切换到搜狗）
        if handle != browser.current_window_handle:
            print('switch to ', handle)
            browser.switch_to_window(handle)
            print(browser.current_window_handle)  # 输出当前窗口句柄（搜狗）
            break
    browser.close() #关闭当前窗口
    browser.switch_to_window(handles[0]) #切换回原窗口
    import time
    time.sleep(10)
    browser.quit()

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    # 开启无界面模式 正式运行的时候,可以这样搞
    #options.add_argument("--headless")  # 开启无界面模式
    #options.add_argument("--disable-gpu")  # 禁用gpu
    # options.set_headles() # 无界面模式的另外一种开启方式
    #使用代理
    #options.add_argument('--proxy-server=http://202.20.16.82:9527')  # 使用代理ip
    #替换UA
    #options.add_argument('--user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0')  # 替换User-Agent
    driver = webdriver.Chrome(chrome_options=options)
    driver.maximize_window()  # 最大化浏览器
    login(driver)
    uploadFile(driver)


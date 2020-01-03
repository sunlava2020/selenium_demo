#!/usr/bin/env python
# encoding: utf-8
"""
@author: Mu庄主
@website: u-union.com
@license: (C) Copyright 2013-2019, Mu庄主
@contact: sunlava2046@gmail.com
@software: PyCharm
@file: youtube_sub.py.py
@time: 2019/12/25 14:37
@desc:
"""
from selenium import webdriver
import time
import os
import shutil
import datetime

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from pysubs2 import SSAFile, SSAEvent, make_time


FILEPATH = 'd:\\srtDown\\' #需要修改为你自己的路径,这是字幕下载地址
NEWDIRPATH = 'd:\\srtDown\\1\\' #这个字幕处理时的临时文件夹
NEWTESTDIRPATH = 'd:\\srtDown\\2\\' #这个字幕处理时的临时文件夹

#根据下载地址和下载路径,进行下载 还是基于selenium库的
def down(url,filePath):
    options = webdriver.ChromeOptions()
    #指定下载路径
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': filePath}
    options.add_experimental_option('prefs', prefs)

    #开启无界面模式
    options.add_argument("--headless")  # 开启无界面模式
    options.add_argument("--disable-gpu")  # 禁用gpu
    # options.set_headles() # 无界面模式的另外一种开启方式
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)
    # 点击搜索按钮
    time.sleep(10)
    #根据内容查找元素,然后再找其哥哥元素,进行下载
    #print(driver.find_element_by_xpath('//span[contains(text(),"Chinese Simplified")]'))
    #下载英文
    driver.find_element_by_xpath('//span[contains(text(),"English")]/preceding-sibling::a[2]').click()
    time.sleep(10)
    newfilename1 = '1_.srt'
    # down(url,filePath)
    time.sleep(10)
    changFileName(filePath, NEWDIRPATH, newfilename1)
    #下载中文
    driver.find_element_by_xpath('//span[contains(text(),"Chinese Simplified")]/preceding-sibling::a[2]').click()
    time.sleep(10)
    newfilename2 = '2_.srt'
    # down(url,filePath)
    time.sleep(10)
    changFileName(filePath, NEWDIRPATH, newfilename2)
    time.sleep(10)
    driver.quit()

#修改文件名
def changFileName(olddirpath,newdirpath,newfilename):
    os.chdir(olddirpath)
    files = filter(os.path.isfile, os.listdir(olddirpath))
    files = [os.path.join(olddirpath, f) for f in files]  # add path to each file
    files.sort(key=lambda x: os.path.getmtime(x))
    newest_file = files[-1]
    os.rename(newest_file, newfilename)
    shutil.copy(os.path.join(olddirpath, newfilename), newdirpath)
    os.remove(os.path.join(olddirpath, newfilename))

    
#根据文件得到字幕list
def getalltext(filename):
    relustarray = []
    subs = SSAFile.load(filename)
    for line in subs:
        relustarray.append(line.text)
    return relustarray
    
#将两个srt文件合并(实现中英双语字幕)
def mergeSrt(filename,filename2,tofilename):
    aa = getalltext(filename)
    bb = getalltext(filename2)
    indexnumber = 0
    a = 1
    b = 2
    c = 3
    state = a
    text = ''
    index = ''
    timetxt = ''
    with open(filename, 'r',encoding='utf-8') as f:  # 打开srt字幕文件，并去掉文件开头的\ufeff
        for line in f.readlines():  # 遍历srt字幕文件
            if state == a:  # 跳过第一行
                index = line
                state = b
            elif state == b:  # 跳过第二行
                timetxt = line
                state = c
            elif state == c:  # 读取第三行字幕文本
                if len(line.strip()) != 0:
                    text += '' + line.strip()  # 将同一时间段的字幕文本拼接
                    text = aa[indexnumber]+"\n"+bb[indexnumber]
                    state = c
                elif len(line.strip()) == 0:
                    with open(tofilename, 'a',encoding='utf-8') as fa:  # 写入txt文本文件中
                        fa.write(index)
                        fa.write(timetxt)
                        fa.writelines(text.replace("\\N","\n")+"\n\n")
                        text = ''
                        state = a
                        indexnumber = indexnumber + 1
if __name__ == "__main__":
    #driver = webdriver.Chrome()
    #需要下载的youtube视频
    videoUrl = 'https://www.youtube.com/watch?v=wJ4hXGq0TV0'
    #这是一个youtube字幕下载网站的地址
    url = 'https://downsub.com/?url='+videoUrl
    down(url,NEWTESTDIRPATH)
    time.sleep(5)
    #将双语字幕合并
    mergeSrt(NEWDIRPATH+"1_.srt",NEWDIRPATH+"2_.srt",FILEPATH+"396.srt")
    time.sleep(1)

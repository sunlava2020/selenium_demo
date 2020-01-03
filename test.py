#!/usr/bin/env python
# encoding: utf-8
"""
@author: sunlava
@website: u-union.com
@license: (C) Copyright 2013-2019, 红叶湾酒店管理有限公司
@contact: sunlava@163.com
@software: PyCharm
@file: test.py
@time: 2020/1/2 16:16
@desc:
"""

import time
import os
FILEPATH = 'h:\\youku_videos\\'
NEWDIRPATH = 'h:\\youku_videos\\1\\'

if __name__ == '__main__':
    print("开始")
    aa = os.listdir(FILEPATH)
    bb=aa
    mp4s = [i for i in os.listdir(FILEPATH) if i.split('.')[1][-3:] == 'mp4']
    print(mp4s)
# python_work


selenium 安装:当然是pip了
pip install selenium

常见问题解答:
https://github.com/SeleniumHQ/selenium/wiki/Frequently-Asked-Questions



WebDriver 各浏览器驱动下载地址
Chrome
点击下载chrome的webdriver： http://chromedriver.storage.googleapis.com/index.html
你本机的chrome浏览器版本在菜单:帮助-->关于Google 里即可找到 或地址栏直接输入:chrome://settings/help 
不同的Chrome的版本对应的chromedriver.exe 版本也不一样，下载时不要搞错了。

Firefox
Firefox驱动下载地址为：https://github.com/mozilla/geckodriver/releases/
根据自己的操作系统下载对应的驱动即可，使用的话，需要把驱动的路径和火狐浏览器的路径加入到环境变量里面才可以

--------------------------------------华丽的分割线-----------------------------------------------
https://github.com/sunlava2020/selenium_demo/blob/master/youku_demo/selenium_youku.py
这个是利用selenium库批量上传视频文件,写这个代码的原因是,youku提供的api不能使用了,不然用api更合适


https://github.com/sunlava2020/selenium_demo/blob/master/youtube_demo/youtube_sub.py
这个是将某youtube视频的字幕下载下来,然后我们可以实现中英文双语合并操作
还是基于selenium库,通过解析下载一个youtube字幕下载站的数据,进行处理的,得到的字幕准确性有90%吧

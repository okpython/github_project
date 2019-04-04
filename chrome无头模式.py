#!/usr/bin/python
#coding=utf-8
# import sys
# reload(sys)
# setdefaultencoding("utf-8")
# 设置chrome浏览器的无头模式
# 使用了无头模式的话，就不用调出浏览器的界面
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("http://www.baidu.com")
content = driver.page_source
print(content)
driver.close()
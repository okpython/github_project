#!/usr/bin/python
#coding:utf-8

import datetime

def getYesterday():
    today = datetime.date.today()
    # days可以随便取值
    oneday = datetime.timedelta(days=1)
    yesterday = today-oneday
    return yesterday

yesterday = getYesterday()
"""
2019-03-24
<type 'datetime.date'>
"""
print(yesterday)
print(type(yesterday))
# 将datetime.date转为str
yesterday = datetime.datetime.strftime(yesterday, "%Y-%m-%d")
"""
2019-03-24
<type 'str'>
"""
print(yesterday)
print(type(yesterday))
# 将str转为datetime.date
yesterday=datetime.datetime.strptime(yesterday, "%Y-%m-%d")
"""
2019-03-24 00:00:00
<type 'datetime.datetime'>
"""
print(yesterday)
print(type(yesterday))
__author__ = 'Administrator'

import codecs
"""
读取txt文档，获取信息
"""
f = codecs.open("ninfo.txt", "r", "utf-8")
data = f.read()
f.close()
data = data.replace("},", "}")

dic_list = [eval(x) for x in data.split('\n')]

for i in dic_list:
    print(i["学号"] + "-" + i["姓名"] + "-" + i["导师姓名"])

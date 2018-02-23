__author__ = 'Administrator'
import re
from bs4 import BeautifulSoup

info ={}


def read(str):
    # soup = BeautifulSoup(open(str), "lxml")
    soup = BeautifulSoup(str, "lxml")
    tem = soup.body.table.table.contents
    info["毕业专业"] = tem[11].contents[3].string
    info["毕业学校"] = tem[13].contents[3].string
    info["科目一"] = tem[15].contents[3].string
    info["科目一分数"] = tem[15].contents[7].string
    info["科目二"] = tem[17].contents[3].string
    info["科目二分数"] = tem[17].contents[7].string
    info["科目三"] = tem[19].contents[3].string
    info["科目三分数"] = tem[19].contents[7].string
    info["科目四"] = tem[21].contents[3].string
    info["科目四分数"] = tem[21].contents[7].string
    # print(info)
    return info

# read("demo.html")
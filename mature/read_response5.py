__author__ = 'Administrator'
import re
from bs4 import BeautifulSoup

info ={}


def read(str):
    # soup = BeautifulSoup(open(str), "lxml")
    soup = BeautifulSoup(str, "lxml")
    tem = soup.body.table.table.contents
    info["性别"] = tem[5].contents[3].string
    info["证件号码"] = tem[7].contents[7].string
    info["政治面貌"] = tem[9].contents[3].string
    info["民族"] = tem[11].contents[3].string
    info["婚姻状况"] = tem[11].contents[7].string
    info["籍贯(省/直辖市)"] = tem[13].contents[7].string
    info["籍贯(市/县)"] = tem[15].contents[3].string
    info["生源所在地"] = tem[15].contents[7].string
    return info

# read("demo.html")
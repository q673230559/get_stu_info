__author__ = 'Administrator'
import re
from bs4 import BeautifulSoup

info ={}


def read(str):
    # soup = BeautifulSoup(open(str), "lxml")
    soup = BeautifulSoup(str, "lxml")
    tem = soup.body.table.table.tbody.contents
    info["导师姓名"] = tem[1].contents[1].string
    info["导师编号"] = tem[1].contents[3].string
    return info

# read("demo.html")
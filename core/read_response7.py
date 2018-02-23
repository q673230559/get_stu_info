__author__ = 'Administrator'
import re
from bs4 import BeautifulSoup

info ={}


def read(str):
    # soup = BeautifulSoup(open(str), "lxml")
    soup = BeautifulSoup(str, "lxml")
    tem = soup.body.table.table.contents
    info["家庭住址"] = tem[1].contents[3].input.attrs["value"]
    info["手机号码"] = tem[5].contents[7].input.attrs["value"]
    # print(info)
    return info

# read("demo.html")
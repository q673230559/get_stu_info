__author__ = 'Administrator'
import re
from bs4 import BeautifulSoup

info ={}

def read(str):
    soup = BeautifulSoup(str, "lxml")

    base = soup.table.table.tbody.contents
    info["学号"] = base[1].contents[3].string
    info["姓名"] = base[3].contents[3].string
    info["院系名称"] = base[11].contents[3].string
    info["专业名称"] = base[13].contents[3].string
    info["年级"] = base[19].contents[3].string
    info["学制"] = base[19].contents[7].string
    return info
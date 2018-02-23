# -*- coding: utf-8 -*-
# __author__ = 'Administrator'
import time

from core import get_info

start = 0
end = 0


def main(s, e):
    """
    起始学号s，结束学号e，遍历。
    模拟登录教务系统获取学生信息，
    写入到ninfo.txt文件中。
    """
    for i in range(s, e, 1):
        counts = 0
        mdic = get_info.get_info(i)
        print(i)
        while len(mdic) == 0 and counts < 3:
            mdic = get_info.get_info(i)
            counts += 1
        if len(mdic) != 0:
            time.sleep(1)
            print(mdic)
            ff = open("ninfo.txt", "a", encoding="utf-8")
            ff.write(mdic.__str__()+",\n")
            ff.close()

if __name__ == '__main__':
    main(start, end)
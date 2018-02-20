# -*- coding: utf-8 -*-
# __author__ = 'Administrator'

import http.cookiejar
import urllib.request
from urllib import parse
from urllib import request
import re
from bs4 import BeautifulSoup
import get_image
from mature import read_response4, read_response5, read_response6, read_response7, read_response8


def get_info(stu_code):
    """
    构建cookie对象,读取验证码，保存验证码cookie
    利用验证码cookie 模拟登录，保存登录后cookie
    利用登录后cookie 多次访问相关页面，获取并解析数据。
    """
    """
    核心代码涉及相关人员隐私，不公布，如有异议联系本人。
    """
    dic ={}
    return dic
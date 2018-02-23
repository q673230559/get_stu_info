# -*- coding: utf-8 -*-
# __author__ = 'Administrator'

import urllib
import http.cookiejar
import urllib.request

# 声明一个CookieJar对象实例来保存cookie
cookie = http.cookiejar.CookieJar()
# 利用urllib库中的request的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib.request.HTTPCookieProcessor(cookie)
# 通过handler来构建opener
opener = urllib.request.build_opener(handler)
# 此处的open方法同urllib的urlopen方法，也可以传入request
response = opener.open("http://yjs.ccnu.edu.cn/yjs/security/initDigitPicture.do?Rgb=255|255|255")

for i in cookie:
    print("Name = "+i.name)
    print("Value = "+i.value)
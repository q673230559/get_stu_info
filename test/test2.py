# -*- coding: utf-8 -*-
# __author__ = 'Administrator'

import sys
import io
import urllib.request
import http.cookiejar


#登录后才能访问的网页
url = 'http://localhost:8080/thesis/a/login'

#设置请求头
headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

#构造cookie
cookie = http.cookiejar.CookieJar()

#由cookie构造opener
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))

#构造访问请求
req = urllib.request.Request(url)

resp = opener.open(req)

print(resp.read().decode('utf-8'))
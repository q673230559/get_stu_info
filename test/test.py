# -*- coding: utf-8 -*-
# __author__ = 'Administrator'

import sys
import io
import urllib.request
import http.cookiejar

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8') #改变标准输出的默认编码



#登录时需要POST的数据
data = {"username":"51thesis",
        "password":"123456"}

post_data = urllib.parse.urlencode(data).encode('utf-8')

#设置请求头
headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

#登录时表单提交到的地址（用开发者工具可以看到）
# login_url = "http://localhost:8080/thesis/a/login"
login_url = "http://yjs.ccnu.edu.cn/yjs/"

#构造登录请求
req = urllib.request.Request(login_url, headers = headers, data = post_data)

#构造cookie
cookie = http.cookiejar.CookieJar()

#由cookie构造opener
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))

#发送登录请求，此后这个opener就携带了cookie，以证明自己登录过
resp = opener.open(req)

#登录后才能访问的网页
url = 'http://localhost:8080/thesis/a/sys/user/info'

#构造访问请求
req = urllib.request.Request(url, headers = headers)

resp = opener.open(req)

print(resp.read().decode('utf-8'))
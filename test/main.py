# -*- coding: utf-8 -*-
# __author__ = 'Administrator'

import requests

import get_image

# jpg_link = "http://yjs.ccnu.edu.cn/yjs/security/initDigitPicture.do?Rgb=255|255|255"  #图片链接
# request.urlretrieve(jpg_link, "111.jpg")
# get_image.getverify1("111.jpg")

codeurl = "http://yjs.ccnu.edu.cn/yjs/security/initDigitPicture.do?Rgb=255|255|255"
valcode = requests.get(codeurl)

f = open('valcode.png', 'wb')
# 将response的二进制内容写入到文件中
f.write(valcode.content)
# 关闭文件流对象
f.close()

code = get_image.getverify1("valcode.png")

print(code)


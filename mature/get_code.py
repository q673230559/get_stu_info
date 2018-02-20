# -*- coding: utf-8 -*-
# __author__ = 'Administrator'
import requests

import get_image

codeurl = "http://yjs.ccnu.edu.cn/yjs/security/initDigitPicture.do?Rgb=255|255|255"
valcode = requests.get(codeurl)

f = open('valcode.png', 'wb')
# 将response的二进制内容写入到文件中
f.write(valcode.content)
# 关闭文件流对象
f.close()

code = get_image.getverify1("valcode.png")

print(code)


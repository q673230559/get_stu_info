# 爬取教务处学生信息
## 过程说明
- 识别验证码，获取cookie
- 带cookie模拟登录，获取登录后cookie
- 带cookie 请求具体页面
- 解析页面，获取数据
- 保存数据

## 技术点
- 利用pytesseract-ocr识别验证码
- 利用BeautifulSoup解析html

## 环境说明
- anaconda3.6.4
- 需要安装图片解析软件pytesseract-ocr，并导入库pytesseract
- 其他依赖库按需安装

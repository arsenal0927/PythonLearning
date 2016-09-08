# coding=utf-8

# 获取百度贴吧Python吧的源代码
# 直接获取
import requests
html = requests.get('http://tieba.baidu.com/f?ie=utf-8&kw=python')
print html.text
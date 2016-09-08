# coding=utf-8

# 修改http头获取源代码
# 网站会对访问它的程序进行检查，通过http头的文件实现
import re
import requests

# 下面三行是编码转换功能，先忽略
import sys
reload(sys)
sys.setdefaultencoding("gb18030")
# header是我们自己构造的一个字典，里面保存了user-agent,即修改的http头
# 进入网站查看源代码，进入Network标签，刷新，进入任意一个标签查看Headers--Requests Headers--user-agent,复制即可
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
# 调用header标签的方式
html = requests.get('http://jp.tingroom.com/yuedu/yd300p/',headers = header)

html.encoding = 'utf-8'#这一行是将编码转为utf-8否则中文会显示乱码。

print html.text


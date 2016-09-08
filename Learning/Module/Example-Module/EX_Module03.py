# coding=utf-8

# 使用方法-from...import
# import sys#导入模块
# from sys import version#导入sys模块的同时导入version方法
# print version

#使用方法-from...import*

from sys import *#导入sys模块的同时导入sys模块对应的多有属性和方法
print version
print executable
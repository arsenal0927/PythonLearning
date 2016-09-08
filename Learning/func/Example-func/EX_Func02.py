# coding=utf-8;

# example-函数的形参与实参


# 参数的概念

# a="asdfg"
# print len(a);

# 什么是形参

# def function01(a,b):
#     if a>b:
#         print a;
#     else:
#         print b;

# 什么是实参

# def function02(a,b):
#     if a>b:
#         print a;
#     else:
#         print b;
# function02(2,5);

# 参数的传递

# def function03(a,b):
#     if a>b:
#         print "a>b";
#     else:
#         print "a<=b";
# function03(2,5);

# 关键参数

# def function04(a=1,b=2,c=4):
#     print a;
#     print b;
#     print c;
# function04(5);
# function04(b=7,a=8);
# function04(5,c=2,b=4);
# function04(b=4,c=3,a=1);
'''注意，参数不能冲突'''
# function04(b=2,c=3,6);
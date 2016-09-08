# coding=utf-8

# 栈的实现
class Stack():#定义一个栈的类
    def __init__(st,size):
        '''栈的初始化

        两个参数分别代表栈的主体和栈的容量
        栈的基本形式是列表'''
        st.stack=[]
        st.size=size
        st.top=-1

    def push(st,content):
        '''堆栈操作

        参数为栈的主体和要压入栈的数据
        每压入一个数据栈顶指针st.top自加一
        通过append方法将数据压入栈'''
        if st.Full():
            print "Stack is Full"
        else:
            st.stack.append(content)
            st.top=st.top+1

    def out(st):
        '''出栈操作

        通过函数Empty判断'''
        if st.Empty():
            print "Stack is Empty!"
        else:
            st.top=st.top-1

    def Full(st):
        '''判断栈是否已经满了

        通过栈顶指针st.top与栈的容量比较'''
        if st.top==st.size:
            return True
        else:
            return False

    def Empty(st):
        '''判断栈是否已经空了

        已经空了就不能进行出栈操作，没有空就能继续进行出战操作
        '''
        if st.top==-1:
            print True
        else:
            print False

q=Stack(7)#调用栈Stack
print q.push("hello")#数据的入栈
print q.out()#数据的出栈

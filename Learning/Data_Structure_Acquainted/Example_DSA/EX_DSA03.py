# coding=utf-8

# 队列的实现


class Queue():
    def __init__(qu, size):
        '''队列的初始化

        两个参数为队列的主体和队列的容量
        使用列表进行"[]"声明
        对手和对位的定义'''
        qu.queue = []
        qu.size = size
        qu.head = -1
        qu.tail = -1

    def Empty(qu):
        '''判断队列是否为空

        队尾指针和对位指针是否相等'''
        if qu.head == qu.tail:
            return True
        else:
            return False

    def Full(qu):
        '''判断队列是否已满'''
        if qu.tail - qu.head + 1 == qu.size:
            return True
        else:
            return False

    def enQueue(qu, content):
        '''入队方法

        首先判断是否已满
        通过append方法将数据压入队列'''
        if qu.Full():
            print "Queue is Full!"
        else:
            qu.queue.append(content)
            qu.tail = qu.tail + 1

    def outQueue(qu):
        '''出队操作

        首先判断队列是否为空'''
        if qu.Empty():
            print "Queue is Empty!"
        else:
            qu.head = qu.head + 1

q=Queue(7)
print q.Empty()
print q.enQueue("hello")
print q.Empty()
print q.outQueue()

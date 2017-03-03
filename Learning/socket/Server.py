# encoding: utf-8

import socket
import time
import threading


def tcplink(sock,addr):
    print 'accept new connection from %s:%s...' % addr

    while True:
        data = sock.recv(1024)
        if data:
            if data == "s01d":
                sock.send('happy')
            if data == "s02d":
                sock.send('sad')
            if data == "s03d":
                sock.send('normal')
            else:
                sock.send('input error')
            break
    
    sock.close()
    print 'Connection from %s:%s closed.' % addr

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 监听端口：
s.bind(('127.0.0.1',9999))
s.listen(5)
print 'wating for connection...'


while True:
        # 接受一个新的连接
        sock,addr = s.accept()
        # 创建新的线程来处理TCP连接
        t = threading.Thread(target=tcplink,args=(sock,addr))
        t.start()
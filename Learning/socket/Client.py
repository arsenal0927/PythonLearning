# encoding: utf-8

# socket client in python

import socket
#import argparse
#import time

host = '127.0.0.1'
PORT = 9999

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,PORT))

data = raw_input("Enter your words: ")

# 接受新消息
s.send(data)
print s.recv(1024)
s.send('exit')
s.close()

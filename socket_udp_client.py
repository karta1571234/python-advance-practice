# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 15:43:16 2021

@author: karta
"""


import socket

hostname = '127.0.0.1'
port = 5288
addr = (hostname,port)

clientsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientsock.connect(addr)
clientsock.settimeout(5)

while 1:
    message = str(input("please enter your message : "))
    clientsock.sendall(message.encode())
    server_respose = str(clientsock.recv(1024), encoding='utf-8')
    print('Server response:', server_respose)
    break
clientsock.close()

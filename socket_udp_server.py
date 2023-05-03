# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 15:42:57 2021

@author: karta
"""


import socket, traceback

hostname = '127.0.0.1'
port = 5288
addr = (hostname,port)

srv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #1: option length
srv.bind(addr)
srv.settimeout(20)

print("Start to recv/send")
while 1:
    try:
        message, address = srv.recvfrom(1024)
        print(f"Got data from address {address} : message is {message}")
        srv.sendto(message, address)
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()
#!/usr/bin/env python3

import socket
from time import sleep

TCP_PORT = 59152
TCP_ADDR = '192.168.2.147'

print ("Making Connection to " + str(TCP_ADDR) + ":" + str(TCP_PORT))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((TCP_ADDR, TCP_PORT))
	s.sendall(b'<torchState>1</torchState>')
	sleep(1)
	s.sendall(b'<torchState>2</torchState>')
	sleep(1)
	s.sendall(b'<torchState>0</torchState>')
	sleep(1)
	s.sendall(b'<torchState>1</torchState>')
	sleep(1)

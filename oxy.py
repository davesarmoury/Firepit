#!/usr/bin/env python3

import socket
from gpiozero import LED
from time import sleep

def main():
	print ("Starting...")

	restartConnection()

def restartConnection():
	print ("Starting conncetion process...")

	conn = openConnection()

	if conn:
		torch = LED(17)
		torch.off()
		BUFFER_SIZE = 1024
		while(True):
			data = conn.recv(BUFFER_SIZE)
			if not data:
				break
			else:
				if '1' in str(data):
					torch.on()
					print("ON")
				else:
					torch.off()
					print("OFF")

		print ("Connection Lost")

		torch.off()
		torch.close()
		closeConnection(conn)
		restartConnection()

	else:
		print ("Failed to connect to robot")

def openConnection():
	#Opens socket for KUKA
	TCP_PORT = 59152

	print ("Making Connection Available on " + str(TCP_PORT))

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(('', TCP_PORT))
	s.listen(1)
	conn, addr = s.accept()

	print ('Connection from: %s', addr)

	return conn


def closeConnection(conn):
	conn.close()

main()


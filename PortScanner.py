#!/bin/python

import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #translate hostname to IPv4

else: 
	print("Inavalid amount of arguments.")
	print("Syntac: python3 PortScanner.py <ip>")
	
#add a pretty banner
print("-" * 50)
print("Scanning target "+target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

try: 
	for port in range(50,443):
		s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) #returns an error
		print("Checking port {}".format(port))
		if result == 0:
			print("Port {} is open".format(port))
		s.close()
		
except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()
	
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()

except socket.error:
	print("Coundn't connect to server.")
	sys.exit()

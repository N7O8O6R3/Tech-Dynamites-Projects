#! /bin/python3/

import sys
import socket
from datetime import datetime as dt




# Define our target 

if len(sys.argv) == 2:
	target= socket.gethostbyname(sys.argv[1])
	
else:
	print("Invalid amount of arguments")
	sys.exit()
#Add a pretty banner

print("-"*50)
print("Scanning target"+target)
print("Time started: "+str(dt.now()))
print("-"*50)

try:
	for port in range(0,255):
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		result=s.connect_ex((target,port))
		print("Checking port {}".format(port))
		if result==0:
			print("port {} is open".format(port))
		s.close()
except KeyboardInterrupt:
	print("\nExiting progarm......")
	sys.exit()
except socket.gaierror:
	print("Host Name Cannot Be resolved")
	sys.exit()

except socket.error:
	print("could not connect to server")
	sys.exit()




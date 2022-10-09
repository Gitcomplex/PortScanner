import sys
import socket
from datetime import datetime as dt

# define our target

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("[-] Invalid amount of arguments")
    print("[-] Syntax: Python3 scanner.py <ip>")

# Adding a Pretty Banner

print("-" * 50)
print("Scanning Target "+target)
print("Time Started: "+ str(dt.now()))
print("-" * 50)

try:
    for port in range(50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect((target, port)) # return an error indicator
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\n Exiting Program")
    sys.exit()

except socket.gaierror:
    print("Host name could not be resolved")
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()


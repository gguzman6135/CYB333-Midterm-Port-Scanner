# Port Scanner
# This script will pick a target IP address and a range of ports, then attempt to connect to each port and report which ones are open.

import socket

# identify target and port range
TARGET = "scanme.nmap.org" # localhost for testing purposes. In real scenarios, this would be the IP address of the target machine. ONLY SCAN LOCAL HOST OR scanme.nmap.org OR IP ADDRESSES THAT YOU OWN.
START_PORT = 80
END_PORT = 100
PORT_LIST = [21, 22, 80, 443] # This is a different variable than the range. Its a list of specific ports. To scan these, change the for loop to "for port in PORT_LIST:"

# Before we start, we should make sure to define the rules. If anything is outside of the rules, print a message and exit.
# validate input.
if START_PORT < 1:
    print("Invalid start port. Port numbers must be between 1 and 65535.")
    exit()
if END_PORT > 65535:
    print("Invalid end port. Port numbers must be between 1 and 65535.")
    exit()
if END_PORT < START_PORT:
    print("Invalid port range. End port must be greater than or equal to start port.")
    exit()
# Validate that the target is a valid address. Target can be IP or Hostname.
try:
    socket.gethostbyname(TARGET)
except socket.gaierror:
    print(f"{TARGET} is an invalid target. Please enter a valid IP address or hostname.")
    exit()

#print(f"Valid target and port range. Scanning {TARGET} for open ports in range {START_PORT}-{END_PORT}...") #PORT RANGE MODE
print(f"Valid target and port range. Scanning {TARGET} for open ports in range {PORT_LIST}...") 

for port in PORT_LIST: #PORT LIST MODE
#for port in range(START_PORT, END_PORT +1): # PORT RANGE MODE ... Need to +1 to include the END_PORT in the range because Python excludes the end value.
    # Before you can make a call, you need a phone. Create a socket.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # You make a call and the phone rings and rings, but never gets answered or hangs up. Before you get started, its best to know how long you will wait before you give up (in seconds)?
    s.settimeout(.5)
    # for port in range try each port and do this except if it fails then move on to the next port.
    try:
        s.connect((TARGET, port)) # need 2 parentheses because the outside set creates the function, but the inside creates the tuple.
        # if connection is successful then python will move on to the next line. If it fails, it will just to except.
        print(f"PORT {port} IS OPEN!!!")
        s.close() # close this connection. The phone number answered. Hang up and move on to the next one. 
    except:
        # if connection fails, print a message indicating the port is closed or unreachable.
        print(f"Port {port} is closed or unreachable.")
        s.close()


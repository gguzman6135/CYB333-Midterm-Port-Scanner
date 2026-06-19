# Port Scanner
# This script will pick a target IP address and a range of ports, then attempt to connect to each port and report which ones are open.

import socket

# identify target and port range
TARGET = "127.0.0.1" # localhost for testing purposes. In real scenarios, this would be the IP address of the target machine.
START_PORT = 5550
END_PORT = 5560
print(f"Scanning {TARGET} for open ports in range {START_PORT}-{END_PORT}...")

for port in range(START_PORT, END_PORT +1): # need to add 1 to include the END_PORT in the range because Python excludes the end value.
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


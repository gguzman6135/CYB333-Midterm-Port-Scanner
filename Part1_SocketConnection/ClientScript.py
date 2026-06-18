# This is the client side script for the socket connection example. It calls a server that is already listening for connections. 
#    
# Order of operations:
# Create socket   -> Buy a phone
# Connect         -> Dial the phone number
# Send            -> Say what you must
# Recv            -> Get a response
# Close           -> Hang up

import socket

HOST = '127.0.0.1' # IP address you want to connect to. Localhost for testing purposes.
PORT = 5555      # Port to connect to. Must match the port that the server is listening on.
ADDRESS = (HOST, PORT) #Combining to make it easier. 
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM) # leaving () blank inside will input the default, which is socket.socket(socket.AF_INET, socket.SOCK_STREAM) which is IPV4 and TCP.
print('Socket created. IPV4, TCP')
#start the connection. Dial the phone number listed above.
s.connect(ADDRESS)
print(f'Connected to server on {HOST}:{PORT}')

# Send a message. lets define the message, then encode it, then send it.
message = 'I have got a message for you, Bud.'
message = message.encode()
# Still on the s socket object. read left to right. Send the message OVER s socket.
s.send(message)
# Print confirmation. Confirmation will be in bytes. Message is even more accurate than if it was just the string.
print(f'Message sent: {message}')

#prepare to receive the response. Need to specify how much we can receive at once. 1024 is the standard.
data = s.recv(1024) # receive 1024 bytes of data over the s socket. Then save that variable and call it data.
data = data.decode() #data variable overwrites the previous data variable.
print(f'Response received: {data}')
#close the connection. This is like hanging up the phone.
s.close()
print('Connection closed. Goodbye!')
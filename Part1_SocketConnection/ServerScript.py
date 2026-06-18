# This is the server script for the socket connection example. It listens for incoming connections.
#    
# Order of operations:
# Create socket  -> Buy a phone

# Bind           -> Get a phone number
# Listen         -> Turn the phone on and wait for calls (server side.. not the caller in this case)
# Accept         -> Answer the phone
# Recv           -> Hear the caller's message
# Send           -> Reply to the caller
# Close          -> Hang up

import socket

# Host and port
HOST = '127.0.0.1'  #   Localhost for testing purposes. In real scenarios, this would probably be '' to listen for all IP addresses, or a specific IP address to listen for only that one. The server will accept incoming IPs so you put the IP of another machine.
PORT = 5555   #   Port to listen on. Can only listen to 1 port per socket. 
ADDRESS = (HOST, PORT) # combine to make tuple

# create the socket object. The socket is like the phone, it allows us to communicate with other computers.
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created. IPV4, TCP')

# now that I have created the phone, i need to give it a number (127.0.0.1:5555)
s.bind(ADDRESS)
print(f'Socket is bound on {HOST}:{PORT}')

# listen for incoming connections. 5 is the number of unaccepted connections that the system will allow before refusing new connections. Its basically having a max of 5 people on hold before the phone starts beeping busy.
s.listen(5)
print('Waiting for a connection. Frozen until it comes in...')

#Accept the connection. This is like answering the phone. It will create a new socket object that can be used to send and receive data on the connection. Now, the listening socket can go back to Listening. Also used the python3 f string to print the address of the client that connected. 
connection, client_address = s.accept()
print(f'Connection accepted from {client_address}')

#now, the server is waiting to receive a message over the connection socket. We need to specify how much it can receive at once. 1024 is the standard.
#need to save that message somewhere. lets call it data.
data= connection.recv(1024)
#the data that comes in is in bytes. Need to decode it to get the string.
#new_variable = do_something_to(old_variable) ... python lets you reuse variable names. The old one gets overwritten.
data= data.decode()
print(f'Message received: "{data}"')

# now that the person on the other side of the line has said what they had to say, we must politely reply. 
# The following line is a simple example, but does not allow us to easily change responses.
#       connection.send(b'Message received, Buddy!')
# Instead, I will make a string. More complex code would probably use a something more dynamic.
response = 'Message received, Buddy!'

# Computer wants bytes. Must encode the string above.
response = response.encode()

# Send the response back to the client.
connection.send(response)
# Print confirmation. Confirmation will be in bytes. Message is even more accurate than if it was just the string.
print(f'Response sent. {response}')

# close the connection socket. This is like hanging up the phone on that particular caller.
connection.close()
print('Connection closed.')
# close the listening socket. This is like turning off the phone and going for a walk.
s.close()
print('Socket closed. Goodbye!')
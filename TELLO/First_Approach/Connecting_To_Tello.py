import socket

# Constants
UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789
Message = "Hello, Server"

# Socket creation
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Sending information (1)
clientSock.sendto(Message.encode(encoding='UTF-8'), (UDP_IP_ADDRESS, UDP_PORT_NO))

# Receiving information
data = clientSock.recv(4096)
print("Received: " + data.decode(encoding='UTF-8'))

# Sending information (2)
clientSock.sendto("Bye Bye, Server".encode(encoding='UTF-8'), (UDP_IP_ADDRESS, UDP_PORT_NO))
# Receiving information
data = clientSock.recv(4096)
print("Received: " + data.decode(encoding='UTF-8'))
#
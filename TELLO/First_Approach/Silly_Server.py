import socket

# Constants
UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789

# Create server socket
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to IP and port
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))

# Print messages received
while True:
    data, addr = serverSock.recvfrom(1024)
    print ("Message: " + data.decode(encoding='UTF-8'))
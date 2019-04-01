import socket

# Constants
UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789
RESPONSE = "This is a basic server. We are communicating. You sent me: "

# Create server socket
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to IP and port
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))

# Print messages received
while True:
    data, addr = serverSock.recvfrom(1024)
    if data:
        print ("Message: " + data.decode(encoding='UTF-8'))
        serverSock.sendto(RESPONSE.encode(encoding='UTF-8') + data, addr)
import socket
import time

# Constants
TELLO_CLIENT_IP = "192.168.10.1"
TELLO_CLIENT_PORT = 8889
INITIATE_SDK = "command"
BATTERY = "battery?"
WIFI = "wifi?"
SDK_VERSION = "sdk?"
STREAM_ON = "streamon"

# Client socket creation
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Initiate SDK
clientSock.sendto(INITIATE_SDK.encode(encoding='UTF-8'), (TELLO_CLIENT_IP, TELLO_CLIENT_PORT))
print("SDK Initiated")
# # Receiving information
data = clientSock.recv(4096)
print("Received: " + data.decode(encoding='UTF-8'))


# Getting battery status
clientSock.sendto(BATTERY.encode(encoding='UTF-8'), (TELLO_CLIENT_IP, TELLO_CLIENT_PORT))
print("Battery sent")
data = clientSock.recv(4096)
print("Received: " + data.decode(encoding='UTF-8'))

# Getting WiFi status
clientSock.sendto(WIFI.encode(encoding='UTF-8'), (TELLO_CLIENT_IP, TELLO_CLIENT_PORT))
print("WiFi sent")
data = clientSock.recv(4096)
print("Received: " + data.decode(encoding='UTF-8'))
#

# Getting SDK Version
clientSock.sendto(SDK_VERSION.encode(encoding='UTF-8'), (TELLO_CLIENT_IP, TELLO_CLIENT_PORT))
print("SDK sent")
data = clientSock.recv(4096)
print("Received: " + data.decode(encoding='UTF-8'))

# Activating stream
clientSock.sendto(STREAM_ON.encode(encoding='UTF-8'), (TELLO_CLIENT_IP, TELLO_CLIENT_PORT))
print("Stream sent")
data = clientSock.recv(4096)
print("Received: " + data.decode(encoding='UTF-8'))
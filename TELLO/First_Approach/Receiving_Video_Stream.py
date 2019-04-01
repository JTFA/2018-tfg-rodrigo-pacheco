import socket
import vlc

# Constants
TELLO_SERVER_IP = "0.0.0.0"
TELLO_SERVER_PORT = 11111

# Create server socket
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to IP and port
serverSock.bind((TELLO_SERVER_IP, TELLO_SERVER_PORT))

# Print messages received
player = vlc.MediaPlayer('rtsp://:8554/output.h264')
while True:
    data, addr = serverSock.recvfrom(1024)
    if data:
        frame = self._h264_decode(data)
        print("Message: " + response)
        if "mid" != response.split(":")[0]:
            print ("Message: " + response)
            # serverSock.sendto(RESPONSE.encode(encoding='UTF-8') + data, addr)
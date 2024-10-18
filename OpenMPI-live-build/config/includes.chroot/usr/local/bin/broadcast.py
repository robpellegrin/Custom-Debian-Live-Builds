import socket
import time

def broadcast_hostname():
    BROADCAST_IP = '255.255.255.255'
    BROADCAST_PORT = 9999
    HOSTNAME = "Manager"

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    while True:
        sock.sendto(HOSTNAME.encode(), (BROADCAST_IP, BROADCAST_PORT))
        time.sleep(5)

if __name__ == "__main__":
    broadcast_hostname()

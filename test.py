import socket
import time

# Create a TCP / IP socket
j = 0.0 # data to be sent to MATLAB

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('192.168.6.3', 22))
    s.listen(1)
    conn, addr = s.accept()
    print(f"Connected: {conn, addr}")

while True:
    t = conn.sendall(f"{j}".encode())
    j += 1.0
    time.sleep(2)

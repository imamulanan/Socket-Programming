# 1. Implement a simple file transfer protocol (FTP) using connection-oriented
#  and connectionless sockets. The connection-oriented FTP works as follows: At
#  the client side, the file to be transferred is divided into units of 100 bytes (and
#  maybeless than100bytes for the last unit depending on the size of the file).
#  The client transfers each unit of the file to the server and expects an
#  acknowledgment from the server. Only after receiving an acknowledgment
#  from the server, the client transmits the next unit of the file. If the
#  acknowledgment is not received within a timeout period (choose your own
#  value depending on your network delay), the client retransmits the unit. The
#  above process is repeated until all the contents of the file are transferred. The
#  connectionless FTP works simply as follows: The file is broken down into lines
#  and the client sends one line at a time as a datagram packet to the server.
#  There is no acknowledgment required from the server side.

import socket
import time

HOST = '127.0.0.1'
PORT = 5000
CHUNK_SIZE = 100  # 100 bytes

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(3)  # timeout = 3 sec
client.connect((HOST, PORT))  # সার্ভারে কানেক্ট

filename = "testfile.txt"

with open(filename, "rb") as f:
    while True:
        chunk = f.read(CHUNK_SIZE)

        if not chunk:
            break  # file finished

#         # এক chunk সার্ভারে পাঠানোর পরে ACK আসা পর্যন্ত এই লুপ চলবে।
# ACK না পাওয়া পর্যন্ত break হবে না।
        while True:
            try:
                client.sendall(chunk)

                # ACK এর জন্য অপেক্ষা
                ack = client.recv(1024)

                if ack == b"ACK":
                    print("ACK received. Sending next chunk...")
                    break
            except socket.timeout:
                print("Timeout! Resending chunk...")
                continue

# File end signal
client.sendall(b"EOF")

client.close()

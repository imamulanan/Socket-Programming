# 5. Develop a simple chatting application using (i) Connection-oriented and (ii)
#  Connectionless sockets. In each case, when the user presses the “Enter” key,
#  whatever characters have been typed by the user until then are transferred to
#  the other end. You can also assume that for every message entered from one
#  end, a reply must comefromthe other end,before another message could be
#  sent. In other words, more than one message cannot be sent from a side
#  before receiving a response from the other side. For connectionless
#  communication, assume the maximum number ofcharacters that can be
#  transferred in a message to be 1000. The chat will be stopped by pressing
#  Ctrl+C on both sides.

import socket

HOST = '127.0.0.1'
PORT = 9000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print(f"Connected to TCP Chat Server\n")

try:
    while True:
        msg = input("You: ")
        client.send(msg.encode())
        
        reply = client.recv(1024).decode()
        if not reply:
            break
        print(f"Server: {reply}")
except KeyboardInterrupt:
    print("\nChat ended")

client.close()

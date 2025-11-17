#  6. Extend the single client– single server chatting application developed in Q5
#  using connection-oriented sockets to a multiple client– single server chatting
#  application. The single server should be able to chat simultaneously with
#  multiple clients. In order to do this, you will have to implement the server
#  program using threads. Once a client program contacts a server, the server
#  process spawns a thread that will handle the client. The communication
#  between aclient and its server thread will be like a single client-single server
#  chatting application.


import socket

HOST = '127.0.0.1'
PORT = 9500

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print(f"Connected to Multi-Client Chat Server\n")

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

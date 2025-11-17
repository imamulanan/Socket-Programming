#  2. Develop a concurrent file server that spawns several threads, one for each
#  client requesting a specific file. The client program sends the name of the file
#  to bedownloadedtotheserver. The server creates the thread by passing the
#  nameofthefile as the argument for the thread constructor. From then on, the
#  server thread is responsible for transferring the contents of the requested file.
#  Use connection-oriented sockets (let the transfer size be at most 1000 bytes
#  per flush operation). After a flush operation, the server thread sleeps for 200
#  milliseconds.


import socket

HOST = '127.0.0.1'
PORT = 6000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

filename = input("Enter filename to download: ")
client.send(filename.encode())

response = client.recv(1024)
if response == b'OK':
    with open(f'downloaded_{filename}', 'wb') as f:
        while True:
            data = client.recv(1000)
            if not data:
                break
            f.write(data)
    print(f"File downloaded as downloaded_{filename}")
else:
    print(response.decode())

client.close()

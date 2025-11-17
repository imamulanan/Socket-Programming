import socket

HOST = '127.0.0.1'
PORT = 5001

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# AF_INET → IPv4
# SOCK_DGRAM → UDP (connectionless)

filename = input("Enter filename to send: ")

with open(filename, 'r') as f:
    for line in f:
        client.sendto(line.encode(), (HOST, PORT))
        print(f"Sent: {line.strip()}")

client.sendto(b'EOF', (HOST, PORT))
print("File transfer complete")
client.close()

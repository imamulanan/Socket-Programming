#  4. Develop a streaming client and server application using connectionless
#  sockets that works as follows: The streaming client contacts the streaming
#  server requesting a multi-media file (could be an audio or video file) to be
#  sent. The server then reads the contents of the requested multi-media file in
#  size randomly distributed between 1000 and 2000 bytes and sends the
#  contents read to the client as a datagram packet. The last datagram packet
#  that will be transmitted could be of size less than 1000 bytes, if required. The
#  client reads the bytes, datagram packets, sent from the server. As soon as a
#  reasonable number of bytes are received at the client side, the user working at
#  the client side should be able to launch a media player and view/hear the
#  portions of the received multi-media file while the downloading is in progress.


import socket
import subprocess
import threading
import time

HOST = '127.0.0.1'
PORT = 8000
BUFFER_SIZE = 10000

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

filename = input("Enter multimedia file to stream: ")
output_file = f"streaming_{filename}"


# ক্লায়েন্ট সার্ভারকে বলে: "আমি এই ফাইল চাই"
# UDP datagram হিসেবে ফাইলের নাম পাঠানো হচ্ছে
client.sendto(filename.encode(), (HOST, PORT))


# সার্ভার যদি ফাইল না পায় → ERROR পাঠায়
# ফাইল না থাকলে client exit করবে
response, _ = client.recvfrom(1024)
if response != b'OK':
    print("File not found on server")
    exit()

print("Streaming started...")

bytes_received = 0
player_launched = False

with open(output_file, 'wb') as f:
    while True:
        try:
            client.settimeout(2)
            data, _ = client.recvfrom(2048)
            
            if data == b'EOF':
                print("\nStreaming complete")
                break
            
# ফাইল লিখা হচ্ছে
# flush() → ফাইল disk-এ immediately save
# bytes_received → মোট ডেটা কত এসেছে
# end='\r' → same line এ counter আপডেট
            f.write(data)
            f.flush()
            bytes_received += len(data)
            print(f"Received: {bytes_received} bytes", end='\r')
            
            if bytes_received >= BUFFER_SIZE and not player_launched:
                print(f"\n{BUFFER_SIZE} bytes buffered. You can now play the file.")
                print(f"Run: vlc {output_file}  (or any media player)")
                player_launched = True
        
        except socket.timeout:
            print("\nStream timeout")
            break

print(f"File saved as: {output_file}")
client.close()

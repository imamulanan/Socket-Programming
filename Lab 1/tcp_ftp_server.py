import socket

# সার্ভারের IP এবং PORT
HOST = '127.0.0.1'
PORT = 5000

# TCP socket তৈরি
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))            # নির্দিষ্ট ঠিকানায় bind করা
server.listen(1)                     # একবারে ১টি কানেকশন নেবে

print("Server is running... Waiting for connection...")

# ক্লায়েন্ট কানেক্ট না হওয়া পর্যন্ত সার্ভার অপেক্ষা করবে
conn, addr = server.accept()
print("Connected with:", addr)

# ক্লায়েন্ট থেকে পাওয়া ফাইল লেখার জন্য নতুন ফাইল খোলা
with open("received_file.txt", "wb") as f:

    while True:
        # ক্লায়েন্ট থেকে ডাটা রিসিভ (একবারে 1024 bytes)
        data = conn.recv(1024)

        # যদি ক্লায়েন্ট "EOF" পাঠায় → ফাইল শেষ
        if data == b"EOF":
            print("File transfer complete.")
            break

        # ফাইলে ডেটা লিখে দেওয়া
        f.write(data)

        # প্রতিটি chunk এর জন্য ক্লায়েন্টকে ACK পাঠানো
        conn.sendall(b"ACK")

# কানেকশন বন্ধ
conn.close()
server.close()

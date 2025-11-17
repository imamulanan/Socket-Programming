#  3. Develop a “Remote Calculator” application that works as follows: The client
#  program inputs two integers and an arithmetic operation (‘*’,’/’,’%’,’+’,’-‘) from
#  the user and sends these three values to the server side. The server does the
#  binary operation on the two integers and sends backs the result of the
#  operation to the client. The client displays the result to the user.


import socket

HOST = '127.0.0.1'
PORT = 7000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

num1 = input("Enter first number: ")
operator = input("Enter operator (+, -, *, /, %): ")
num2 = input("Enter second number: ")

message = f"{num1} {operator} {num2}"
client.send(message.encode())

result = client.recv(1024).decode()
print(f"Result: {num1} {operator} {num2} = {result}")

client.close()

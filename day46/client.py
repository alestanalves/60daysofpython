import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 12345

client_socket.connect((host, port))

message = "Oi sou o Goku"
client_socket.send(message.encode())

response = client_socket.recv(1024).decode()
print(f"Resposta do servidor: {response}")

client_socket.close()
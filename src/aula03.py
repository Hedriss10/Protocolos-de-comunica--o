from socket import *


host = "127.0.0.1"
port = 43120


msg = bytes(input("Digite algo: "), 'utf-8')
obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.connect((host, port))
obj_socket.send(msg)
response = obj_socket.recv(1024)
print("Recebemos sua mensagem", response)
obj_socket.close()
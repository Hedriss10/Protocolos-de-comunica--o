from socket import *

#-----------------------
#host
#port
host = "127.0.0.1"
port = 43210
#-----------------------


obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.connect((host, port))
print("Servidor pronto..")


while True:
    dados, origem = obj_socket.recvfrom(65535)
    print("Origem....", origem)
    print("Dados...", dados.decode())
    response = input("Digite a respo: ")
    obj_socket.sendto(response.encode(), origem)
    
    
    obj_socket.close()

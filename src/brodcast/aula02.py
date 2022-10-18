from socket import *



host = "127.0.0.1"
port = 43210


obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.connect((host, port))
saida = ""

while saida != "X":
    msg = input("\nSua mensagem\n: ")
    obj_socket.sendto(msg.encode(), (host, port))
    dados, origem = obj_socket.recvfrom(65535)
    print("Reposta do servidor", dados.decode())
    exit_saida = input("Aperta o x para sair").upper()
    

    
obj_socket.close()
    

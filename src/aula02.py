from socket import *

servidor = "127.0.0.1" # localhost 
port = 43120 #porta 

#trabalhando com protocolos tcp 
obj_socket = socket(AF_INET, SOCK_STREAM) # informando á tipagem de dados 
obj_socket.bind((servidor, port)) #conexão com o servidor 
obj_socket.listen(2) # cliente para conectar

print("Aguardando o cliente....")


while True:
    con, client = obj_socket.accept() # aceitamos a conexão 
    print(f"Logado com sucesso ", client) # damos boas vindas 
    
    while True:
        msg_recibe = str(con.recv(1024)) # maximo de mensagem recebida
        print(f"Recebemos sua mensagem", msg_recibe)
        msg_send = b"Hellow world"
        con.send(msg_send)
        break 
    con.close()
        
    

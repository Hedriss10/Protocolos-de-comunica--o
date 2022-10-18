import socket

resp="S"

while(resp == "S"):
    url = input("Digite sua url: ")
    ip= socket.gethostbyname(url)
    print("O IP informado é: ", ip)
    resp=input("Digite <S> para continuar: ").upper()

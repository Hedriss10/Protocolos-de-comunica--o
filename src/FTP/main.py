from ftplib import *


ftp = FTP("ftp.ibiblio.org")


print(ftp.getwelcome())


usario = input("Digite o usuario: ")

senha =  input("Digite sua senha: ")


ftp.login(usario, senha)

print('Diretório atual do trabalho: ', ftp.pwd())


ftp.cwd('pub')


print('Diretorio corrente:' , ftp.pwd())

print(ftp.retrlines("LIST"))

ftp.quit()
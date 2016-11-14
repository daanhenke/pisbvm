#UDP BROADCASTER FOR OFF DEVICE DEBUGGING AND INFORMATION GATHERING

import socket


class UDPBugger(object):
    def __init__(self):
        self.address = ('<broadcast>', 1337)
        self.name = "PIV1TEST"

        self.server_address = None

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)


    def broadcast(self):
        self.socket.sendto("00x0", self.address)
        data, servaddr = self.socket.recvfrom(2048)

        if data == "00x1":
            print "Connected to udpBugger compatible server"
            self.server_address = servaddr
        else:
            print "Something went wrong.."
            print data, servaddr

    def send(self, code, message):
        if self.server_address is not None:
            self.socket.sendto(str(code) + ":" + message, self.server_address)
        print str(code) + ":" + message
        #TODO: ELSE PUT ONTO QUEUE AND SEND WHEN CONNECTION IS MADE

    def log(self, message):
        self.send("01x0", message)
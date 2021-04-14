import socket
class User:
    def __init__(self,skt,username="null"):
        self.skt=skt
        self.username=username
        #self.password=password
    def sendmsg(self,msg):
        self.skt.send(msg.encode("utf-8"))
    def logout(self):
        self.skt.close()
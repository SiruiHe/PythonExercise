'''
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

hello={"何思睿":"540660919","黄宸睿":"1128321"}
for name in hello.keys():
    print(name)
'''
import threading,time

def test():
    for i in range(1,50):
        print("子线程"+str(i))

a=threading.Thread(target=test)
a.start()
for j in range(10,20):
    print("父线程" + str(j))
    if(j==15):
        print("父线程挂起")
        time.sleep(10)
a.join()



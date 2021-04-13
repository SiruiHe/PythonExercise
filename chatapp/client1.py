import threading,time,socket
host="127.0.0.1"
port=8888
addr0=(host,port)
sc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sc.connect(addr0)
while(1):
    data=input("输入：")
    if not data:
        break
    sc.send(data.encode("utf-8"))
    data=sc.recv(100)
    if not data:
        break
    print("收到消息:"+data.decode("utf-8"))
sc.close()
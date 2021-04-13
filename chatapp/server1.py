import threading,socket,time

def tcp_link(conn,addr):
    conn.send("Welcome!".encode("utf-8"))
    while(1):
        try:
            data=conn.recv(100)
        except Exception:
            print("一客户端登出")
            break
        print("收到消息:"+data.decode("utf-8"))
        if not data:
            break
        msg=time.strftime("%y-%m-%d %x")
        conn.send(msg.encode("utf-8"))
    conn.close()

host="127.0.0.1"
port=8888
addr0=(host,port)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(addr0)
s.listen(5)
print("开始监听")
while(1):
    conn,addr=s.accept()
    print("已连接:"+str(addr))
    t=threading.Thread(target=tcp_link,args=(conn,addr))
    t.start()
s.close()


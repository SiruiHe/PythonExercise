import threading,socket,time,shelve

host="127.0.0.1"
port=8888
addr0=(host,port)
global usermap
userstate={}

def sendmsg(skt,msg,head=""):
    if len(head)>0:
        msg=head+msg
    skt.send(msg.encode("utf-8"))

class User:
    def __init__(self,skt,username="null"):
        self.skt=skt
        self.username=username
        #self.password=password
    def sendmsg(self,msg):
        self.skt.send(msg.encode("utf-8"))
    def logout(self):
        self.skt.close()

def server_signup(skt):
    global usermap
    flag=0
    while(1):
        msg=skt.recv(100).decode("utf-8")
        msg=msg.split("$")
        if(msg[0]=="signup_username"):
            username=msg[1]
            flag+=1
            text = "ok"
            skt.send(text.encode("utf-8"))

        if(msg[0]=="signup_password"):
            password=msg[1]
            flag+=1
        if flag==2:
            break
    usermap[username]=password
    text="signup_ok"
    #打出来看一下
    print(usermap[username])

    skt.send(text.encode("utf-8"))
    server_login(skt)


def server_login(skt):
    global usermap
    flag=0
    username,password="",""
    while(1):
        msg=skt.recv(100).decode("utf-8")
        msg=msg.split("$")
        if(msg[0]=="login_username"):
            username=msg[1]
        if(msg[0]=="login_password"):
            password=msg[1]
        if len(username)>0 and len(password)>0:
            try:
                if(usermap[username]==password):
                    break
                else:
                    sendmsg(skt,"login_failed")
                    username,password="",""
            except Exception:
                sendmsg(skt, "login_failed")
                username, password = "", ""
    sendmsg(skt,"login_ok")
    server_user_online(skt,username)



def server_user_online(skt,username):
    print("test 该用户成功登陆！")
    user=User(skt,username)

    ##
    while (1):
        try:
            data = skt.recv(100)
            msg = data.decode("utf-8")
        except Exception:
            print("一客户端登出")
            break
        print("收到消息:" + msg)

        if not data:
            break
        msg = time.strftime("%y-%m-%d %x")
        skt.send(msg.encode("utf-8"))



def tcp_link(conn,addr):
    #conn.send("Welcome!".encode("utf-8"))
    while(1):
        try:
            data=conn.recv(100)
            msg=data.decode("utf-8")
        except Exception:
            print("一客户端登出")
            break
        print("收到消息:"+msg)
        if(msg.startswith("signup_guide$")):
            server_signup(conn)
        if(msg.startswith("login_guide$")):
            server_login(conn)


        if not data:
            break
        msg=time.strftime("%y-%m-%d %x")
        conn.send(msg.encode("utf-8"))
    conn.close()



def main():
    global usermap
    usermap=shelve.open("userinfo")
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(addr0)
    s.listen(10)
    print("开始监听")
    while(1):
        conn,addr=s.accept()
        print("已连接:"+str(addr))
        t=threading.Thread(target=tcp_link,args=(conn,addr))
        t.start()
    s.close()
    usermap.close()

if __name__=="__main__":
    main()

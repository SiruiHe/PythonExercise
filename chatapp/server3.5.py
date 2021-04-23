import threading,socket,time,shelve,struct

host="0.0.0.0" #??
port=8888
addr0=(host,port)
global usermap


userstate={}    #[用户名：socket]的字典

def sendmsg(skt,msg,head=""):
    if len(head)>0:
        msg=head+msg
    skt.send(msg.encode("utf-8"))

'''
class User:
    def __init__(self,skt,username="null"):
        self.skt=skt
        self.username=username
        #self.password=password
    def sendmsg(self,msg):
        self.skt.send(msg.encode("utf-8"))
    def logout(self):
        self.skt.close()
'''

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
    global userstate
    global file_permission
    file_permission=0
    print("用户 "+username+" 成功登陆！")
    userstate[username]=skt

    #send_usertemp(skt)

    #服务器消息处理与转发
    while(1):
        msg=skt.recv(100).decode("utf-8")
        msg=msg.split("$")
        print("收到"+str(msg))

        if(msg[0]=="chat_with_sb"):
            username1=msg[1]
            skt1=userstate[username1]
            newmsg=username+":"+msg[2]
            sendmsg(skt1,newmsg)
        if(msg[0]=="online_or_not"):
            username1=msg[1]
            if username1 in userstate.keys():
                sendmsg(skt,"online$")
            if username1 not in userstate.keys():
                sendmsg(skt,"offline$")
        if(msg[0]=="get_usertemp"):
            send_usertemp(skt)
        if (msg[0] == "say_byebye"):
            sendmsg(skt,"byebye$")
            sendmsg(skt1, "byebye$")
        if (msg[0] == "receive_file_request"):
            print("收到文件接收请求:"+str(msg))
            username1 = msg[1]
            skt1 = userstate[username1]
            sendmsg(skt,"receive_file_permission$")
            file_permission=1
            msg=skt.recv(100).decode("utf-8")
            while(file_permission!=2):
                pass
            sendmsg(skt1,msg)

        if(msg[0]=="send_file_request"):
            print("收到文件发送请求:" + str(msg))
            while(file_permission!=1):
                pass
            sendmsg(skt,"send_file_permission$")
            file_permission=2

        if (msg[0] == "receive_file_over"):
            file_permission = 0

        if (msg[0] == "logout"):
            print("已退出:"+msg[1])
            del userstate[username]

        if(msg[0]=="start_send_file"):

            username1 = msg[1]
            skt1 = userstate[username1]
            sendmsg(skt1,"file_ready$")

            '''
            
            fileinfo_size = struct.calcsize("128sl")
            buf = skt.recv(fileinfo_size)
            sendmsg(skt1, buf)
            filename, filesize = struct.unpack("128sl", buf)
            recvd_size = 0
            while recvd_size < filesize:
                if (filesize - recvd_size > 1024):
                    data = skt.recv(1024)
                    recvd_size += len(data)
                    sendmsg(skt1,data)
                    process = recvd_size / filesize * 100
                    print("接收中: " + "%.2f" % process + "%")
                else:
                    data = skt.recv(filesize - recvd_size)
                    recvd_size = filesize
            print("接收完毕!")
            
            '''

            while (1):
                msg = skt.recv(1024)
                try:
                    if(msg.decode("utf-8").startswith("send_file_over$")):
                        break
                except UnicodeDecodeError:
                    pass
                skt1.send(msg)
            #file_permission = 0
            print("退出文件发送")





    #chat_with_sb(username, skt, username1)


    #a_to_b=threading.Thread(target=chat_with_sb,args=(skt,username))
    #b_to_a = threading.Thread(target=chat_with_sb, args=(username, username))

def send_usertemp(skt):
    global userstate
    # 发送在线名单
    usertemp = ""
    try:
        for user in userstate.keys():
            usertemp=usertemp+user+"\n"
    except Exception:
        usertemp = ""
    sendmsg(skt, usertemp)
    return

'''
def chat_with_sb(username,skt,username1):

    # 我方用户名username,我方socket为skt
    # 对方用户名username1,对方socket为chatwith
    chatwith=userstate[username1]
    while (1):
        try:
            data = skt.recv(100)
            msg = data.decode("utf-8")
        except Exception:
            print("异常")
            break
        msg_with_head = username + ": " + msg
        print("收到消息:" + msg_with_head)
        if(msg=="byebye"):
            #向对方通知这边退出。msg原始信息（不含用户名头）
            sendmsg(chatwith,msg)
            print(username+" 主动退出。")
            break
        sendmsg(chatwith,msg_with_head)
    server_user_online(skt,username)
'''





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
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
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

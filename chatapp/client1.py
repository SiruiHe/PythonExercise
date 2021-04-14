import threading,time,socket

host="127.0.0.1"
port=8888
addr0=(host,port)
chat_with_byebye_flag=0

def sendmsg(skt,msg,head=""):
    if len(head)>0:
        msg=head+msg
    skt.send(msg.encode("utf-8"))



def client_signup(skt):
    print("欢迎注册！")
    guide="signup_guide$"
    skt.send(guide.encode("utf-8"))
    while(1):
        username=input("请输入您想使用的用户名：")
        text="signup_username$"+username
        skt.send(text.encode("utf-8"))
        msg=skt.recv(100).decode("utf-8")

        password=input("请输入您想设置的密码：")
        text="signup_password$"+password
        skt.send(text.encode("utf-8"))
        msg=skt.recv(100).decode("utf-8")

        if(msg.lower()=="signup_ok"):
            print("注册成功,转入登陆界面")
            break
        else:
            print("注册失败,请重试")
    client_login(skt)

def client_login(skt):
    print("欢迎登录！")
    guide="login_guide$"
    skt.send(guide.encode("utf-8"))
    while(1):
        username = input("请输入您的用户名：")
        sendmsg(skt,username,"login_username$")

        password = input("请输入您的密码：")
        sendmsg(skt,password,"login_password$")
        msg=skt.recv(100).decode("utf-8")
        if (msg.lower() == "login_ok"):
            print("登录成功")
            break
        else:
            print("登录失败,请重试")
    client_online(skt)
        

def client_online(skt):
    print("test 登陆成功！")
    while(1):
        msg=skt.recv(100).decode("utf-8")
        if(len(msg)>0):
            break
        else:
            print("当前没有其他用户在线，等待10秒后重试。")
            time.sleep(10)
            #sendmsg(skt,"onlinelist$")
    print("当前在线的用户有：\n"+msg)
    while(1):
        chatwith=input("请输入想聊天用户的名字：")
        sendmsg(skt,chatwith,"chat_with_sb$")
        msg=skt.recv(100).decode("utf-8")
        if(msg.startswith("chat_start")):
            print("开始和 "+chatwith+" 聊天。")
            break
        else:
            print("找不到 "+chatwith+" ,请重试。")
    client_chat_with_sb(skt,chatwith)

def client_chat_with_sb(skt,chatwith):
    global chat_with_byebye_flag
    #启动另一个监听线程
    thread_receive=threading.Thread(target=clinet_thread_receive,args=(skt,))
    thread_receive.start()

    while (1):
        #data = input("输入：")
        data = input()
        skt.send(data.encode("utf-8"))
        if(data=="byebye"):
            chat_with_byebye_flag=1
            break
        if(chat_with_byebye_flag==1):
            #chat_with_byebye_flag=0
            break
    print("你已退出与 "+chatwith+" 的对话")
    time.sleep(0.5)
    chat_with_byebye_flag=0
    time.sleep(0.5)
    client_online(skt)

def clinet_thread_receive(skt):
    global chat_with_byebye_flag
    while (1):
        msg=skt.recv(100).decode("utf-8")
        if(msg.startswith("byebye")):
            print("对方已退出。")
            chat_with_byebye_flag=1
            break
        elif(chat_with_byebye_flag==1):
            break
        else:
            print("\n"+msg)


def main():
    skt=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    skt.connect(addr0)
    print("连接成功。请选择...")
    print("1.注册\t2.登陆\t")
    choice1=input(">>")
    if(choice1=="1"):
        client_signup(skt)
    if(choice1=="2"):
        client_login(skt)
    '''
    while(1):
        data=input("输入：")
        if not data:
            break
        skt.send(data.encode("utf-8"))
        data=skt.recv(100)
        if not data:
            break
        print("收到消息:"+data.decode("utf-8"))
    skt.close()
    '''


if __name__ == '__main__':
    main()
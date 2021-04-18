import threading, time, socket,os,struct
#服务器公网ip地址
host = "127.0.0.1"
port = 8888
addr0 = (host, port)
clinet_receive_flag = 0


def sendmsg(skt, msg="", head=""):
    if len(head) > 0:
        msg = head + msg
    skt.send(msg.encode("utf-8"))


def client_signup(skt):
    print("欢迎注册！")
    guide = "signup_guide$"
    skt.send(guide.encode("utf-8"))
    while (1):
        username = input("请输入您想使用的用户名：")
        text = "signup_username$" + username
        skt.send(text.encode("utf-8"))
        msg = skt.recv(100).decode("utf-8")

        password = input("请输入您想设置的密码：")
        text = "signup_password$" + password
        skt.send(text.encode("utf-8"))
        msg = skt.recv(100).decode("utf-8")

        if (msg.lower() == "signup_ok"):
            print("注册成功,转入登陆界面")
            break
        else:
            print("注册失败,请重试")
    client_login(skt)


def client_login(skt):
    print("欢迎登录！")
    guide = "login_guide$"
    skt.send(guide.encode("utf-8"))
    while (1):
        username = input("请输入您的用户名：")
        sendmsg(skt, username, "login_username$")

        password = input("请输入您的密码：")
        sendmsg(skt, password, "login_password$")
        msg = skt.recv(100).decode("utf-8")
        if (msg.lower() == "login_ok"):
            print("登录成功")
            break
        else:
            print("登录失败,请重试")

    # 转入本客户机发送过程
    client_online(skt)


def client_online(skt):
    global clinet_receive_flag
    print("test 登陆成功！")
    while (1):
        clinet_receive_flag = 0
        # stop=0
        while (1):
            # 获取在线用户
            sendmsg(skt, "get_usertemp$")
            msg = skt.recv(100).decode("utf-8")

            print("\n当前在线的用户有：\n" + msg)
            chatwith = input("请输入用户的名字：")
            sendmsg(skt, chatwith, "online_or_not$")
            msg = skt.recv(100).decode("utf-8")
            if (msg.startswith("online$")):
                break
            if (msg.startswith("offline$")):
                print("无法与此用户取得联系，请重试。")


        while(1):
            print("请选择您想做的事情：")
            print("1.聊天\t2.发文件\t3.收文件\t")
            choice2=int(input(">>"))
            if(choice2==1 or choice2==2 or choice2==3):
                break

        # 开始聊天
        if(choice2==1):
            print("向用户 " + chatwith + " 发送消息")
            clinet_receive = threading.Thread(target=clinet_thread_receive, args=(skt,))
            clinet_receive.start()

            while (1):
                msg = input()
                sendmsg(skt, chatwith + "$" + msg, "chat_with_sb$")
                if (msg.startswith("byebye")):
                    sendmsg(skt, "say_byebye$")
                    clinet_receive_flag = 1
                    time.sleep(0.2)
                    clinet_receive.join()
                    break

        #发文件
        elif(choice2==2):
            print("向用户 " + chatwith + " 传输文件")
            print("接收方准备中...")
            sendmsg(skt, chatwith + "$", "send_file_request$")
            msg=skt.recv(100).decode("utf-8")

            if(msg.startswith("send_file_permission$")):
                clinet_send_file(skt)

        elif (choice2 == 3):
            print("从用户 " + chatwith + " 接收文件")
            sendmsg(skt, chatwith + "$", "receive_file_request$")
            msg = skt.recv(100).decode("utf-8")

            if (msg.startswith("receive_file_permission$")):
                clinet_receive_file(skt)



def clinet_send_file(skt):
    print("欢迎来到发送界面！")
    msg=skt.recv(100).decode().split("$")
    ip=msg[1]
    port=int(msg[2])
    skt_send = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host=(ip,port)
    skt_send.connect(host)

    #sendmsg(skt, "127.0.0.1$6666", "sendhere$")
    count = 0
    while (1):
        filepath = input("输入要发送的文件路径:")
        if len(filepath) == 0:
            filepath = r"C:\Users\sword\Pictures\老中青.JPG"
        if os.path.isfile(filepath):
            fileinfo_size = struct.calcsize("128sl")
            filehead = struct.pack("128sl", bytes(os.path.basename(filepath).encode('utf-8')),
                                   os.stat(filepath).st_size)
            skt_send.send(filehead)
            print("接收方文件路径:{}".format(filepath))

            fp = open(filepath, "rb")
            while (1):
                data = fp.read(1024)
                count += len(data)
                if not data:
                    print("{0} 此文件发送完成.".format(filepath))
                    break
                skt_send.send(data)
                process = count / os.stat(filepath).st_size * 100
                # print("Receiving process: " + "%.2f" % process + "%")
                print("发送中: " + "%.2f" % process + "%")
        skt_send.close()
        break
    return

def clinet_receive_file(skt):
    print("欢迎来到接收界面！")
    skt_receive = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    skt_receive.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    skt_receive.bind(("0.0.0.0", 6666))  # 0.0.0.0
    skt_receive.listen(2)

    hostname=socket.gethostname()
    this_ip=socket.gethostbyname(hostname)
    print("您的ip地址是 "+this_ip)
    sendmsg(skt,this_ip+"$6666","sendhere$")
    print("等待连接...")

    conn, addr = skt_receive.accept()
    print("连接成功！")

    while (1):
        fileinfo_size = struct.calcsize("128sl")
        buf = conn.recv(fileinfo_size)
        if buf:
            filename, filesize = struct.unpack("128sl", buf)

            # 去除空格
            fn = filename.decode().strip("\00")

            new_filename = os.path.join("./", "new_" + fn)
            print("接收的新文件为 {0},文件大小为 {1}".format(new_filename, filesize))

            recvd_size = 0
            fp = open(new_filename, "wb")
            print("开始接收文件...")

            # while not recvd_size==filesize:
            while recvd_size < filesize:
                if (filesize - recvd_size > 1024):
                    data = conn.recv(1024)
                    recvd_size += len(data)
                    process = recvd_size / filesize * 100
                    print("接收中: " + "%.2f" % process + "%")
                else:
                    data = conn.recv(filesize - recvd_size)
                    recvd_size = filesize
                fp.write(data)
            fp.close()
            print("接收完毕!")
        conn.close()
        break
    sendmsg(skt,"receive_file_over$")
    return



def clinet_thread_receive(skt):
    global clinet_receive_flag
    while (1):
        if (clinet_receive_flag == 1):
            break
        msg = skt.recv(100).decode("utf-8")
        if (msg.startswith("byebye$")):
            break
        print("\n" + msg)
    print("全局变量被改动。监听线程退出。")
    # return


def main():
    skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    skt.connect(addr0)
    print("连接成功。请选择...")
    print("1.注册\t2.登陆\t")
    choice1 = input(">>")
    if (choice1 == "1"):
        client_signup(skt)
    if (choice1 == "2"):
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
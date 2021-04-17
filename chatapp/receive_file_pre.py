import  socket,threading,time
import sys,os,struct

def socket_service():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("127.0.0.1", 8888))
    s.listen(10)

    print("waiting for connections...")
    while(1):
        conn,addr=s.accept()
        t=threading.Thread(target=dealing,args=(conn,addr))
        t.start()

def dealing(conn,addr):
    print("Accept new connection from{}".format(addr))
    conn.send("hello,ready for transmition!".encode())
    while(1):
        fileinfo_size=struct.calcsize("128sl")
        buf=conn.recv(fileinfo_size)
        if buf:
            filename,filesize=struct.unpack("128sl",buf)

            #去除空格
            fn=filename.decode().strip("\00")

            new_filename=os.path.join("./","new_"+fn)
            print("file new name is {0},filesize is {1}".format(new_filename,filesize))

            recvd_size=0
            fp=open(new_filename,"wb")
            print("start receiving...")

            # while not recvd_size==filesize:
            while recvd_size<filesize:
                if(filesize-recvd_size>1024):
                    data=conn.recv(1024)
                    recvd_size+=len(data)
                    process=recvd_size/filesize*100
                    print("Receiving process: "+"%.2f"%process+"%")
                else:
                    data=conn.recv(filesize-recvd_size)
                    recvd_size=filesize
                fp.write(data)
            fp.close()
            print("Receiving ends!")
        conn.close()
        break


if __name__=="__main__":
    socket_service()
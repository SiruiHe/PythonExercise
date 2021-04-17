import socket,os,sys,struct
def socket_client():
    #try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("127.0.0.1",8888))
    #except socket.error as msg:
    #    print(msg)
    #sys.exit(1)

    count=0
    print(s.recv(1024).decode())
    while(1):
        filepath=input("Iuput file path:")
        if len(filepath)==0:
            filepath=r"C:\Users\sword\Pictures\老中青.JPG"
        if os.path.isfile(filepath):
            fileinfo_size=struct.calcsize("128sl")
            filehead=struct.pack("128sl",bytes(os.path.basename(filepath).encode('utf-8')),
                                 os.stat(filepath).st_size)
            s.send(filehead)
            print("client filepath:{}".format(filepath))

            fp=open(filepath,"rb")
            while(1):
                data=fp.read(1024)
                count+=len(data)
                if not data:
                    print("{0} file send over.".format(filepath))
                    break
                s.send(data)
                process = count / os.stat(filepath).st_size * 100
                #print("Receiving process: " + "%.2f" % process + "%")
                print("Sending process: "+"%.2f"%process+"%")
        s.close()
        print("done.")
        break

if __name__=="__main__":
    socket_client()
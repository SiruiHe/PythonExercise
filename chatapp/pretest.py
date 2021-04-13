import threading
def printf(n):
    for i in range(n):
        print("LOVE YOU!")

def main():
    th = threading.Thread(target=printf,args=(10,))
    th.start()
    sum=0
    for i in range(100):
        sum+=i
    print("sum="+str(sum))

if __name__=="__main__":
    main()



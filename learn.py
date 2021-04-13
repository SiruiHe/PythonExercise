'''
name=""
while(name!="fuckyou"):
    name=input("please input your name")
    if(name=='fuckyou'):
        print("bye bro.")
        break
    print(name+" , your name sounds so sexy!")

print("calculate")
sum=0
for i in range(3.1,5.1):#need to be interger
    sum=sum+i
print("sum="+str(sum))

import random, sys, os


def AskForAge():
    myage = input("please input your age:")
    # print("your name is "+myname+" and the len of it is "+str(len(myname)))
    print("you will be " + str(int(myage) + 1) + " in a year.\nconguatulations!")
    myage = int(myage)
    if myage > 10:
        print("you are a men now.",end="")
    elif myage <= 10 and myage >= 5:
        print("you are still a kid.",end="")
    else:
        print("hi baby.",end="")
    return myage


def RandomOutput(age):
    times1=int(times)
    for i in range(times1):#cannot modify global varies in local domain
        temp = random.randint(1, 20)
        if (temp != 5):
            print(temp)
        else:
            print("NO COMMENTS!")
            print("I know your age is "+str(age))
            sys.exit()

age=AskForAge();
times=input("how MUCH TIMES:")
RandomOutput(age)

def test():
    global a
    a=int(a)
    if(a>1):
        print(a+1)
a=input("shuru=")
test()

import random
def test():
    a=random.randint(0,3)
    return 3//a
for i in range(10):
    try:#try except 异常处理
        print(test())
    except ZeroDivisionError:
        print("AN ERROR OUCCRED.")

def collatz(number):
    num=number
    if(num%2==0):
        num=num//2
    else:
        num=3*num+1
    print(num)
    return num
try:
    number=int(input("Enter number:\n"))
    while(1):
        if(number!=1):
            number=collatz(number)
        else:
            break
except ValueError:
    print("you have to input a integer!")

import random
president=['mao','deng','jiang','hu','xi']
num=random.randint(1,5)
print("The greatest president of China is "+president[num])
for i in range(len(president)):
    print(president[i])
love=input("who's your favorite?:")
if love not in president:
    print("Sorry.maybe he's in prison.")
else:
    if(love=='mao'or love=="xi"):
        print("really?cannot believe")
    else:
        print("i think so.")

def func(list):
    str=""
    for i in range(len(list)):
        if i!=len(list)-1:
            str=str+list[i]+", "
        else:
            str=str+"and "+list[i]
    return str

list=input("Please input...:")
print(func(list))
from pprint import *
message='It was a bright cold day in April, and the clocks were striking thirteen.'
count={}
for character in message:
    count.setdefault(character,0)#设置默认值（如果此时没有）
    count[character]=count[character]+1
pprint(count)

#一个半成品的黑白棋程序
theBoard={'top-L':' ','top-M':' ','top-R':' ',
'mid-L':' ','mid-M':' ','mid-R':' ',
'low-L':' ','low-M':' ','low-R':' '
}
def printboard(board):
    print(board['top-L']+'|'+board['top-M']+'|'+board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
turn='X'
for i in range(9):
    printboard(theBoard)
    print("Turn for "+turn+".Move on which space?")
    move=input()
    #try:
    theBoard[move]=turn
    if turn=='X':
        turn='O'
    else:
        turn='X'
    #except ZeroDivisionError:
        #print("print error.try again.")
printboard(theBoard)

president=['mao','deng','jiang','hu','xi']
a=" love ".join(president)
print(a)


#p108 项目 完成对剪切板字符串的简单处理
import pyperclip
text=pyperclip.paste()

lines=text.split('\n')
for i in range(len(lines)):
    if lines[i].startswith('*'):
        continue
    else:
        lines[i]='*'+lines[i]
text='\n'.join(lines)
pyperclip.copy(text)
print("成功！粘贴即可。")



#p111 实践项目 表格打印
tableData=[['apples','oranges','cherries','banana'],
           ['Alice','Bob','Carol','David'],
           ['dogs','cats','moose','goose']]
def printTable(tableData):
    colWidths=[0]*len(tableData)
    for i in range(len(tableData)):
        colWidths[i]=0
        for j in range(len(tableData[i])):
            temp=len(tableData[i][j])
            if(temp>colWidths[i]):
                colWidths[i]=temp
    for j in range(len(tableData[0])):  # 4
        for i in range(len(tableData)):#3
            print(tableData[i][j].rjust(colWidths[i]) + " ", end="")
        print("")

printTable(tableData)
'''




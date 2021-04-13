
'''
var=1
while(var==1):
    a=int(input("请输入一个数字"))
    print("你输入的数字是"+a)
    var=1
while(var==1):
    a=int(input("请输入一个数字"))
    print("你输入的数字是%d"%a)


bicycles=['xiarong','chongcheng','xilinsx']
for i in range(len(bicycles)):
    print("My bicycle is "+bicycles[i].title())

n=100
counter=1
sum=0
while(counter<=100):
    sum+=counter
    counter+=1
print("The sum from 1 to 100 is %d"%sum)
'''
'''
bike=['sukuzi','yamaha','sakura','keyaki','nogi']
print(bike)
bike.insert(3,'hinata')
print(bike)
lastbike=bike.pop(3)
bike.append('xiaomi')
bike.insert(0,'google')
print(bike)
print("下面开始排序测试")
print(sorted(bike))
print(bike)
bike.sort(reverse=True)
print(bike)
print(len(bike))
del bike[0]
print(bike,' ',len(bike))
for kind in range(0,3):
    print('Im in lkove it! '+bike[kind])
print("I am eccentric")

num=list(range(1,7,1))
print(num)

squares=[]
sum=0
for value in range(1,11):
    square=value**2
    sum+=square
    squares.append(square)
print(squares)
print('THE SUM IS',sum)
'''
'''
square=[value**2 for value in range(1,11)]
square2=square
print(square)
print("square2 now is",square2)
square2.append(5050)
print(square2)
print(square)
if 100 in square:
    print("True bro")

import random
s=[]
i=0
for value in range(1,10000001):
    s.append(random.randint(0,1))
    i+=1
print("total times is ",i)
print("1 totally appears",sum(s),"times,and the probability is",sum(s)/10000000)

myfriend={
    'best':'hlc',
    'old':'hcr',
    'school':'lrh',
    'university':'la',
    'politics':'hlc',
    'meme':'hlc'
}
for level,name in myfriend.items():
    print("He is my "+level+' friend, name is '+name)
print(myfriend.values())
print(set(myfriend.items()))#set的返回值是大括号（字典）？ 其实set只是一个不允许重复的列表
hobbies=['anime','japanese_idol','politics','sci-fi','sci-fi']
print(hobbies)
print((sorted(set(hobbies))))
'''
'''
aliens=[]
for num in range(20):
    alien={'color':'green','points':5,'speed':'slow'}
    aliens.append(alien)
    print(alien)
print("That's all the aliens we have for now.\n")
for alien in aliens[0:5]:#修改前五个alien的属性
    if alien['color']=='green':
        alien['color']='yellow'
        alien['speed']='fast'
        alien['points']=10
for alien in aliens[0:5]:
    print(alien)
print("......")
favorite_language={
    'hsr':['cpp','python'],
    'hcr':['c','java','python'],
    'hlc':['python','r'],
    'wyc':[],
    'liang':['objective-c']
}
for name,languages in favorite_language.items():
    if len(languages)>1:
        print("\n"+name.title()+"'s favourite languages are as follows:")
        for language in languages:
            print("\t"+language.title())
    elif len(languages)==1:
        print("\n" + name.title() + "'s favourite languages is:")
        print("\t"+languages[0])
    elif len(languages)<1:
        print("\n" + name.title()+" doesn\'t have a favorite language.")

message="Now please tell me sth"
message+="\n...about Yourself:"
info=input(message)
while info!='hesirui':
    info=input("Say that again:")
    print("Your name is "+info)
print("Welcome,HESIRUI!")

#输出100以内的质数
num=1
s=[]
while num<100:
    flag = 2
    num+=1
    while(flag<=num//2):
        if(num%flag==0):
            break
        flag+=1
    if(flag>num//2):
        s.append(num)
print(s)

def welcome(name):
    print("Hello,"+name.title())
welcome("Jack")

def build_person(first_name,last_name,age=''):
    person={"first":first_name,'last':last_name}
    if age:
        person['age']=age
    return person
test=build_person("Sirui","He",20)
print(test)

def greet_users(names):
    for name in names:
        print("Hello,"+name)

part1=['HESORO','ADIA','SRIRI','ABRAMEHM']
greet_users(part1)

class Dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sit(self):
        print(self.name.title()+" is sitting.")
    def roll_over(self):
        print(self.name.title()+" rolled over!")
    def info(self):
        print("My dog's name is "+self.name+", his age is "+str(self.age)+"!")

my_dog=Dog('william',6)
my_dog.sit()
my_dog.roll_over()
my_dog.info()


'''
'''
import ast
start = [[2, 8, 3], [1, 0, 4], [7, 6, 5]]
for index,test in enumerate(start):
    print[]
'''
'''
test=[1,2,3,4,5]
test.append(6)
test.remove(3)
print(test.pop())
print(test)
'''
myname="heSIrUi   "
print(myname.title()+'low0')
print("\t"+myname.rstrip()+'low0')
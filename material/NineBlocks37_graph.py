import sys
import ast
import copy
from functools import cmp_to_key
sys.setrecursionlimit(1000000)

fathergraph = []
graph1 = {}
openlist = []
closedlist = []

class Vector():#用来描述节点的数据结构
    def __init__(self, value):
        self.father = 0
        self.deep = 0
        self.value = value
        self.hn = 0
        for x_index, l in enumerate(value):
            for y_index, v in enumerate(l):
                if v == 0:
                    self.x = x_index
                    self.y = y_index

    def __eq__(self, other):
        return self.value == other.value

    __hash__ = object.__hash__

    def fathers(self, v):
        self.father = v

    def deeps(self, d):
        self.deep = d


def control(s0, end):#执行搜索过程
    openlist.append(s0)
    deepmax = 50
    while openlist:
        if method=="b":#全局择优搜索，对openlist根据估价函数重新排序
            openlist.sort(key=cmp_to_key(compare_func), reverse=True)
        n = openlist.pop()
        ds = n.deep
        closedlist.append(n)
        if n == end:
            print("搜索成功。")
            break
        res = nextVector(n)
        if res and n.deep < deepmax:
            ds += 1
            M = []
            for x in res:
                if x not in fathergraph:
                    M.append(x)
            for x in M:
                x.fathers(n)
            for x in M:
                x.deeps(ds)
            for x in M:
                if (method=="a"):#广度优先搜索
                    openlist.insert(0,x)
                elif(method=="b"):#全局择优搜素
                    openlist.append(x)

            Graph(graph1, n, M)


def Graph(graph, fathervec, sonvec=[]):
    if fathervec not in graph:
        graph[fathervec] = []
        fathergraph.append(fathervec)
    if sonvec:
        for vec in sonvec:
            graph[fathervec].append(vec)
            fathergraph.append(vec)
    return graph


def nextVector(V):#扩展节点
    resultlist = []
    temp = 0
    x = V.x
    y = V.y
    if V.x == 0:
        Vlist = copy.deepcopy(V.value)
        temp = Vlist[x][y]
        Vlist[x][y] = Vlist[x + 1][y]
        Vlist[x + 1][y] = temp
        resultlist.append(Vector(Vlist))
    if V.x == 1:
        Vlist = copy.deepcopy(V.value)
        temp = Vlist[x][y]
        Vlist[x][y] = Vlist[x - 1][y]
        Vlist[x - 1][y] = temp
        resultlist.append(Vector(Vlist))
        Vlist = copy.deepcopy(V.value)
        temp = Vlist[x][y]
        Vlist[x][y] = Vlist[x + 1][y]
        Vlist[x + 1][y] = temp
        resultlist.append(Vector(Vlist))
    if V.x == 2:
        Vlist = copy.deepcopy(V.value)
        temp = Vlist[x][y]
        Vlist[x][y] = Vlist[x - 1][y]
        Vlist[x - 1][y] = temp
        resultlist.append(Vector(Vlist))
    if V.y == 0:
        Vlist = copy.deepcopy(V.value)
        temp = Vlist[x][y]
        Vlist[x][y] = Vlist[x][y + 1]
        Vlist[x][y + 1] = temp
        resultlist.append(Vector(Vlist))
    if V.y == 1:
        Vlist = copy.deepcopy(V.value)
        temp = Vlist[x][y]
        Vlist[x][y] = Vlist[x][y - 1]
        Vlist[x][y - 1] = temp
        resultlist.append(Vector(Vlist))
        Vlist = copy.deepcopy(V.value)
        temp = Vlist[x][y]
        Vlist[x][y] = Vlist[x][y + 1]
        Vlist[x][y + 1] = temp
        resultlist.append(Vector(Vlist))
    if V.y == 2:
        Vlist = copy.deepcopy(V.value)
        temp = Vlist[x][y]
        Vlist[x][y] = Vlist[x][y - 1]
        Vlist[x][y - 1] = temp
        resultlist.append(Vector(Vlist))
    return resultlist

def compare_func(vec1, vec2):#比较两个vector的代价
    fvec1 = 0
    fvec2 = 0
    for this, target in enumerate(end):
        for i in range(3):
            if vec1.value[this][i]!= target[i]:
                fvec1 += 1
            if vec2.value[this][i]!= target[i]:
                fvec2 += 1
    fvec1 += vec1.deep
    fvec2 += vec2.deep
    return fvec1 - fvec2

def compare_deep(vec1, vec2):#比较两个vector的深度
    dvec1 = vec1.deep
    dvec2 = vec2.deep
    return dvec1 - dvec2

#main program starts here
start=[[2, 8, 3], [1, 0, 4], [7, 6, 5]]
end = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
print("-----------重排九宫-----------")
if input("是否要修改默认起始状态(y/n):")=="y":
    for i in range(3):
        start[i] = ast.literal_eval(input("请以列表形式输入第" + str(i+1) + "行:"))
print("请选择您想使用的搜索策略：")
print("a.广度优先搜索\tb.全局择优搜索")
method=input("您的选择是:")
deeps = []
result = []
s = Vector(start)
fathergraph.append(s)
e = Vector(end)
control(s,e)
result_father = closedlist[len(closedlist) - 1]
while result_father:
    result.append(result_father)
    result_father = result_father.father
result.reverse()
print("解路径为：")
for x in result:
    print(x.value)
search_confirm=input("是否输出搜索过程？(y/n):")
if(search_confirm=="y"):
    if (method == "b"):#全局择优
        closedlist.sort(key=cmp_to_key(compare_deep))
    for x in closedlist:
        if x.deep not in deeps:
            deeps.append(x.deep)
            print("第",x.deep,"层的节点有：")
        for i in range(x.deep):
            print("\t",end="")
        print(x.value)
print("结束时closedlist中共有",len(closedlist),"个节点")

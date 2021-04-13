import copy
import sys
#from functools import cmp_to_key
sys.setrecursionlimit(1000000)
start0 = [[2, 8, 3], [1, 0, 4], [7, 6, 5]]
end = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
fathergraph = []
graph1 = {}
openlist = []
closedlist = []
path1 = []


class Vector(object):
    def __init__(self, value):
        super(Vector, self).__init__()
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

    def fathers(self, v):
        self.father = v

    def deeps(self, d):
        self.deep = d


def cmpVec(vec1, vec2):
    diffvec1 = 0
    diffvec2 = 0
    for index, value in enumerate(end):
        if vec1.value[index] != value:
            diffvec1 += 1
        if vec2.value[index] != value:
            diffvec2 += 1
    diffvec1 += vec1.deep
    diffvec2 += vec2.deep
    return diffvec1 - diffvec2


def inGraph(ve):
    if not fathergraph:
        return False
    for i in fathergraph:
        if i == ve:
            return True
    return False


def control(s0, end):
    openlist.append(s0)
    deepmax = 50
    while openlist:
        openlist.sort(cmp=cmpVec, reverse=True)#key=cmp_to_key
        n = openlist.pop()
        ds = n.deep
        closedlist.append(n)
        if n == end:
            print ("success")
            break
        res = nextVector(n)
        if res and n.deep < deepmax:
            ds += 1
            M = [x for x in res if x not in fathergraph]
            [x.fathers(n) for x in M]
            [x.deeps(ds) for x in M]
            [openlist.append(x) for x in M]
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


def nextVector(V):
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
        Vlist[x][y] = Vlist[x + 1][y]
        Vlist[x + 1][y] = temp
        resultlist.append(Vector(Vlist))
        Vlist = copy.deepcopy(V.value)
        temp = Vlist[x][y]
        Vlist[x][y] = Vlist[x - 1][y]
        Vlist[x - 1][y] = temp
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
        Vlist[x][y] = Vlist[x][y + 1]
        Vlist[x][y + 1] = temp
        resultlist.append(Vector(Vlist))
        Vlist = copy.deepcopy(V.value)
        temp = Vlist[x][y]
        Vlist[x][y] = Vlist[x][y - 1]
        Vlist[x][y - 1] = temp
        resultlist.append(Vector(Vlist))
    if V.y == 2:
        Vlist = copy.deepcopy(V.value)
        temp = Vlist[x][y]
        Vlist[x][y] = Vlist[x][y - 1]
        Vlist[x][y - 1] = temp
        resultlist.append(Vector(Vlist))
    return resultlist


if __name__ == '__main__':
    result = []
    s = Vector(start0)
    fathergraph.append(s)
    e = Vector(end)
    control(s, e)
    fa = closedlist[len(closedlist) - 1]
    while fa:
        result.append(fa)
        fa = fa.father
    result = result[::-1]
    for x in result:
        print (x.value)

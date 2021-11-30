from makeUnionFind import Union
from graphGeneration import Graph
from collections import defaultdict, deque

def heap_helper(edgeList, n, i):
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and edgeList[i] > edgeList[l]:
        smallest = l
    if r < n and edgeList[smallest] > edgeList[r]:
        smallest = r
    if smallest != i:
        edgeList[i], edgeList[smallest] = edgeList[smallest], edgeList[i]
        heap_helper(edgeList, n, smallest)


def kruskalsAlgo(G):
    global seen
    seen = set()

    edgeList = G.listed()

    # HeapSort the Edge List
    n = len(edgeList)
    for i in range(n, -1, -1):
        heap_helper(edgeList, n, i)
    for i in range(n-1, 0, -1):
        edgeList[i], edgeList[0] = edgeList[0], edgeList[i]
        heap_helper(edgeList, i, 0)
    
    myTraversal = Union()

    A = Graph()

    for v, u, w in edgeList:
        if myTraversal[w] != myTraversal[u]:
            A.addEdge(u,w,v)
            myTraversal.unionFind(u,w)
    
    return A

def breadthFirstSearch(G, s, t):
    s = s - 1
    t = t - 1

    path = str(s+1)

    if t == s:
        return 0, path
    
    Q = deque()
    seen = set([s])

    for w, v in G.edgeCounter(s):
        if w not in seen:
            Q.append([w,v,path+' ,'+str(w+1)])
            seen.add(w)
    
    while(True):
        w,v,path = Q.popleft()

        if w == t:
            return v, path
        
        for ws, vs in G.edgeCounter(w):
            if ws not in seen:
                Q.append([ws, min(v,vs), path+' ,'+str(ws+1)])
                seen.add(ws)







    

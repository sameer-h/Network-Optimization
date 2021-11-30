from makeUnionFind import Union
from graphGeneration import Graph
from collections import defaultdict, deque
import random
import time
# Sameer Hussain - CSCE 629 - Network Optimization

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

    #edgeList = G.listed()
    edgeList = []
    for i in G.listed():
        if i != None:
            edgeList.append(i)

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


def main():
    testElements = list(range(1,5001))
    srcs = []
    targets = []

    for _ in range(5):
        source = random.choice(testElements)
        testElements.remove(source)
        target = random.choice(testElements)
        testElements.remove(target)
        srcs.append(source)
        targets.append(target)

    testSet = list(zip(srcs,targets))
    Graph1 = []
    Graph2 = []

    for _ in range(5):
        Graph1.append(Graph.G1())
        Graph2.append(Graph.G2())
    
    bw1  = [[0]*5]*5
    path1 = [['']*5]*5
    i = 0
    for g1 in Graph1:
        j = 0
        T = kruskalsAlgo(g1)
        print("Kruskal's Graph1 Results for graph: ", i+1, '\n')
        for source, target in testSet:
            start_time = time.time()
            bw1[i][j], path1[i][j] = breadthFirstSearch(T, source, target)
            end_time = time.time() - start_time
            print("Source: ", source, "\t"+"Target: ", target)
            print("Maximum Bandwidth: ", bw1[i][j])
            print("Path Followed: ", path1[i][j])
            print("Time: " + str(end_time), "\n")
            j+=1
        print('---------------------------------------------------------\n\n\n')
        i+=1

    # bw2  = [[0]*5]*5
    # path2 = [['']*5]*5
    # i = 0
    # for g2 in Graph2:
    #     j = 0
    #     T = kruskalsAlgo(g2)
    #     print("Kruskal's Graph2 Results for graph: ", i+1, '\n')
    #     for source, target in testSet:
    #         start_time = time.time()
    #         bw2[i][j], path2[i][j] = breadthFirstSearch(T, source, target)
    #         end_time = time.time() - start_time
    #         print("Source: ", source, "\t"+"Target: ", target)
    #         print("Maximum Bandwidth: ", bw2[i][j])
    #         print("Path Followed: ", path2[i][j])
    #         print("Time: " + str(end_time), "\n")
    #         j+=1
    #     print('---------------------------------------------------------\n\n\n')
    #     i+=1 

if __name__ == "__main__":
    main()
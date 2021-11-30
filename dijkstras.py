from graphGeneration import Graph
from makeHeap import Heap, Vertex
import random
import math
import time
import sys
# Sameer Hussain - CSCE 629 - Network Optimization

V = 5000

def dijkstrasWithoutHeap(G, s, t): # Following the Dijkstra's Algorithm studied in class
    s = s-1
    t = t-1

    #Initializing variables to track
    dad = [0] * V
    status = ['unseen'] * V
    bw = [0] * V
    status[s] = 'in-tree'
    
    path = str(t+1) # string variable to track the shortest path

    #neighbors for fringes
    for w, v in G.edgeCounter(s):
        status[w] = 'fringe'
        dad[w] = s
        bw[w] = v


    while(True):
        u = -1
        v = 0

        for i in range(5000):
            if((bw[i] > v) and (status[i] == 'fringe')):
                v = bw[i]
                u = i
        
        status[u] = 'in-tree' # Vertex added to the tree

        if u == t:

            temp = t
            while (s != temp):
                temp = dad[temp]
                path = str(temp+1)+', '+path 
            
            return v, path
        

        for w, vs in G.edgeCounter(u):

            if status[w] == 'unseen':
                status[w] = 'fringe'
                dad[w] = u
                bw[w] = min(v, vs)

            elif status[w] == 'fringe' and min(v, vs) > bw[w]:
                dad[w] = u
                bw[w] = min(v, vs)


def dijkstraHeap(G, s, t):

	myHeap = Heap()
	bw = [0]*V
	parent = [-1]*V
	status = [2]*V

	path = str(t+1)
	status[s] = 0

	bw[s] = sys.maxsize

	for v in G.neighbors(s):

		bw[v.dst] = v.bw
		parent[v.dst] = s

		status[v.dst] = 1
		myHeap.insert(v.dst, bw[v.dst])

	while status[t] != 0:

		v = myHeap.maximum()
		myHeap.delete(myHeap.maximum())

		status[v] = 0
		n = G.neighbors(v)

		for i in range(len(n)):
			w = n[i].dst

			if (status[w] == 2):

				bw[w] = min(bw[v], n[i].bw)
				parent[w] = v
				status[w] = 1
				myHeap.insert(w, bw[w])

			elif (status[w] == 1 and bw[w] < min(bw[v], n[i].bw)):

				myHeap.delete(w)
				bw[w] = min(bw[v], n[i].bw)
				parent[w] = v
				myHeap.insert(w,bw[w])

	return bw[t] # max bandwidth path

def main():
    allTestVals = list(range(1,5001))
    srcs = []
    targets = []

    for _ in range(5):
        source = random.choice(allTestVals)
        allTestVals.remove(source)
        target = random.choice(allTestVals)
        allTestVals.remove(target)
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
        print("Heap-less Graph1 Results for graph: ", i+1, '\n')
        for source, target in testSet:
            start_time = time.time()
            bw1[i][j], path1[i][j] = dijkstrasWithoutHeap(g1, source, target)
            end_time = time.time() - start_time
            print("Source: ", source, "\t"+"Target: ", target)
            print("Maximum Bandwidth: ", bw1[i][j])
            print("Path Followed: ", path1[i][j])
            print("Time: " + str(end_time), "\n")
            j+=1
        print('---------------------------------------------------------\n\n\n')
        i+=1
    
    bw2  = [[0]*5]*5
    path2 = [['']*5]*5
    i = 0
    for g2 in Graph2:
        j = 0
        print("Heap-less Graph2 Results for graph: ", i+1, '\n')
        for source, target in testSet:
            start_time = time.time()
            bw2[i][j], path2[i][j] = dijkstrasWithoutHeap(g2, source, target)
            end_time = time.time() - start_time
            print("Source: ", source, "\t"+"Target: ", target)
            print("Maximum Bandwidth: ", bw2[i][j])
            print("Path Followed: ", path2[i][j])
            print("Time: " + str(end_time), "\n")
            j+=1
        print('---------------------------------------------------------\n\n\n')
        i+=1

if __name__ == '__main__':
    main()

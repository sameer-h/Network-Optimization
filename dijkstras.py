from graphGeneration import Graph
from makeHeap import Heap, Vertex, Edge
import random
import math
import time

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


def dijkstrasWithHeap(G, s, t):
    s = s - 1
    t = t - 1

    myHeap = Heap()

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
        myHeap.push([v,w])
    
    while(True):
        v, u = myHeap.pop()

        status[u] == 'in-tree'

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
                bw[w] = min(v,vs)
                myHeap.push([min(v,vs), w])

            elif ((bw[w] < min(v,vs)) and (status[w] == 'fringe')):
                dad[w] = u
                bw[w] = min(v,vs)
                myHeap.push([min(v,vs), w])





from graphGeneration import Graph
import random
import math
import time

V = 5000

def dijkstrasWithoutHeap(G, s, t):
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

# def main():
#     pool = list(range(1,5001))
#     sources = []
#     targets = []

#     for _ in range(5):
#         source = random.choice(pool)
#         pool.remove(source)
#         target = random.choice(pool)
#         pool.remove(target)
#         sources.append(source)
#         targets.append(target)

#     testSet = list(zip(sources,targets))
#     SparseG = []

#     for _ in range(5):
#         SparseG.append(Graph.G1())
    
#     bw1  = [[0]*5]*5
#     path1 = [['']*5]*5
#     #time1 = [[0 for _ in range(5)] for _ in range(5)]
#     i = 0
#     for sg in SparseG:
#         j = 0
#         print("SparseG Results for SG: ", i+1, '\n')
#         for source, target in testSet:
#             start_time = time.time()
#             bw1[i][j], path1[i][j] = dijkstrasWithoutHeap(sg, source, target)
#             end_time = time.time() - start_time
#             print("Source: ", source, "\t"+"Target: ", target)
#             print("Maximum Bandwidth: ", bw1[i][j])
#             print("Path Followed: ", path1[i][j])
#             print("Time: " + str(end_time))
#             j+=1
#         print('\n\n\n')
#         i+=1

# if __name__ == '__main__':
#     main()

        


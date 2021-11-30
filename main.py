from graphGeneration import Graph
from dijkstras import dijkstrasWithHeap, dijkstrasWithHeap
from makeHeap import Heap, Vertex, Edge
from makeUnionFind import Union
from kruskals import heap_helper, kruskalsAlgo, breadthFirstSearch
import math
import random as rand
import time

def main():
    vals = list(range(1,5001))

    #Sources and targets for testing
    src = []
    ts = []

    for _ in range(5):
        s = rand.choice(vals)
        t = rand.choice(vals)
        vals.remove(s)
        vals.remove(t)
        src.append(s)
        ts.append(t)
    
    tests = list(zip(src,ts))

    g1List = [] # List of G1 Graphs
    g2List = [] # List of G2 Graphs

    for i in range(5): #Generate 5 Graphs of each type to test
        g1List.append(Graph.G1())
        g2List.append(Graph.G2())
    
    # Each graph
    bandwidth = [[0] * 5]*5
    pathUsed = [['']*5]*5
    i = 0
    for g1 in g1List:
        j = 0
        print("For Graph G1, iteration", i+1, "we have: \n")
        for sc, tg in tests:
            start_time = time.time()
            bandwidth[sc][tg], pathUsed[sc][tg] = dijkstrasWithHeap(g1, sc, tg)
            end_time = time.time() - start_time
            print("From :", sc , " and Destination: ", tg , " we have a max bandwidth of: ", bandwidth[sc][tg])
            print("Path taken: "+pathUsed[sc][tg])
            print("Total time (s) : " + str(end_time))
            j = j + 1
        print("-------------------------------------------\n\n")
        i = i + 1
            

if __name__ == "__main__":
    main()
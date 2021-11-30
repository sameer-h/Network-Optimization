import random as rand
from collections import defaultdict

# Sameer Hussain - CSCE 629 - Network Optimization

class Vertex:
	def __init__(self, dst = 0, bw = 0):
		self.dst = dst
		self.bw = bw

class Graph:

    def __init__(self):

        self.adjacencyList = defaultdict(list)

        self.neighbor = defaultdict(set)

        self.edges = []

    def valid(self,u,v,w):
        if v not in self.neighbor[u]:
            self.neighbor[u].add(v)
            self.adjacencyList[u].append([v,w])

        if v not in self.neighbor[v]:
            self.neighbor[v].add(u)
            self.adjacencyList[v].append([u,w])

    def addEdge(self, u, v, w):
        self.valid(u,v,w) #Making sure the graph is valid and prevents duplicates
        self.edges.append([w,u,v]) #Adding to my edge list to later use in Dijkstra's Algorithm
    
    def listed(self):
        return self.edges
    
    def edgeCounter(self, v):
        return self.adjacencyList[v]

    def neighbors(self, v):
        return self.neighbor[v]

    def deg(self, v):
        n = len(self.adjacencyList[v])
        return n
    
    def G1():  
        
        Graph1 = Graph()
        #5000 vertices randomized
        stack = list(range(5000))
        rand.shuffle(stack)

        lastV = stack.pop()
        while(True):
            currV = stack.pop()
            weight = rand.randint(1,999)
            Graph1.addEdge(lastV,currV,weight)
            lastV = currV

            if not stack: # Edges between neighbors
                break

        for _ in range(10001):
            while(True):
                u = rand.randint(0,4999)
                v = rand.randint(0,4999)

                if u != v and v not in Graph1.neighbors(u):
                    weight = rand.randint(1,999)
                    Graph1.addEdge(u,v,weight)
                    break
            
                else:
                    continue
        return Graph1


    def G2():
        
        Graph2 = Graph()

        stack = list(range(5000))
        rand.shuffle(stack)

        lastV = stack.pop()
        while(True):
            currV = stack.pop()
            weight = rand.randint(1,999999)
            Graph2.addEdge(lastV, currV, weight)
            lastV = currV

            if not stack:
                break

        freeV = list(range(5000))

    #20% of the graph
        for u in range(5000):
            while(True):
                myEdges = len(Graph2.neighbors(u))

                if myEdges > 1000: #break if vertex is connected to 20% of Graph2
                    break

                while(True):
                    v = rand.choice(freeV)

                    if Graph2.deg(v) >= 1025:
                        freeV.remove(v)
                        continue

                    if u != v and v not in Graph2.neighbors(u):
                        weight = rand.randint(1,999999)
                        Graph2.addEdge(u,v,weight)
                        break

                    else:
                        continue

        #for i in Graph2.listed():
        #    print(i)
    
def main():
    Graph.G2()

if __name__ == "__main__":
    main()
        
    


import random
import math
from collections import defaultdict

class Edge:
	def __init__(self, src, dst, bw):
		self.src = src
		self.dst = dst
		self.bw = bw

class Vertex:
	def __init__(self, dst = 0, bw = 0):
		self.dst = dst
		self.bw = bw

V = 5000

class Heap:
    def __init__(self):
        self.heap = []

    def pop(self):
        store = self.heap[0]
        self.delete(0)
        return store
    
    def delete(self, x):
        heapSize = len(self.heap)

        #Error Handling
        while(heapSize == 1 and x == 0):
            self.heap.pop()
        
        #Normal
        self.heap[x] = self.heap.pop()

        heapSize = heapSize - 1

        if (self.heap[x] > self.heap[x/2]) and (x > 0): #Shift up for heap to be proper
            while ((x > 0) and (self.heap[x/2] < self.heap[x])):
                temp = self.heap[x/2]
                self.heap[x/2] = self.heap[x]
                self.heap[x] = temp
                x = x / 2

        else:
            while(((heapSize > 2*x) and (self.heap[2*x] > self.heap[x])) or (((heapSize > (2*x)+1) and (self.heap[(2*x)+1] > self.heap[x])))):
                if ((self.heap[(2*x)+1] < self.heap[2*x]) or ((heapSize - 1) == (2*x))):
                    temp2 = self.heap[x]
                    self.heap[x] = self.heap[2*x]
                    self.heap[2(x)] = temp2
                    x = 2 * x
                else:
                    temp3 = self.heap[x]
                    self.heap[x] = self.heap[(2*x)+1]
                    self.heap[(2*x)+1] = temp3
                    x = (2*x) + 1

        
    def push(self, i):
        self.heap.append(i)

        n = int(len(self.heap))-1

        while ((n > 0) and (self.heap[n//2] < self.heap[n])):
            myVal = self.heap[n//2]
            self.heap[n//2] = self.heap[n]
            self.heap[n] = myVal
            n = n // 2




        
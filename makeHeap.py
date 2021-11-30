import math
from graphGeneration import Vertex

# Sameer Hussain - CSCE 629 - Network Optimization

V = 5000
class Heap:
	def __init__(self):
		self.heap = list()
		#H VECTOR
		self.pos = [-1 for i in range(V)]

	def maximum(self):
		return self.heap[0].dst

	def delete(self, v):
		myHeap = self.pos[v]
		if myHeap > V:
			return

		self.heap.pop()
		self.pos[v] = -1

		self.heapify(myHeap)
		return

	def insert(self, v, bw):
		if len(self.heap) == V:
			return

		node = Vertex(v, bw)
		self.heap.append(node)
		i = len(self.heap) - 1
		self.pos[v] = i

		while (i != 0 and self.heap[self.parent(i)].bw < self.heap[i].bw):

			self.pos[self.heap[self.parent(i)].dst] = self.parent(i)
			i = self.parent(i)

	def parent(self, i):
		a = math.ceil((i/2)-1)
		return a

	def heapify(self, i):
		m = i
		l = 2*i+1
		r = 2*i+2

		if (l < len(self.heap) and self.heap[l].bw > self.heap[m].bw):
			m = l
		if (r < len(self.heap) and self.heap[r].bw > self.heap[m].bw):
			m = r
		if (m != i):
			self.heap[m], self.heap[i] = self.heap[i], self.heap[m]
			self.pos[self.heap[i].dst] = i

			self.pos[self.heap[m].dst] = m
			self.heapify(m)
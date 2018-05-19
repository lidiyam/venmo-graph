import collections


class Graph(object):

	def __init__(self):
		self.adjList = collections.defaultdict(set)
		self.ts_end = None
		self.ts_start = None
		self.heap = []

	def addEdge(self, u, v):
		self.adjList[u].add(v)
		self.adjList[v].add(u)

	def removeEdge(self, u, v):
		try:
			self.adjList[u].remove(v)
			self.adjList[v].remove(u)

			if len(self.adjList[u]) == 0:
				del self.adjList[u]
			if len(self.adjList[v]) == 0:
				del self.adjList[v]
		except KeyError:
			print 'edge u-v does not exist'

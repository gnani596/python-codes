class node:
	def __init__(self,data):
		self.left = None
		self.right = None
		self.data = data
class Tree:
	def createNode(self,data):
		return node(data)
	def insert(self,node,data):
		if node is None:
			return self.createNode(data)
		elif(data>node.data):
			node.right = self.insert(node.right,data)
		elif(data<node.data):
			node.left = self.insert(node.left,data)
		return node



n,q = map(int,input().split())
array = list(map(int,input().split()))
for _ in range(1,n):
	u,v = map(int,input().split())
	

class Branch: 
	
	def __init__(self):
		self.o_node = DNode()
		self.t_node = DNode()
		self.chr = ''
	def __init__(self, c):
		self.o_node = DNode()
		self.t_node = DNode()
		self.chr = c
	def __init__(self,c,f,t):
		self.o_node = f
		self.t_node = t
		self.chr = c
	def getONode(): 
		return self.o_node 
	
	def getTNode():
		return self.t_node
	
	def setTNode(t):
		self.t_node = t
	
	def setONode(f):
		self.o_node = f
class DNode:
	
	def __init__(self):
		self.branches_to = []
		self.branches_from = []
		self.final = False
		
	def __init__(self,bt,bf):
		self.branches_to = []
		self.branches_from = []
		self.final = True
		
	def setFinal():
		self.final = True
	
	def childCheck(xNode, yNode):
		if (len(xNode.branches_to) != len(yNode.branches_to)):
			return False
		else:
			j = 0
			while j < len(xNode.branches_to):
				if (xNode.branches_to)[j] == (yNode.branches_to)[j]:
					childCheck((xNode.branches_to)[j].getTNode(),(yNode.branches_to)[j].getTNode())
				else:
					return False
		return True
				
	def insert (self,word):
		terminalNodes = []
		# Phase 1 - create basic trie
		index = 0
		currentNode = self
		while (index<len(word)):
			exist = false
			for b in currentNode.branches_to:
				if b.chr == word[index]:
					currentNode = b.node
					exist = true
					index+= 1
					break
					
			if (not exist):
				newNode = DNode()
				newBranch = Branch(b.chr,currentNode,newNode)
				(newNode.branches_from).append(newBranch)
				currentNode = newNode
			if(index == len(word)-1):
				terminalNodes.append(currentNode)
		# Phase 2 - collapse
		
		for x in terminalNodes:
			if(childCheck(currentNode,x)): # childCheck - TODO
				if(currentNode.branches_from != []) and (x.branches_from != []) :
					(currentNode.branches_from)[0].setTNode(x)
				else
					####
							
	def search (word):
		currentNode = self
		while (index<len(word)):
			exist = false
			nextChar = ''
			for b in currentNode.branches_to:
				if b.chr == word[index]:
					nextChar = b.chr
					currentNode = b.node
					exist = true
					index+= 1
					break
			if(index == len(word)):
				print('')
			elif(not exist):
				print('Not found.')
			else:
				print(search+nextChar)			
# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # Write your code here.
		nodeNames = []
		self.getNodeList(array, nodeNames)
		return nodeNames
		
	def getNodeList(Node, array, nodeNames):
		nodeNames.append(Node.name)
		print("node name : " + Node.name +", array: " + str(array))
		#base case
		if Node.children is None:
			return
			
		#recursion
		for elementNode in array:
			getNodeList(elementNode, elementNode.children , nodeNames)
		return 
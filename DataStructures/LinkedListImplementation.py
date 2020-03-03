# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        # Write your code here.
		node.next = self.head
		self.head = node

    def setTail(self, node):
        # Write your code here.
        node.prev = self.tail
		self.tail = node

    def insertBefore(self, node, nodeToInsert):
        # Write your code here.
		if self.head == node:
			self.head = nodeToInsert
		nodeToInsert.next = node
		nodeToInsert.prev = node.prev
		node.prev = nodeToInsert
		
	def insertAfter(self, node, nodeToInsert):
        # Write your code here.
		# TODO: check if node exists in the list
		if self.tail == node:
			self.tail = nodeToInsert
        nodeToInsert.prev = node
		nodeToInsert.next = node.next
		node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
		# assuming non negative position values
        node = self.traverseToPosition(0, position, self.head)
		self.insertBefore(node, nodeToInsert)
		
	def traverseToPosition(self, index, position, node):
		# helper function for insertAtPosition
		#return node
		if index == position :
			return node
		elif node.next is not None:
			index += 1
			return self.traverseToPosition(index, position, node.next)
			
    def removeNodesWithValue(self, value):
        # Write your code here.
        while(containsNodeWithValue):
			self.remove(getNodeWithValue(value))

	def getNodeWithValue(self, value):
		if self.head.value == value:
			return self.head
		return self.getNodeWithValueHelper(value, self.head.next)
		
	def getNodeWithValueHelper(self, value, node):
		# assumes value exists in list
		if node.value == value:
			return node
		else :
			return self.getNodeWithValueHelper(value, node.next)
	
    def remove(self, node):
        # Write your code here.
        if self.head == node:
			self.setHead(self.head.next)
		elif self.tail == node:
			self.setTail(self.tail.prev)
		else:
			node.prev.next = node.next
			node.next.prev = node.prev

    def containsNodeWithValue(self, value):
        # Write your code here.
        if self.head is not None and self.head.value == value:
			return True
		else:
			return self.containsNodeWithValueHelper(value, self.head.next)
	
	def containsNodeWithValueHelper(self, value, node):
        # Write your code here.
		hasValue = False
        if node.value == value:
			hasValue = True
			return hasValue
		else :
			hasValue =  self.containsNodeWithValueHelper(value, node.next)
			return hasValue

	def traverseListHead(self, Node, DestinyNode):
		#the function can return none value
		if Node is None:
			return 
		if Node == DestinyNode:
			return Node
		else :
			return self.traverseListHead(Node.next, DestinyNode)
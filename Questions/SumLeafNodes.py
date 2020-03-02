# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
	if root == []:
		return []
	else:
		return branchSumsList(root, 0, [])

# helper function
def branchSumsList(tree, sum, sumsList):
	sum += tree.value

	#recursion
	if(tree.left != None):
		sumsList = branchSumsList(tree.left, sum, sumsList)
	if(tree.right != None):
		sumsList = branchSumsList(tree.right, sum, sumsList)
		
	#base case
	if(tree.left == None and tree.right == None):
		sumsList.append(sum)
	return sumsList

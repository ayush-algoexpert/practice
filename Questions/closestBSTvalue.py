def findClosestValueInBst(tree, target):
    # Write your code here.
	closestMate = tree.value
	print("target: " + str(target))
	closestMate = traverseBST(tree, target, closestMate)
	return closestMate
	

def traverseBST(tree, target, closestMate):
	# base case
	if abs(tree.value - target) <= abs(closestMate-target):
		closestMate = tree.value;
	
	#recursion	
	if(tree.left != None):
		closestMate = traverseBST(tree.left, target, closestMate)
	if(tree.right != None):
		closestMate = traverseBST(tree.right, target, closestMate)
	return closestMate
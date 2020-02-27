def twoNumberSum(array, targetSum):
    # Write your code here.

	doNumbersExist = False
	if(len(array)!=0):	
	# check every number in array
		for x in range(0,len(array)-1):
			for y in range(x+1,len(array)):
				if(array[x]+array[y]==targetSum):
					doNumbersExist = True
					outputArray=[array[x],array[y]]
	if(doNumbersExist):
		return outputArray
	else:
		return []
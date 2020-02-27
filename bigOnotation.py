import time 

array1 = list(range(1000))

#f1 1+a[0]
def function1(array):
    return 1 + array[0]

start1 = time.time()
# print('f1 = %d' % function1(array1))
function1(array1)
print("adding 1 to first index")
print(time.time() - start1)

#f2 sum(a)
def function2(array):
    sum = 0
    for i in range(len(array)):
        sum = sum + array[i]
    
    return sum
start2 = time.time()
# print('f2 = %d' % function2(array1))
function2(array1)
print("suming the array")
print(time.time() - start2)


#f3 pair(a)
def function3(array):
    string = ""
    for i in range(len(array)):
        for k in range(len(array)):
            string += '( '+ str(array[i])+ ',' +str(array[k])+ ')'

    return string
start3 = time.time()
# print('f3 = %s' % function3(array1))
function3(array1)
print("pairing the array")
print(time.time() - start3)


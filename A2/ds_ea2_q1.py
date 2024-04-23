import random
import sys
import time
import numpy as np

def getRandomArray(size):
    list = []
    for i in range(size):
        list.append(random.randint(-sys.maxsize - 1, sys.maxsize))
    return list      

def getIndicesNumpy(list):
    if(isValid(list)):

        print("----------------------")
        if(len(list) <= 20):
            print("Sort of " + str(list) + " with Numpy:")
        else:
            print("Sort of big List with Numpy:")

        start = time.time()
        indices = np.argsort(list)
        end = time.time()

        print("Time = " + str(end - start))
        if(len(list) <= 20):
            print("Indices = " + str(indices))
        return indices, end - start
    
def getIndicesNoNumpy(list):
    if(isValid(list)):

        print("----------------------")
        if(len(list) <= 20):
            print("Sort of " + str(list) + " without Numpy:")
        else:
            print("Sort of big List without Numpy:")

        start = time.time()
        indices = manualSort(list)
        end = time.time()

        print("Time = " + str(end - start))
        if(len(list) <= 20):
            print("Indices = " + str(indices))
        return indices, end - start

def isValid(list):
    if list is None:
        raise ValueError("List is Null")
    if any(not isinstance(item, (int, float)) for item in list):
        raise ValueError("List is not numerical")
    return True

def manualSort(list):
    li = []
    for i in range(len(list)):
        li.append([list[i], i])
    li.sort()
    indices = []

    for x in li:
        indices.append(x[1])
    return indices



##### MAIN #####

list1=[23, 104, 5, 190, 8, 7, -3]
list2=[]
list3=getRandomArray(1000000)
list4=["df", "dsfv", "goo"]

print("----------------------")
print ("NUMPY")

getIndicesNumpy(list1)
getIndicesNumpy(list2)
time1 = getIndicesNumpy(list3)[1]
#getIndicesNumpy(list4)

print("----------------------")
print ("NO NUMPY")

# NO NUMPY
getIndicesNoNumpy(list1)
getIndicesNoNumpy(list2)
time2 = getIndicesNoNumpy(list3)[1]
#getIndicesNoNumpy(list4)

print("----------------------")
print("----------------------")
print("Time difference Numpy/NoNumpy with big random list: NoNumpy=" + str(time2) + ", Numpy=" + str(time1) + ", Difference=" + str(time2-time1))
print("Numpy-Sort significantly faster than NoNumpy-Sort for big list (size=1000000)!")
print("----------------------")
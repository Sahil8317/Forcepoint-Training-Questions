#Question 3

import sys

def findMaximum(array):
    firstMaximum = -sys.maxsize-1
    secondMaximum =  -sys.maxsize-1
    for ele in array:
        if ele >firstMaximum:
            secondMaximum = firstMaximum
            firstMaximum = ele
    return firstMaximum,secondMaximum



arr = [100,55,64,2,1,101,98,6,34,21]
firstMax,secondMax = findMaximum(arr)
print(arr)
print("First Maximum = "+str(firstMax),"Second Maximum "+ str(secondMax))

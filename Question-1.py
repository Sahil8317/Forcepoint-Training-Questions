
#Question 1

def reverseArray (arr):
    i = 0
    j = len(arr)-1
    while i<=j:
        ele = arr[i]
        arr[i] = arr[j]
        arr[j] = ele
        i+=1
        j-=1
    return arr


arr = ['s','a','h','i','l']
print(arr)
reverseArray(arr)
print(arr)
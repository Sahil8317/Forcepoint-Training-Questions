#Question-7

def findCommonElements(arr1,arr2):
    i=0
    j=0
    ans = []
    n = len(arr1)
    m = len(arr2)
    while(i<n and j<m):
        if(arr1[i]==arr2[j]):
            ans.append(arr1[i])
            i+=1
            j+=1
        elif(arr1[i]>arr2[j]):
            j+=1
        else:
            i+=1
    return ans

arr1 = [1,3,4,6,7,9]
arr2 = [1,2,4,5,9,10]

ansArr = findCommonElements(arr1,arr2)
print(arr1)
print(arr2)
print(ansArr)




#Question 6

def maxOccurenceNumber(array):
    occurence = [0]*101    
    ans = 0
    ansFreq = 0
    for ele in array:
        occurence[ele]+=1
    for index, ele in enumerate(occurence):
        if ele>=ansFreq:
            ans = index
            ansFreq = ele

    return ans

numberArray = [40,5,40,1,2,6,8,6,40]
ans = maxOccurenceNumber(numberArray)
print(numberArray)
print(ans)

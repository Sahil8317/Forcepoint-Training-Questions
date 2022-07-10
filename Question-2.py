# Question 2


def numberOfOccurences(arr):
    occurence = [0]*101    
    for ele in arr:
        occurence[ele]+=1

    return occurence



arr = [100,67,87,85,25,62,58,32,21,22,10,0,1,2,8,9,66,99,100,12,12,15,2,6,55,91,64,45,51]
occurence = numberOfOccurences(arr)
print(arr)
for index,ele in enumerate(occurence):
    print(str(index)+" - "+str(ele),end=" ")


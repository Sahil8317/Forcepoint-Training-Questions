#Question 5

def calculateSum():
    sum = 0
    for number in range(10,1000000):
        digitSum = 0
        for j in str(number):
            digitSum+= int(j)**5
        if(digitSum==number):
            sum+=number

    return sum 


sum = calculateSum()
print("sum = "+ str(sum))


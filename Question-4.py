#Question 4

def roundOffFloatNumber(floatNum):
    temp = floatNum*10
    firstNumber = int(temp/10)
    secondNumber = temp%10
    if(secondNumber>=5):
        firstNumber+=1
    return firstNumber


number = 9.8
convertedNumber = roundOffFloatNumber(number)
print(number)
print(convertedNumber)
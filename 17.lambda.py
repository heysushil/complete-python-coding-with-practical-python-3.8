'''
Lambda Function ke bare me:

1. Ye ek anonymous function hai.
2. Lambda function me hum multiple arguemts de sakte hain. But iss fucntion ke andar kewal single expression diya ja sakta hai.

Lambda fucntion Syntax:

lambda numberOfArguments : your expression
'''

def simpleFunction():
    print('\nHello function')

# fucntion call
simpleFunction()

# lambda fucniton define and pass 2 arguments
# store lambda result on mysum
mysum = lambda num1, num2: num1 + num2

# call lambda fucntion
result = mysum(10, 20)

# print result
print('\nLambda result: ', mysum(10, 20))

# normal version of lambda fucntion
def mysumFun(num1, num2):
    mysum = num1 + num2
    return mysum

resutl = mysumFun(50, 100)
print('\nNormal result: ', mysumFun(50, 100))


'''
Question:

1. What is .md file?
2. Use lambda function in normal function.
'''
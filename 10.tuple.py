'''
About Tuple:

1. Tuple syntax: (,)
2. Tuple non-changeable hota hai.
3. Tuple me dublicate values allow hain.

Note: Rember single value tuple me hame comma dena jarui hai. Otherwise wo value simply normal value hogi.
'''

# creat tuple
mytuple = ('1',)
mytuple = (1,2,3,4,5,6,7,8)
print('\nmytuple type: ', type(mytuple))
print('\nMytuple: ', mytuple[0])

# trying to change 0 index postion value.
# mytuple[0] = 11
# print('\nMytuple: ', mytuple)

# check how many time the number will use in tuple
mytuple = (1,2,3,4,5,6,7,8,2,2,2,2,2)
mytuple.count(2)

print('\nMytuple: ', mytuple.count(2))

# chekc index postion by value
print('\nMytuple: ', mytuple.index(3))

# convert tuple into list
tuple2listConvert = list(mytuple)
print('\ntuple2listConvert type: ', type(tuple2listConvert))

tuple2listConvert.append(30)
print('\n', tuple2listConvert)

mytuple = tuple(tuple2listConvert)
print('\nMytuple: ', mytuple)

'''
Question:

1. Ek tupe creat karna hai then uske index positions ko find karna hai, positive and negative index bhi find karne hain and sath me slicing ka use kar ke bhi check karna hai.

2. Create your friend list aur isme at least 5 friends ko add karna hain then isko non-changable bana hai. 

Aur uske baad fir se isme kuch friends ko hata kar new friend ko add karn hai.
'''
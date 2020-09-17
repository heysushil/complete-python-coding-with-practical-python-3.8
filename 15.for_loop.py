'''
For loop ka work:

1. for loop sequece ko run karta hai aur iske liye ye python collection types ka use karta hai.

2. Python me collecton types:
    a. list
    b. tuple
    c. set
    d. dictonary
    e. range()

3. For loop ka syntax:
    for initialization in collectionData:
        body of for loop
'''

# use sting with for loop
name = 'Python'
name[0]
number = [1,2,3,4,5,6]
# print(number[0])
# print(number[1])


for n in number:
    print(n)

# Output: P

names = ['ram','shyam','radha','seeta']

for n in names:
    print(n)

# range use in for
# range(start, stop, difference)
for r in range(2, 21, 2):
    print(r)

'''
Question:

1. for loop me else ka use karna hai.
2. For loop me break ka use karna hai
3. For loop me continue ka use karna hai.
4. For loop me ek dictnonary ka output show karna hai:
    Example:
        data = {
            'name' : 'Your name',
            'email' : 'your email',
            'mobile' : 'your mobile',
        }
'''
'''
Python Operatores:

1. Arithmatic: +-*%
2. Assignment: =
3. Comparison:
    a. ==
    b. <=
    c. >=
4. Logical:
    a. and
    b. or
    c. not
5. Identiry:
    a. is
    b. is not
6. Membership:
    a. in
    b. not in
7. Bitwise:
    a. & (AND)
    b. | (OR)
    c. ~ (NOT)
    d. ^ (XOR)
'''

# arthmatic: + - * / % ** //
print('Multiply: ', 6 ** 2)

print('Divition floor: ', 15 // 4)

# comparison: == < > ! >= <= !=
print('\nComaprea: ', 3 == 3)
print('\nComaprea: ', 3 != 3)

# Example:
# num1 = input('Enter 1st numeber: ')
# num2 = input('Etner 2nd numeber: ')

# # print('num1 type: ', type(num1))
# # print('\nComapre: ', num1 == num2)
# print('Yes ' + num1 + ' and ' + num2 + ' are equal.')

# logical: and or not
print('\nMultiple condtions: ', 'hi' == 'hi' or 3 > 3)

# Identity: is | is not
name = 'python'
print('Identity: ', 'python' is name)
print('Identity: ', name is not 'python')

# membership: in | not in
mylist = ['ram','shyam']
print('\nmembership: ', 'ram' in mylist)
print('\nmembership: ', 'ram' not in mylist)


'''
Excercise: 

1. Condition check karna hai ki left side string and right side string len equal hai ya nahi. Ye dono string user se input kar ke lena hai.

2. Multiple conditon ka use karna hai and user se more then 3 alat-alag input le kar unpar and | or | not ke case check karne hai.
'''
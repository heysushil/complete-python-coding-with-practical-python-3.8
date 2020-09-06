# single line stirng
name = 'Python Progamming'
name = "Python Progamming"
welcome = '\nName: '
print(welcome, name)

# multiline string
multilineString = '''
        Microsoft Windows [Version 10.0.20197.1000]
    (c) 2020 Microsoft Corporation. All rights reserved.

Name:  Python Progamming
'''

print('\n', multilineString)

name = 'Python '
# name = '''
# Python
# '''
print('\nName: ', name[0])
print('\nLength of name: ', len(name))

# slicing n-1 Positive slicing (left => right)
print('\ny to h: ', name[1:4])
print('only start point: ', name[3:])
print('end point only: ', name[:3])

# Negative slicing (right to left) Python
name = 'Ram'
print('\nnegative -1: ', name[-1])
print('\nnegative -1: ', name[-2:])

# check stinge methods
name = 'poornima9'
print('\nUser title: ', name.title())
print('\nCapital: ', name.upper())
print('\nCheck sting: ', name.isalpha())
print('\nCheck sting: ', name.isalnum())

name = 'Hi Python'
getInList = name.split(' ')
print('\n', getInList)

'''
Question to do:

1. chek all positive slining on negative
2. Check most of relevant string method
'''
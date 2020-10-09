'''
Error Handling concept:

Error handling me 4 block of area use kiya jata hai:

1. try: code ko yaha par check kiya jata hai
2. except: code agar sahi hai then yaha par aayega
3. finally: at last sub close karne ke liye
4. else: last message show karane ke liye

Raise keywork ka use:
1. raise keywork ka use single line error handle ke liye kiya jata hai.

Multiple errors:

1. syntax error
2. type error
3. intentation error
4. ModuleNotFoundError
'''

# try and except

# try:
#     print(x)
# except NameError:
#     print('\nX not defined')
# except:
#     print('\nUnexpected error')


# try except with else
# x = 10
# try:
#     print(x)
# except :
#     print('\nX not defined')
# except:
#     print('\nUnexpected error')
# else:
#     print('No error found')
# finally:
#     print('\nTHis is finally')



# try:
#     myfun()
# except SyntaxError:
#     print('\nSyntax error')

# num = 5

# if num < 6:
#     raise Exception('Yaha par kewal 5 se less then values allowed hain.')

# name = 100
# if not type(name) is str:
#     raise TypeError('Only stirng values allowed.')

try:
    import myname
except ModuleNotFoundError:
    print('\nModeule name is wrong.')



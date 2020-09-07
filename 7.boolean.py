'''
Boolean Values:

1. Boolean values alwarys return Ture or False
2. Boolean values 0 ko False aur 1 to True as accept karta hai
3. Boolean method is bool()

Boolean Values kab False return karta hai:

1. bool(False)
2. bool(None)
3. bool(0)
4. bool('')
5. bool([])
6. bool(())
7. bool({})

Note: String me concatenae  or 1 se jada stirng ko marge karne ke liye hum + sign ka use karte hain.
C, C++ languages me concatenation ke liye .(dot) sign ka use kiya jata hain.
'''

print('\n', bool(1))
print('\n', bool())
print('\n', bool([]))

# example with condtion
name = input('Enter your name: ')

print('\nChek name: ', bool(name))

if bool(name) == False:
    print('You must give your name.')
else:
    print('\nName: ' + name)
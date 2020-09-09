'''
About Dictionary:

1. Dict ka syntax: {key:value}
2. Ye same to same associative array hai jiska use c ya c++ me kiya jata hai.
'''

data = {
    'name' : 'poornima',
    'course' : 'Python'
}

print('\ndata type: ', type(data))
print('\ndata: ', data)

# get single keys value
print('\ndata: ', data['name'])

# add new key
data['address'] = 'My India'

name = data['name']

# get value by get()
print('\nName: ', data.get('name'))

# find length
print('\ndata length: ', len(data))

# remove value by key using pop()
data.pop('name')

# remove last key:value form dict using popitem()
data.popitem()

# delete complete dict using del keywork
del data

data = data = {
    'name' : 'poornima',
    'course' : 'Python',
    'mobile' : 8998989879,
    'address' : 'India',
}

# make dublicate dict using copy()
newdata = data.copy()

# empty the dict using clear()
data.clear()

print('\ndata: ', data)
print('\nnewdata: ', newdata)

# get only keys using kyes()
print('\nkeys: ', newdata.keys())

# get only values using values()
print('\nvalues: ', newdata.values())

# nested dict using
data = {
    'poornima' : {
        'mobile' : 87979798,
        'address' : 'India',
    },
    'rimjhim' : {
        'mobile' : 98798798,
        'address' : 'Delhi',
    },
}
print('\n', data['poornima']['mobile'])

'''
Question:

1. Apne alag-alag friedns ka data set bana hai using dict and in sabhi friends ke detail ko dict mese multi line stirng ka use karke show karna hai.

Example: Output
----------------------------------------
        FriendName Data
----------------------------------------
Name: ____________
Email: ____________
Address: __________________
Mobile: ______________________

2. Jo upar friends dict banaya hai useme kuch new friends ko add karna hai and old friends ko remove karna hai alag se.

Aur ye kaam karne se pahle apne old friend list ka ek backup bhi lena hai.
'''
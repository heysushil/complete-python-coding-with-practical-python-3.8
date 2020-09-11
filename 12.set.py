'''
Set jo hai ye list, tuple aur dictinary se alag hai. Because isme existing values ka koi fix index position nahi hota hai.

Set ke barem me kuch points:

1. set ka syntax: {}
2. set me dublicate values not allowed.
3. set values non-index form me hote hain.
4. set ke andar hum union, intersection etc... work kar sakte hain.
'''

# define set
myset = {1,2,3,4,5,6,7,8}
print('\nmyset type: ', type(myset))

# check index postion value
# print('\nmyset[0]: ', myset[0])

# membership: in | identity: is
# list......    ==

# check any value to set collection by membership oper.
print('\nComapre is: ', 1 is myset)

# add single valeu in set
myset.add(9)

# add multiple values to set using update()
addlist = [10,11,12,13]
myset.update([10,11,12,13])

# remove a valeu using remove()
myset.remove(13)
# myset.remove(13)

# handle error on remove using discard()
myset.discard(12)
myset.discard(12)

# remove value by pop()
myset.pop()

# make copy of set using copy()
yourset = {10,11,12,13,14,15}

# union of 2 sets
unionset = myset.union(yourset)
print('\nunionset: ', unionset)

# merge 2 set into one using update()
myset.update(yourset)

# use differnec()
diffset = myset.difference(yourset)
print('\ndiffset: ', diffset)

myset.difference_update(yourset)

# myset.
print('\nmyset: ', myset)

'''
Questions:

1. Set ki copy banai hai and old set ko clear karna hai.

2. Set bana hain and set ko clear karna hain then usko delete kar dena hai.

3. 3 set banae hai aur inpar union, intersection, diffence activity perform karna hai.

4. Set ke baki sabhi methods ko check karna hai and try karn hai.
'''
'''
All Collection Types: (Array)

1. list (changeable, dublicate)
2. tuple (non-changable, dublicate)
3. dictionary (changable, non-dublicate)
4. set (non-index form, non-dublicate)
'''

# List []
mylist = [1,2,3,4,5,6]
print('\nmylist type: ', type(mylist))
print('\n', mylist)
print('\n', mylist[0])

# add new value at last of list by append()
mylist.append(11)

# directly update value to existing index position
mylist[0] = 10

# update index postion value by insert
mylist.insert(1, 12)

# make dublicate list by copy
list_1 = mylist.copy()

# extend mylist using extend
mylist.extend(list_1)

print('\nmylist: ', mylist)
print('\nList_1: ', list_1)

# find index postion using index()
print('\nFind the index position of 11: ', list_1.index(11))

# delete lats value using pop
list_1.pop()

# delete specific index postion value using pop
list_1.pop(1)

# delete value by remove
list_1.remove(10)

# empty the list using clear
list_1.clear()

# delete the list using del keywork
del list_1

# print('\nList_1: ', list_1)

# sort the list using sort()
mylist.sort()

# sort the list by desending order using sort(reverse)
mylist.sort(reverse = True)

print('\nmylist: ', mylist)

# reverse the list using reverse()
newlist = [2,4,6,5,3,1,3,5,6,7,11,2,4,6,5,3,1,3,5,6,7,11]

newlist.reverse()
print('\nReverse list: ', newlist)



'''
Question:

1. Ek python file me multiline comment me list, tuple, set aur dict ke difference serch karke likhna hai.

2. List me positive and negative position values ko print kar ke check karna hai.

3. List me positive and negative slicing bhi print kar ke check karna hai.

4. Find the length of list?

5. Ek list bana hai jisme ki input ka use karke apne friends ke name insert karne hain.

6. Jo friend list banai hai usme se app kisi bhi friend ka name remove karna cahte ho aur aysa karne ke liye app input method ka use karke ye kaam karoge.
'''
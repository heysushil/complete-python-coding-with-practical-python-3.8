'''
Python Condition use karne ke tarike:

1. Condtion sysntax:
    a. single condtion syntax:
        if yourCondtion:
            body of if

    b. condition worng hone par default else part ka use:
        if yourCondtion:
            body of if
        else:
            body of else

    c. multiple condtion ka use:
        if yourCondtion:
            body of if
        elif yourCondtion:
            body of if
        .
        .
        .
        else:
                body of else

2. Condtion ka use karne ke liye hame operatores ka use karna hota hai.

Python conditons:

Note: a and b are two varabils jinka use yaha kiya gaya hai.

1. equals: a == b
2. not equal to: a != b
3. less then: a < b
4. less then or equal to: a <= b
5. greater then: a > b
6. greater then or equla: a >=  b
'''

name = input('Enter your name: ')

# agar koi name deta hai to hum condtion ka use karke name show karyenga other waise error message show karenge.
if bool(name) == True:
    print('Hi, ',name)
else:
    print('Pleas enter your name then press enter.')

# use multiple condtion
if name.isalpha() == True:
    print('Hi, ' + name + ' welcome back.')
elif name.isalnum() == True:
    print('You used alphabets and digit. It\'s not acceptable.')
else:
    print('\nSomething wrong try again.')

# 2 number ke sath condtions: also useing nested case
a = 10
b = 10
c = 20

if a > b:
    print('if a > b: true')
elif a >= b:
    print('if a >= b: true')
    # nested condtion
    if c > a:
        print('if c > a: true')
        # sub nested condtion
        if a >= b:
            print('in sub nested if a >= b: true')
else:
    print('No one right.')

# use multiple condtion in single line
if a >= b and c < a or b < c and a != b:
    print('if a >= b: condtion is right')

# pass keyword ka use:
if a >= b and c < a or b < c and a != b:
    pass

'''
Question:

1. user se name recive karna hai aur check karna hai ki agar user name me koi value deta hai to name print ho otherwise: plesa enter your name ka message show ho.

2. Program bana hai ki jisme 3 alag-alag number user se lene hai aur ye following condtion bana hai:
    a. agar first value greater hai then first user win
    b. agar second value greater then second user win
    c. same for thired user
    d. agar sabhi ke number same hai then tie ka message
    e. agar koi number galt enter hua to uska message
    f. sath me winer user ke liye ek alag se grand message aap ke tarike se jo bhi best output show kara sako.

3. Ek friend list bana hai aur agar uske sath me condtion lagana hai ki:
    a. User kisi bhi random friend ko check karna chata hai ki kya wo party me hai ya nahi. Uski madad karo ye check karne me. 

    b. Agar friend party me nahi hai then User usko party me add karna cahta hai. Uski madad karo uske friend ko party me add karne ke liye.

    c. User, jis friend ko serach kar raha hai agar wo present hai to user ko uske bare me batao.

    e. User ek friend ko party se nikalna chata hai uski madad karo. Aur jab wo friend se nikal jaye to user ko batao ki wo friend party se gaya.

Note: In question ke liye aap ko apne hisab se soch kar program karna hai aur ye sare question ke liye abhi tak jo padha hai unhi ka use karna hai.
'''
'''
Python me Loop ka use and work case.

Python me hame 2 loop case milte hain.

1. while loop
2. for loop

Note: Waise other programming languages like C, C++, PHP me hame 3 loop case milte hain. For, while, do-while. Also C, C++ jaise lanagauge me increment (++) aur decrement (--) use hota hai but python me ye use nahi hota hai.
PHP do-while syntax:
    do{
        // body of do, yaha par jo kuch bhi output show karana hai wo likha jayega.
    }while(yourConditon);

Loop ka use kyo karte hain?

1. Loop same type ke repated work ke liye use hota hai.
2. Sequence datatype - list, tuple, range ye values ko index form me sotore rakhte hain. Inka use loop me values ko one by one print karne ke liye kiya ja sakta hai.
3. Ya fir kisi bhi collection of data like database table data ko bhi hum loop ke through print kara sakte hain.
4. Loop me pre aur post increment aur decrement nahi hote hain.

While loop ka syntax:

intilization
while (condtion):
    body of while loop
    increment or decrement

While loop syntax ke baare me:

1. Intilization me koi bhi starting point decide karna hota hai. Like i = 1, Becasue loop ko hamesa starting and ending point ki need hoti hai.
2. while (i <= 10): Ye condtion hogi ki loop ko kaha tak chalna hai.
3. While body: yaha par jo kuch bhi print karna hai ya fir koi loop ya condtion chalana hai. Wo sab kuch yaha par kiya ja sakta hai.

For loop syntax:

for intilization in collectionOfValues:
    body of for loop

For loop syntax ke baare me:

1. For loop me intilization kewal variable ka hoga isme koi bhi value assign nahi karna hai. Becasue jo collection values hai usme se one by one values intilization ko recive hoga and wo usko for loop ke body ko pass karega.
2. Collection of values: Ye koi bhi collection ho sakta hai. Like as:
    a. list collection
    b. tuple collection
    c. range collection
    d. database tabel data collection
    e. so on....

If aur while loop me difference?

1. If Condtion agar sahi hai to wo condtion body me aayega aur wahi work stop ho jayega.
2. While loop me jab tak condtion sahi hai tab tak loop chalta ranega.
'''

# while loop
i = 2
while i <= 20:
    print(i)
    i += 2 # i = i + 1

# string ko loop me print karna
name = 'Hindi'
# name = []
# print(name[0]) # list 
n = 0
while n < len(name):
    print(name[n])
    n += 1

# use break
c = 0
myclass = ['ram','shyam','hari']

# while c < len(myclass):
#     print(myclass[c])
#     # use codntion with break
#     if 'shyam' == myclass[c]:
#         print('Hello, ', myclass[c], ' show your homework.')
#         break
#     c += 1

# use with continu
mynum = 0
print('3\'s Table')
while mynum <= 27:
    mynum += 3
    # check 15 number then skip it
    if mynum == 15:
        continue
    
    print(mynum)
else:
    print('WHile loop is end')

    

'''
While loop programs:

1. 1 to 10 Number print karna hai.

2. 1 to 50 number print karna hai but jab 25 number mile to hame ek alg print message show karn hai 25 numbre ke liye using condtion.

3. Ek list create karo aur usme apne friedns ka name include karo then agar first friend aaye to usko hello hi message show karna hai. Second friend aaye to usse colleage ke bareme puchna hai. Thired fried aaye to susse jo man kare wo puch lena. Yaha par multiple condtion ka use karna hai. Sath me isme sabhi friend ko while loop karne ke show karn hai.

4. Ek list create karna hai jisme ki alphabets honge aur unko while loop ka use karke print karna hai but jab bhi koi vovel aaye to usko batan hai. Yaha par while loop and condtion use hoga. Yaha par single if condtion me ye kaam karna hai iske liye multiple condtion nahi use karna hai.

5. While loop ka use kar ke 2 ka table (pahada) print karan hai.

6. 2 list bana hai:
    a. list1 = ['name','address','course','mobile']
    b. list2 = ['yourname','youraddress','yourcourse','yourmobile']

    While loop ka use karke key aur value pair me side by side data show karna hai.
    Like as:
        name => yourname
        and so on.....

Extra Question:

1. What is preincrement and post-incremet or decrement
2. do-while loop ka kya work hai aur ye kya karta hai. Yaad rahe ki ye python me nahi hota hai.
'''
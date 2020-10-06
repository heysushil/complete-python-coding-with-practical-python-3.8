'''
Inheritance Kya hai?

1. Inheritance ek concept hai jiski madad se hum code ko reuse kar sakte hain.
2. Inheritance OOP's (Object Oriented Programming) ka concetp hai to iska matalb hai ki hum iska use class ke sath hi karenge.
3. Inheritance ek class ke code ko kisi bhi dusre class me use karne ki facility deta hai.
4. Inheritance me hame 2 tarike milte hain:
    a. mutlilevel inheritance
    b. mutlipal inheritance
5. Inheritance me hame 2 tarike ki class milti hain:
    a. parent class: Ye class jiske ke pas sare concept hai.
    b. child class: Ye class jo parent class ke concepts ka use karegi.
6. Inheritance ko asani se samjhne ke liye ise hum kuch is tarike se samjh sakte hain ki:
    a. parent class: dendata (dene wala)
    b. child class: lendata (lene wala)

Multilevel inheritance kya hai?

1. Multilevel inheritance ka use class me ek chaine form me hota hai. Jaie ki a frined hai b ka, b friend hai c ka, c friend hai d ka. Then d indirectly friend hogaya a ka.
2. Yahi same concept multilevel inheritance me use hota hai.
3. Multilevel inheritance me hamesa koi bhi child class kewal single parent class ki properties ko inherit ya use karega.
4. Agar ek child class ek se jada parent class ka use karta hai then is concetp ko 'multiple inheritance kahenge'.

Multiple inheritance kya hai?

1. Yaha par ek child class ek se jada parent class ki properties ka use karta hai.
2. Iske alawa baki multilevel jaisa hi concpet hota hai.
'''

# calculater class
class Mycalculater:
    def __init__(self, num1, num2):
        self.n1 = num1
        self.n2 = num2

    def addition(self):
        add = self.n1 + self.n2
        return add
        # print('''
        # Your addition result is:

        # {} + {} = {}

        # '''.format(self.n1, self.n2, add))

    def multiplication(self):
        mul = self.n1 * self.n2
        return mul
        # print('''
        # Your multiplication result is:

        # {} * {} = {}

        # '''.format(self.n1, self.n2, mul))


# create child class
class MychildClass(Mycalculater):
    def __init__(self, num1, num2, name):
        self.name = name
        # num1 aur num2 pass karna hai parent class ke constructer ko
        Mycalculater.__init__(self, num1, num2)

    # create user funciton
    def mydata(self):
        myearning = Mycalculater.addition(self)

        data = '''
        Hi, my detail is:

        Name: {}
        Earing points: {}
        Total points: {}
        '''.format(self.name, myearning, Mycalculater.multiplication(self))

        print(data)

# create child class object
chillobj = MychildClass(20, 50, 'Python')
# print(chillobj.addition())
chillobj.mydata()

# create class object
# mycal = Mycalculater(10, 20)
# print(mycal.addition())
# mycal.multiplication()

'''
Program:

1. parent class banana hai calulater name ka jisme sum, subtract, multiplication, percantage ke methods banane hai.

    1. Yaha par percantage me 4 subjects: hindi, english, math, sci ke number teacher se add karane hain.
    2. inka percantage calulate karana hai so that is child class me iska use kiya ja sake.

    Is class ke banne ke bad me ek child class bana hai marksheet ka. Is class ke andar:

    1. student method bana hai jisme student ki following details show karani hai:
        a. name, class name, rollnumber

    2. marksheet method create karna hai jaha par multiline string ka use karke marksheet format bana hai like this:

    ----------------------------------------------
                User name Marksheet
    ----------------------------------------------
    Class Name:                 RollNumber:
    ----------------------------------------------
    Hindi:
    English:
    Math:
    Sci:
    ----------------------------------------------
    Total numebr =              Percantage:
    ----------------------------------------------
'''
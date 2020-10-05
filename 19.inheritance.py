'''
Inheritance:

1. multilevel
2. multipal
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
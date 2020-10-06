# multipal inheritance

# calculater parent class first
class Mycalculater:
    def __init__(self, num1, num2):
        self.n1 = num1
        self.n2 = num2

    def addition(self):
        add = self.n1 + self.n2
        return add

    def subtraction(self):
        mul = self.n1 - self.n2
        return mul

# student data parent class
class Student:
    def __init__(self, **studentData):
        self.name = studentData['name']
        self.myclass = studentData['myclass']

    # return student details:
    def studentDetails(self):
        mydata = '''
        ----------------------------------------------
                    {} Detail
        ----------------------------------------------
        Class Name:  {}
        ----------------------------------------------
        '''.format(self.name, self.myclass)

        return mydata

class MyResult(Mycalculater, Student):
    def __init__(self, *subjectsNumber):
        self.hindi = subjectsNumber[0]
        self.english = subjectsNumber[1]
        # self.math = subjectsNumber[2]

        # Pass 2 values to mycalculater class
        Mycalculater.__init__(self, self.hindi, self.english)

        # Pass 2 values to student parent class
        Student.__init__(self, name = subjectsNumber[2], myclass = subjectsNumber[3])

    def result(self):
        # first to show student details
        studentDetails = Student.studentDetails(self)

        # get total number of subject by Mycalculater class
        totalNumber = Mycalculater.addition(self)
        totalData = '''
        ----------------------------------------------
        Total numebr: {}
        ----------------------------------------------
        '''.format(totalNumber)

        # show student details
        print(studentDetails)

        # show subejcts and their numbers
        mysubjects = '''
        Hindi:      {}
        English:    {}
        '''.format(self.hindi, self.english)

        print(mysubjects)
        print(totalData)

# creater object of child class Myresult
myresult = MyResult(70, 88, 'Poornima', 'B.Tech')

# student data
# print(myresult.studentDetails())

# call addition method of mycalculater class to see the result
# print(myresult.addition())

# call result method to show result
myresult.result()

'''
Program:

1. Is multipal inheritacne program me mycalculater class me ek new method create kanr hai subject percantage find karne ke liye.

2. Then last me jo result abhi print kara rahe hai usme percentage bhi show karana hai.
'''
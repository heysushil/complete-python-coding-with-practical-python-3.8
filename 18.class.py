'''
Class ke bare me jankari:
1. Class ko use karne ke liye 'class' keyword ka use kiya jata hain.
2. Jaise fucntion me function ko use karne ke liye fucntion call karte hain waise hi yaha par class ko use karane ke liye 'object' banate hain.
3. Jaise single function me ek kisi work ko complete kiya jata hai. Wise hi class multiple functions aur  attributs or variables ka collection hota hai.
4. Jaise normal case me hum ek fucntion ko function kahte hain. Wise hi ek function class me as a 'method' kaha jata hain.
5. Hum class me variables ko 'attributs' kahte hain.

Note: Class ka first character hamesa capital letter me hona cahiye.
'''

# create class
class MyClass:
    # name = 'Hello Python'
    # creating constructer
    def __init__(self, name, mobile):
        self.name = name
        self.mobile = mobile
    
    def mydetail(self):
        print('\n' + self.name + ' and ' + self.mobile)

    def mypersionaldetail(self, email):
        print('''
        Hello {}, how are you?
        Is this your mobile number {}
        Is this your email id {}
        '''.format(self.name, self.mobile, email))

# create objecte
# myclass()
myobj = MyClass('Neha','987987987')

myobj.mydetail()
myobj.mypersionaldetail('python@gmail.com')
# print(myobj.name)


'''
Questions:

1. jaise sum ka funciton bayan hai waise hi aap ek Calculater name ka class banaoge aur usme sum, subtract, multiplication aur divistion ke methods banae hai. Aur ye 4 methods char alag-alag fucntion behaviour ka use karke banae hain.

2. ek calculate name ka class bana hai aur isme number of methods banae hain: addition, subtraction, division, multiplication.
'''
# mydata library file
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
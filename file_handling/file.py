'''
File handling kya hai? Kya work hota hai?

1. file handling normal jaise hum system me files create karte hai. Wahi same work hum python ke help se karenge.
2. EK file ke case me hum:
    1. file ko create karna
    2. file ko read karna
    3. file ko update karna
    4. file ko delete karna

File handling ka work:

1. File handling me 4 methods mostly use hote hain:
    1. Main method to open file: open()
        1. Sub methods for files: read()
        2. write()
        3. close()
2. Sab se pahle hum file ko open karte hain. Is case me file open karne ke sath kuch methods use karne hote hain:
    1. open() method me second argement as 4 alag tarike ke arguments pass kar sakte hain:
        1. 'r': file read ke liye, error if file not exists
        2. 'x': create file, if file exists get error
        3. 'w': open file for write, create file if not exists
        4. 'a': append - create file if not exists
    2. open() method me 2 aur arguments milte hian:
        1. 't': text - ye by default text mode ke liye hota hai
        2. 'b': binary - multimedia format (e.g: image)
'''

# open file and read it
myfile = open('file_handling/demo/demo.txt', 'r')
readfile = myfile.read()
print('\n', readfile)
myfile.close()

# open file if not exists then creat using 'x' and write down on it
name = input('Enter your name: ')
# myfile = open('file_handling/demo/' + name + '.txt', 'w')
myfile = open('file_handling/demo/' + name + '.txt', 'a')

# get data to store on file
mydata = '''Hello team how are you
Poornima?
Rimjhim?
Sushil?
'''
storeData = myfile.write(mydata)
myfile.close()

# read current file
userfilename = open('file_handling/demo/' + name + '.txt', 'r')
print('\n', userfilename.read())
userfilename.close()


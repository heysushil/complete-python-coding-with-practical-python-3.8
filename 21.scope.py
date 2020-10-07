'''
Scope ke type?

1. scope 2 type ke hain:
    1. local scope
    2. gloabl scope
2. ye scope varibale ke sath set kiye jatae hain.

Sope ka work kya hai?

1. local variable kewal function ke andar hi accessable hota hai.
2. gloabl variable function ke andar aur bahar dono jagh accessable hota hai.
'''

# a variable abhi gloablly defined hai
a = 10
print(a)

# creat function
def fucntionWithLocalScope():
    # b = local varibal hai funciton ka. Ye function ke bahar acceable nahi hai.
    b = 100

    # c = Vaiablr ek global variable hai so ye fucniton ke bahar bhi accessable hai
    global c
    c = 500
    print(a, b)

    # function ke andar function
    def innerFunction():
        print('\nInner fucntion b: ',b)
    # call inner fucniton in main fucntion
    # innerFunction()

# call fucntion
fucntionWithLocalScope()

print(c)

# innerFunction()

'''
Question:

1. Kya hum function ke andar function creat karke usko main function ke bahar bhi call kar sakte hain?
2. Agar kar sakte hain? To kaise karenge?
'''
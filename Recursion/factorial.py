# Iterative

def fac(num,factorial):
    if num==1:
        print(factorial)
        return 
    fac(num-1,factorial*num)

num = int(input("Enter an number: "))
fac(num,1)

# Recursive

def fact(num):
    if(num==0):
        return 1
    return num * fact(num-1)

num = int(input("Enter an number: "))
print(fact(num))
def Sum_N(i,num):
    if i>num:
        return 0

    return i + Sum_N(i+1,num)


num = int(input("Enter an number: "))
print(Sum_N(1,num))

# Method Two

def Sum_N2(i,sum):
    if (i<1):
        print(sum)
        return
    Sum_N2(i-1,sum+i)

num2 = int(input("Enter a num: "))
Sum_N2(num2,0)
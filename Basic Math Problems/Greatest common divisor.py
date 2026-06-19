n1 = int(input("Enter num 1 : "))
n2 = int(input("Enter num 2 : "))
gcd=0
for i in range(1,min(n1,n2)):
    if n1%i==0 and n2%i==0:
        gcd=i
print("Greatest Common Divisor :",gcd)
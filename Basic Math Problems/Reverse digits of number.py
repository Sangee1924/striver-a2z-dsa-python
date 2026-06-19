n = int(input("enter an number: "))

while (n%10==0):
    n=n//10

length = len(str(n))

for i in range(length):
    print(n%10,end="")
    n=n//10